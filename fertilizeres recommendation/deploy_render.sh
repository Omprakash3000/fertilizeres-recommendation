#!/bin/bash
# Quick deployment script for Render

echo "🚀 Deploying to Render..."
echo ""
echo "Make sure you have:"
echo "1. A GitHub repository with your code"
echo "2. A Render account (https://render.com)"
echo ""
echo "Steps:"
echo "1. Push your code to GitHub"
echo "2. Go to Render dashboard"
echo "3. Click 'New +' → 'Web Service'"
echo "4. Connect your GitHub repo"
echo "5. Use these settings:"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: python app.py"
echo "   - Health Check: /api/health"
echo ""
echo "Your app will be live at: https://your-app-name.onrender.com"

