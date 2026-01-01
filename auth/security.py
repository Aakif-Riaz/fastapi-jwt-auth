from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    try:
        # Passlib handles the 72-byte limit internally
        return pwd_context.hash(password)
    except ValueError:
        # This catches the "Password too long" error specifically
        raise ValueError("Password exceeds maximum length allowed by hashing algorithm")

def verify_password(plain_password: str, hashed_password: str):
    try:
        # Only catch ValueErrors (like the 72-char limit)
        return pwd_context.verify(plain_password, hashed_password)
    except ValueError:
        return False
        