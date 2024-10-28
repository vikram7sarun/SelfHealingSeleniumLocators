import os

# Database configuration
DATABASE_URL = "sqlite:///healing_data.db"
DEBUG_MODE = True

# Screenshot directory
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
