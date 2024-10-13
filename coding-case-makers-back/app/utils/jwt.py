from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from app.models.user import User
from app.services.auth_service import AuthService
from app.dependencies import get_user_service
from env import env

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = env['SECRET_KEY']

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create a new JWT token with the provided data and expiration time.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm="HS256")
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), service: AuthService = Depends(get_user_service)) -> User:
    """
    Retrieve the current user from the token. Raises an HTTP exception if the token is invalid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token to extract user information
        payload = jwt.decode(token, SECRET_KEY,
                             algorithms=["HS256"])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = service.user_repository.get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user