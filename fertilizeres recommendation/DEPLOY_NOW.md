# 🚀 Deploy to Render (Working Solution)

## Quick Steps:

1. **Go to**: https://render.com
2. **Sign up/Login** (free account works)
3. **Click**: "New +" → "Web Service"
4. **Connect**: Your GitHub repository
   - If not on GitHub yet, push your code first
5. **Configure**:
   - **Name**: fertilizer-recommendation
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Health Check Path**: `/api/health`
6. **Click**: "Create Web Service"
7. **Wait**: 5-10 minutes for deployment

## Your app will be live at:
`https://fertilizer-recommendation.onrender.com`

## ✅ Advantages:
- ✅ No size limits (unlike Vercel)
- ✅ Free tier available
- ✅ Easy setup
- ✅ All files included automatically

## 📝 Note:
Render's free tier spins down after 15 min inactivity. First request may take 30-60 seconds to wake up.

