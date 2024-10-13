from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user import User
from app.utils.jwt import get_current_user

router = APIRouter()


def admin_required(current_user: User = Depends(get_current_user)):
    """
    Dependency to ensure the user has admin privileges.
    Raises a 403 Forbidden exception if the user is not an admin.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")


@router.get("/dashboard")
async def dashboard(current_user: User = Depends(admin_required)):
    """
    Dashboard endpoint accessible only to admin users.
    Returns a welcome message with the user's name and role.
    """
    return {"message": f"Welcome to the dashboard, {current_user.name}!", "role": current_user.role}
