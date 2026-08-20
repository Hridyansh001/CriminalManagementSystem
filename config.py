import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'crime-management-system-secret-key-2026')
    
    # Database Settings
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_NAME = os.environ.get('DB_NAME', 'crimemanagementsystem')
    DB_PORT = int(os.environ.get('DB_PORT', 3306))
    
    # Pool settings
    DB_POOL_NAME = 'cms_pool'
    DB_POOL_SIZE = int(os.environ.get('DB_POOL_SIZE', 5))
