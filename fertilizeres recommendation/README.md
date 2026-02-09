# Fertilizer Recommendation System

A machine learning-based fertilizer recommendation system with a user-friendly web interface.

## Features

- 🌱 Predict optimal fertilizer based on soil and crop conditions
- 📊 Display prediction probabilities and confidence scores
- 🎨 Modern, responsive web interface
- ⚡ Fast API backend with FastAPI
- 🤖 Trained RandomForest model with 93% accuracy

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server

```bash
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 3. Access the Application

Open your web browser and navigate to:
```
http://localhost:8000
```

## API Endpoints

- `GET /` - Serves the frontend HTML page
- `GET /api/health` - Health check endpoint
- `POST /api/predict` - Predict fertilizer recommendation
- `GET /api/crop-types` - Get available crop types
- `GET /api/soil-types` - Get available soil types

## Usage

1. Fill in the form with:
   - Nitrogen (N), Phosphorus (P), Potassium (K) percentages
   - Temperature, Humidity, Soil Moisture
   - Soil Type (Sandy, Loamy, Clayey, etc.)
   - Crop Type (Rice, Wheat, Maize, etc.)

2. Click "Get Recommendation" to get the predicted fertilizer

3. View the prediction with confidence score and probability distribution

## Model Information

- **Algorithm**: RandomForest Classifier
- **Accuracy**: 93.33%
- **Features**: N, P, K, Temperature, Humidity, Moisture, Soil Type, Crop Type
- **Output**: Fertilizer recommendations (DAP, Urea, MOP, 14-35-14, 17-17-17, 28-28-0, 10-26-26)

## Project Structure

```
fertilizeres recommendation/
├── app.py                          # FastAPI backend
├── index.html                      # Frontend interface
├── main.ipynb                      # Model training notebook
├── models/
│   └── fertilizer_rf.joblib        # Trained model
├── fertilizer_dataset_cleaned.csv # Dataset
├── train.csv                       # Training data
├── test.csv                        # Test data
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Notes

- Make sure the model file exists at `models/fertilizer_rf.joblib` before running the server
- If you need to retrain the model, run the training cells in `main.ipynb`

