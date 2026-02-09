@echo off
echo ========================================
echo   Deploying to Vercel
echo ========================================
echo.

REM Check if Vercel CLI is installed
where vercel >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Vercel CLI not found. Installing...
    echo Please install Node.js first, then run: npm i -g vercel
    pause
    exit /b 1
)

echo Step 1: Login to Vercel (if not already logged in)
vercel login

echo.
echo Step 2: Deploying to Vercel...
vercel

echo.
echo Step 3: Deploy to production? (y/n)
set /p deploy_prod=
if /i "%deploy_prod%"=="y" (
    vercel --prod
    echo.
    echo ========================================
    echo   Deployment Complete!
    echo ========================================
    echo Your app is live at: https://your-project.vercel.app
) else (
    echo Preview deployment complete!
    echo Run 'vercel --prod' to deploy to production.
)

echo.
pause

