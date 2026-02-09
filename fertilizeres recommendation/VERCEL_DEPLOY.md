# Deploy to Vercel

This guide will help you deploy your Fertilizer Recommendation System to Vercel.

## 🚀 Quick Deploy Steps

### Method 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Navigate to your project directory**:
   ```bash
   cd "fertilizeres recommendation"
   ```

4. **Deploy**:
   ```bash
   vercel
   ```
   
   Follow the prompts:
   - Set up and deploy? **Yes**
   - Which scope? (Select your account)
   - Link to existing project? **No** (for first deploy)
   - Project name? (Press Enter for default or enter custom name)
   - Directory? (Press Enter for current directory)
   - Override settings? **No**

5. **Deploy to production**:
   ```bash
   vercel --prod
   ```

6. **Your app will be live at**: `https://your-project-name.vercel.app`

---

### Method 2: Deploy via GitHub Integration

1. **Push your code to GitHub** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your-github-repo-url
   git push -u origin main
   ```

2. **Go to Vercel Dashboard**:
   - Visit [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub

3. **Import Project**:
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration

4. **Configure**:
   - Framework Preset: **Other**
   - Root Directory: `fertilizeres recommendation` (or leave blank if root)
   - Build Command: Leave blank (or `pip install -r requirements.txt`)
   - Output Directory: Leave blank
   - Install Command: `pip install -r requirements.txt`

5. **Deploy**:
   - Click "Deploy"
   - Wait for deployment (2-5 minutes)

6. **Your app will be live automatically**

---

## 📋 Pre-Deployment Checklist

- [ ] Ensure `models/fertilizer_rf.joblib` exists and is committed
- [ ] Verify `vercel.json` is in the project root
- [ ] Check that `api/index.py` exists
- [ ] Ensure `index.html` is in the project root
- [ ] Test locally: `python app.py`

## 🔧 Important Notes

### File Structure for Vercel:
```
fertilizeres recommendation/
├── api/
│   └── index.py          # Vercel serverless function
├── models/
│   └── fertilizer_rf.joblib
├── app.py                # Main FastAPI app
├── index.html            # Frontend
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── ...
```

### Requirements Update:
You may need to add `mangum` to your requirements.txt for ASGI compatibility:
```bash
echo "mangum==0.17.0" >> requirements.txt
```

### Model File Size:
- Vercel has a 50MB limit for serverless functions
- If your model file is larger, consider:
  - Using Vercel's Blob Storage
  - Hosting the model on a CDN
  - Using a smaller model

## 🐛 Troubleshooting

### Issue: "Module not found" errors
**Solution**: Ensure all dependencies are in `requirements.txt` and the model file is included.

### Issue: "Function timeout"
**Solution**: Vercel has a 10-second timeout on free tier. Consider:
- Optimizing model loading
- Using Vercel Pro for longer timeouts
- Pre-loading model in a global variable

### Issue: Frontend not loading
**Solution**: 
- Check `vercel.json` routes configuration
- Ensure `index.html` is in the root directory
- Verify static file serving is configured

### Issue: API routes not working
**Solution**:
- Check that `api/index.py` properly imports the app
- Verify route paths in `vercel.json`
- Check Vercel function logs in dashboard

## 🔗 Useful Commands

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View deployment logs
vercel logs

# List deployments
vercel ls

# Remove deployment
vercel remove
```

## 📝 Environment Variables (if needed)

If you need to set environment variables:
1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add variables like:
   - `MODEL_PATH` (if different)
   - `PORT` (usually auto-set)

## 🎯 After Deployment

1. **Test your deployment**:
   - Visit your Vercel URL
   - Test the prediction API
   - Check health endpoint: `https://your-app.vercel.app/api/health`

2. **Update Frontend API URL** (if needed):
   - The frontend in `index.html` uses `http://localhost:8000`
   - For production, it should auto-detect, but you can update line 159 in `index.html`:
   ```javascript
   const API_BASE_URL = window.location.origin;
   ```

3. **Custom Domain** (optional):
   - Go to Vercel Dashboard → Settings → Domains
   - Add your custom domain

---

**Need Help?**
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Support](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [FastAPI on Vercel](https://vercel.com/guides/deploying-fastapi-with-vercel)

