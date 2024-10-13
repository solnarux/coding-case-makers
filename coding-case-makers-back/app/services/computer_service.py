from typing import List, Optional
from app.models.computer import Computer
from app.repositories.computer_repository import ComputerRepository


class ComputerService:
    def __init__(self, repository: ComputerRepository):
        self.repository = repository

    def get_computers(self) -> List[Computer]:
        return self.repository.read_computers()

    def get_computer_by_id(self, computer_id: int) -> Optional[Computer]:
        return self.repository.get_computer_by_id(computer_id)

    def add_computer(self, computer: Computer) -> None:
        self.repository.add_computer(computer)

    def update_computer(self, computer_id: int, updated_computer: Computer) -> None:
        self.repository.update_computer(computer_id, updated_computer)

    def delete_computer(self, computer_id: int) -> None:
        self.repository.delete_computer(computer_id)
