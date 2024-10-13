from typing import List, Optional, Type
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self) -> List[Type[User]]:
        """Retrieve all users from the repository."""
        return self.repository.read_users()

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Retrieve a user by their email."""
        return self.repository.get_user_by_email(email)

    def add_user(self, user: User) -> None:
        """Add a new user to the repository."""
        self.repository.add_user(user)

    def update_user(self, email: str, updated_user: User) -> None:
        """Update user details in the repository by email."""
        self.repository.update_user(email, updated_user)

    def delete_user(self, email: str) -> None:
        """Delete a user from the repository by email."""
        self.repository.delete_user(email)

    def get_users_by_role(self, role: str) -> List[Type[User]]:
        """Retrieve users by their role."""
        return self.repository.read_users(role=role)