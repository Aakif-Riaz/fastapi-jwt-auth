import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from jose import jwt

# This line loads the variables from your .env file into the system memory
load_dotenv()

# Pull the values using os.getenv
SECRET_KEY = os.getenv("SECRET_KEY") # Use this command in the terminal:  python3 -c "import secrets; print(secrets.token_hex(32))"
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
