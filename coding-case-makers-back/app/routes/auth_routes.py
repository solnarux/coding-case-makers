from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models.user import User
from app.services.auth_service import AuthService
from app.dependencies import get_user_service

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=User)
async def register(user: User, service: AuthService = Depends(get_user_service)):
    return service.create_user(user)


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(get_user_service)):
    user = service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = service.create_access_token(user=user)
    return {"access_token": access_token, "token_type": "bearer"}
