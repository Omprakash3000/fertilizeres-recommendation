# Deployment Guide

This guide covers multiple deployment options for the Fertilizer Recommendation System.

## 🚀 Quick Deploy Options

### Option 1: Render (Recommended - Free Tier Available)

**Steps:**
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository (or use manual deploy)
4. Configure:
   - **Name**: fertilizer-recommendation
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Health Check Path**: `/api/health`
5. Click "Create Web Service"
6. Wait for deployment (5-10 minutes)
7. Your app will be live at: `https://your-app-name.onrender.com`

**Note**: Render's free tier spins down after 15 minutes of inactivity. First request may take 30-60 seconds.

---

### Option 2: Railway (Easy & Fast)

**Steps:**
1. Go to [railway.app](https://railway.app) and sign up/login
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect the Python app
5. Add environment variable (if needed):
   - `PORT` = 8000 (usually auto-set)
6. Deploy automatically
7. Your app will be live at: `https://your-app-name.up.railway.app`

**Note**: Railway provides $5 free credit monthly.

---

### Option 3: Fly.io (Great for Docker)

**Steps:**
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Sign up: `fly auth signup`
3. Login: `fly auth login`
4. Initialize: `fly launch` (in project directory)
5. Deploy: `fly deploy`
6. Your app will be live at: `https://your-app-name.fly.dev`

**Note**: Fly.io has a generous free tier.

---

### Option 4: Docker Deployment (Any Platform)

**Build and run locally:**
```bash
# Build the image
docker build -t fertilizer-app .

# Run the container
docker run -p 8000:8000 fertilizer-app
```

**Deploy to Docker Hub:**
```bash
# Tag the image
docker tag fertilizer-app yourusername/fertilizer-app

# Push to Docker Hub
docker push yourusername/fertilizer-app
```

Then deploy to any platform that supports Docker (AWS ECS, Google Cloud Run, Azure Container Instances, etc.)

---

### Option 5: PythonAnywhere (Simple & Free)

**Steps:**
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files via Files tab
3. Go to Web tab → Add a new web app
4. Choose Flask (we'll modify it)
5. Edit WSGI file to point to your FastAPI app
6. Configure static files
7. Reload web app

**Note**: Free tier has limitations but good for testing.

---

### Option 6: Heroku (Paid, but reliable)

**Steps:**
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`
5. Your app: `https://your-app-name.herokuapp.com`

---

## 📋 Pre-Deployment Checklist

- [ ] Ensure `models/fertilizer_rf.joblib` exists in your repository
- [ ] Test locally: `python app.py`
- [ ] Verify all dependencies in `requirements.txt`
- [ ] Check that `index.html` is in the root directory
- [ ] Update CORS settings if needed (currently allows all origins)

## 🔧 Environment Variables

Some platforms may require these environment variables:
- `PORT`: Server port (defaults to 8000)
- `MODEL_PATH`: Path to model file (defaults to `models/fertilizer_rf.joblib`)

## 📝 Important Notes

1. **Model File Size**: The `fertilizer_rf.joblib` file needs to be included in your deployment. Make sure it's committed to your repository.

2. **Free Tier Limitations**:
   - Render: Spins down after inactivity
   - Railway: Limited monthly credits
   - Fly.io: Limited resources
   - Plan accordingly for production use

3. **CORS**: The app currently allows all origins (`*`). For production, update `app.py` to specify allowed origins:
   ```python
   allow_origins=["https://your-domain.com"]
   ```

4. **Static Files**: The `index.html` is served directly. For better performance, consider using a CDN or static file hosting.

## 🐛 Troubleshooting

### Port Issues
- Ensure the platform sets the `PORT` environment variable
- Check that your app reads `os.environ.get("PORT", 8000)`

### Model Not Found
- Verify the model file path is correct
- Check that the file is included in your deployment
- Ensure the working directory is set correctly

### Dependencies Issues
- Make sure `requirements.txt` has all dependencies
- Some platforms may need `gunicorn` instead of `uvicorn` (add to requirements if needed)

## 🔗 Quick Links

- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [Fly.io Documentation](https://fly.io/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)

---

**Recommended for beginners**: Render or Railway (easiest setup)
**Recommended for production**: Fly.io or Docker on cloud platforms

