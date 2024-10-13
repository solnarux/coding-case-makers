from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.services.user_service import UserService
from app.dependencies import get_user_service

router = APIRouter()

@router.get("/users", response_model=List[User])
async def get_users(service: UserService = Depends(get_user_service)):
    """Get a list of all users."""
    return service.get_users()

@router.get("/users/{email}", response_model=User)
async def get_user(email: str, service: UserService = Depends(get_user_service)):
    """Get a specific user by email."""
    user = service.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=User)
async def add_user(user: User, service: UserService = Depends(get_user_service)):
    """Add a new user."""
    service.add_user(user)
    return user

@router.put("/users/{email}", response_model=User)
async def update_user(email: str, updated_user: User, service: UserService = Depends(get_user_service)):
    """Update an existing user."""
    service.update_user(email, updated_user)
    return updated_user

@router.delete("/users/{email}")
async def delete_user(email: str, service: UserService = Depends(get_user_service)):
    """Delete a user by email."""
    service.delete_user(email)
    return {"detail": "User deleted successfully"}

@router.get("/users/role/{role}", response_model=List[User])
async def get_users_by_role(role: str, service: UserService = Depends(get_user_service)):
    """Get users by their role."""
    return service.get_users_by_role(role)