from typing import List, Optional, Type
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self) -> List[Type[User]]:
        return self.repository.read_users()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.repository.get_user_by_email(email)

    def add_user(self, user: User) -> None:
        self.repository.add_user(user)

    def update_user(self, email: str, updated_user: User) -> None:
        self.repository.update_user(email, updated_user)

    def delete_user(self, email: str) -> None:
        self.repository.delete_user(email)
