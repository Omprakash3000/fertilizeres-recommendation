"""
FastAPI backend for Fertilizer Recommendation System
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import os

app = FastAPI(title="Fertilizer Recommendation API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model artifact
MODEL_PATH = "models/fertilizer_rf.joblib"

def load_model():
    """Load the trained model and metadata"""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train the model first.")
    artifact = joblib.load(MODEL_PATH)
    return artifact

# Load model on startup
try:
    artifact = load_model()
    model = artifact['model']
    feature_columns = artifact['feature_columns']
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    feature_columns = None

# Request/Response models
class FertilizerInput(BaseModel):
    n: float = Field(..., description="Nitrogen content", ge=0, le=100)
    p: float = Field(..., description="Phosphorus content", ge=0, le=100)
    k: float = Field(..., description="Potassium content", ge=0, le=100)
    temperature: float = Field(..., description="Temperature in Celsius", ge=-50, le=50)
    humidity: float = Field(..., description="Humidity percentage", ge=0, le=100)
    moisture: float = Field(..., description="Soil moisture percentage", ge=0, le=100)
    soil_type: str = Field(..., description="Soil type (Sandy, Loamy, Clayey, etc.)")
    crop_type: str = Field(..., description="Crop type (Rice, Wheat, Maize, etc.)")

class PredictionResponse(BaseModel):
    predicted_fertilizer: str
    probabilities: dict
    confidence: float

def prepare_input_df(df_raw, feature_columns):
    """Prepare input dataframe to match training features"""
    df = df_raw.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    expected = ['n', 'p', 'k', 'temperature', 'humidity', 'moisture', 'soil_type', 'crop_type']
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Input is missing required columns: {missing}")

    # Convert numeric columns
    for col in ['n', 'p', 'k', 'temperature', 'humidity', 'moisture']:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Standardize categorical columns
    for col in ['soil_type', 'crop_type']:
        df[col] = df[col].astype(str).str.strip()

    # One-hot encode categorical columns
    df_enc = pd.get_dummies(df, columns=['soil_type', 'crop_type'], drop_first=False)

    # Align with training feature columns
    for col in feature_columns:
        if col not in df_enc.columns:
            df_enc[col] = 0
    
    df_enc = df_enc[feature_columns]
    return df_enc

@app.get("/")
async def read_root():
    """Serve the frontend HTML file"""
    html_path = Path("index.html")
    if not html_path.exists():
        raise HTTPException(status_code=404, detail="Frontend file not found")
    return FileResponse(html_path)

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/api/predict", response_model=PredictionResponse)
async def predict_fertilizer(input_data: FertilizerInput):
    """Predict fertilizer recommendation based on input parameters"""
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Please train the model first.")
    
    try:
        # Convert input to DataFrame
        df_input = pd.DataFrame([{
            'n': input_data.n,
            'p': input_data.p,
            'k': input_data.k,
            'temperature': input_data.temperature,
            'humidity': input_data.humidity,
            'moisture': input_data.moisture,
            'soil_type': input_data.soil_type,
            'crop_type': input_data.crop_type
        }])
        
        # Prepare features
        X = prepare_input_df(df_input, feature_columns)
        
        # Make prediction
        prediction = model.predict(X)[0]
        
        # Get probabilities
        probabilities = {}
        confidence = 0.0
        if hasattr(model, 'predict_proba'):
            probs_raw = model.predict_proba(X)[0]
            classes = model.classes_
            probabilities = {str(cls): round(float(p), 3) for cls, p in zip(classes, probs_raw) if p > 0.001}
            # Get confidence (probability of predicted class)
            pred_idx = list(classes).index(prediction)
            confidence = round(float(probs_raw[pred_idx]), 3)
        
        return PredictionResponse(
            predicted_fertilizer=str(prediction),
            probabilities=probabilities,
            confidence=confidence
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")

@app.get("/api/crop-types")
async def get_crop_types():
    """Get list of available crop types from training data"""
    # Common crop types from the dataset
    return {
        "crop_types": ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Soyabean", "Mungbean", "Tea", "Coffee", "Coconut"]
    }

@app.get("/api/soil-types")
async def get_soil_types():
    """Get list of available soil types"""
    return {
        "soil_types": ["Sandy", "Loamy", "Clayey", "Black", "Red"]
    }

if __name__ == "__main__":
    import uvicorn
    import os
    # Get port from environment variable (for cloud deployments) or default to 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

