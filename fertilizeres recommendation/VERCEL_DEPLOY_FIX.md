# Vercel Deployment Issue - Model File Too Large

## Problem
Vercel has a 250MB limit for serverless functions. The model file + dependencies exceed this limit.

## Solutions

### Option 1: Host Model on External Storage (Recommended)

1. **Upload model to cloud storage** (AWS S3, Google Cloud Storage, or any CDN)
2. **Update app.py to download model at runtime**:

```python
import urllib.request
import tempfile

MODEL_URL = os.environ.get("MODEL_URL", "https://your-cdn.com/models/fertilizer_rf.joblib")

def load_model():
    """Load model from external URL"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.joblib') as tmp:
        urllib.request.urlretrieve(MODEL_URL, tmp.name)
        artifact = joblib.load(tmp.name)
        os.unlink(tmp.name)
    return artifact
```

### Option 2: Use Alternative Platform (Easier)

**Render** or **Railway** don't have these size limits. Use the deployment configs already created:
- See `DEPLOYMENT.md` for Render
- See `railway.json` for Railway

### Option 3: Reduce Dependencies

Use lighter alternatives:
- Replace pandas with built-in Python (if possible)
- Use a smaller ML library
- Compress the model file

## Quick Fix: Deploy to Render Instead

1. Go to [render.com](https://render.com)
2. Connect GitHub repo
3. Deploy - no size limits!

