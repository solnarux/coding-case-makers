from typing import List, Optional, Type

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models.computer import Computer
from app.repositories.computer_repository import ComputerRepository


class DBComputerRepository(ComputerRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def read_computers(self, **kwargs) -> list[Type[Computer]]:
        """Read computers from the database and filter based on provided attributes."""
        query = self.db_session.query(Computer)

        filters = []

        for key, value in kwargs.items():
            if key == 'min_price':
                filters.append(Computer.price >= value)
            elif key == 'max_price':
                filters.append(Computer.price <= value)
            elif hasattr(Computer, key):
                filters.append(getattr(Computer, key) == value)

        if filters:
            query = query.filter(and_(*filters))

        return query.all()

    def get_computer_by_id(self, computer_id: int) -> Optional[Computer]:
        return self.db_session.query(Computer).get(computer_id)

    def write_computers(self, computers: List[Computer]) -> None:
        for computer in computers:
            self.db_session.add(computer)
        self.db_session.commit()

    def add_computer(self, computer: Computer) -> None:
        self.db_session.add(computer)
        self.db_session.commit()

    def update_computer(self, computer_id: int, updated_computer: Computer) -> None:
        computer = self.db_session.query(Computer).get(computer_id)
        if computer:
            for key, value in updated_computer.dict().items():
                setattr(computer, key, value)
            self.db_session.commit()

    def delete_computer(self, computer_id: int) -> None:
        computer = self.db_session.query(Computer).get(computer_id)
        if computer:
            self.db_session.delete(computer)
            self.db_session.commit()
