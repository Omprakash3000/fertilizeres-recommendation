# Quick Start Guide

## 🚀 Getting Started

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server

**Option A: Using Python directly**
```bash
python app.py
```

**Option B: Using uvicorn (recommended)**
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Option C: Using the batch script (Windows)**
```bash
run_server.bat
```

**Option D: Using the shell script (Linux/Mac)**
```bash
chmod +x run_server.sh
./run_server.sh
```

### Step 3: Open Your Browser
Navigate to: **http://localhost:8000**

## 📝 How to Use

1. Fill in all the form fields:
   - **N, P, K**: Nutrient percentages (0-100)
   - **Temperature**: In Celsius (-50 to 50)
   - **Humidity**: Percentage (0-100)
   - **Soil Moisture**: Percentage (0-100)
   - **Soil Type**: Select from dropdown (Sandy, Loamy, Clayey, etc.)
   - **Crop Type**: Select from dropdown (Rice, Wheat, Maize, etc.)

2. Click **"Get Recommendation"** button

3. View the results:
   - Recommended fertilizer name
   - Confidence score
   - Probability distribution for all fertilizers

## 🔧 Troubleshooting

### Model Not Found Error
- Make sure `models/fertilizer_rf.joblib` exists
- If missing, run the training cells in `main.ipynb` first

### Port Already in Use
- Change the port in `app.py` (line 130) or use:
  ```bash
  uvicorn app:app --reload --port 8001
  ```
- Update the API URL in `index.html` (line 159) to match

### Dependencies Not Installed
```bash
pip install fastapi uvicorn pandas scikit-learn joblib pydantic
```

## 📊 API Testing

You can test the API directly using curl:

```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "n": 25,
    "p": 32,
    "k": 65,
    "temperature": 23,
    "humidity": 22,
    "moisture": 36,
    "soil_type": "Sandy",
    "crop_type": "Rice"
  }'
```

## 🎯 Example Input

Try these values to test:
- **N**: 25
- **P**: 32
- **K**: 65
- **Temperature**: 23
- **Humidity**: 22
- **Moisture**: 36
- **Soil Type**: Sandy
- **Crop Type**: Rice

Expected result: Should predict **Urea** with high confidence.

