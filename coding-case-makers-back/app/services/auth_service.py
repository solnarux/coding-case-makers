from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.models.user import User
from app.repositories.user_repository import UserRepository
from passlib.context import CryptContext
from env import env

SECRET_KEY = env['SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_user(self, user: User) -> None:
        hashed_password = self.pwd_context.hash(user.password)
        user.password = hashed_password
        return self.user_repository.add_user(user)

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.get_user_by_email(email)
        if not user or not self.pwd_context.verify(password, user.password):
            return None
        return user

    def create_access_token(self, user: User, expires_delta: timedelta = None):
        to_encode = {"sub": user.email, "role": user.role}
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
