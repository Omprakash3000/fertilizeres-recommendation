# 🚀 Deploy to Render - Step by Step Guide

## ✅ Your code is ready! Follow these steps:

### Step 1: Push to GitHub (if not already done)

1. Go to https://github.com and create a new repository
2. Name it: `fertilizer-recommendation`
3. Copy the repository URL

Then run these commands in your terminal:
```bash
cd "C:\programming\machinelearningproject\fertilizeres recommendation"
git remote add origin YOUR_GITHUB_REPO_URL
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to**: https://render.com
2. **Sign up/Login** (use GitHub to sign in - it's easiest)
3. **Click**: "New +" button (top right)
4. **Select**: "Web Service"
5. **Connect**: Your GitHub account (if not connected)
6. **Select**: Your `fertilizer-recommendation` repository
7. **Configure**:
   - **Name**: `fertilizer-recommendation` (or any name you like)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave blank (or `fertilizeres recommendation` if deploying from subdirectory)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Health Check Path**: `/api/health`
8. **Click**: "Create Web Service"
9. **Wait**: 5-10 minutes for first deployment

### Step 3: Your App is Live! 🎉

Your app will be available at:
`https://fertilizer-recommendation.onrender.com`

(Replace `fertilizer-recommendation` with your actual service name)

## 📝 Important Notes:

- ✅ **Free tier available** - No credit card needed
- ✅ **No size limits** - Unlike Vercel, Render handles large files
- ⚠️ **Free tier spins down** after 15 minutes of inactivity
- ⚠️ **First request** after spin-down takes 30-60 seconds to wake up
- 💰 **Upgrade** to paid plan for always-on service ($7/month)

## 🔧 Troubleshooting:

- **Build fails?** Check build logs in Render dashboard
- **App not starting?** Verify `python app.py` works locally
- **Model not found?** Ensure `models/fertilizer_rf.joblib` is committed to git

## 🎯 Quick Test:

Once deployed, test these URLs:
- Frontend: `https://your-app.onrender.com`
- Health: `https://your-app.onrender.com/api/health`
- API: `https://your-app.onrender.com/api/predict` (POST)

---

**Need help?** Check Render docs: https://render.com/docs

