"""
Vercel serverless function entry point for FastAPI
"""
import sys
import os
from pathlib import Path

# Add parent directory to path to import app
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# Change working directory to parent for model loading
os.chdir(parent_dir)

from app import app
from mangum import Mangum

# Create ASGI handler for Vercel
handler = Mangum(app, lifespan="off")

