from typing import List, Optional, Type
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.models.user import User


class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def read_users(self, **kwargs) -> List[Type[User]]:
        """Read users from the database and filter based on provided attributes."""
        query = self.db_session.query(User)

        filters = []

        for key, value in kwargs.items():
            if hasattr(User, key):
                filters.append(getattr(User, key) == value)

        if filters:
            query = query.filter(and_(*filters))

        return query.all()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db_session.query(User).filter_by(email=email).first()

    def write_users(self, users: List[User]) -> None:
        for user in users:
            self.db_session.add(user)
        self.db_session.commit()

    def add_user(self, user: User) -> None:
        self.db_session.add(user)
        self.db_session.commit()

    def update_user(self, email: str, updated_user: User) -> None:
        user = self.get_user_by_email(email)
        if user:
            for key, value in updated_user.model_dump().items():
                setattr(user, key, value)
            self.db_session.commit()

    def delete_user(self, email: str) -> None:
        user = self.get_user_by_email(email)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()