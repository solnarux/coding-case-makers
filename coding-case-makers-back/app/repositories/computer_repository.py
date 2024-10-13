from typing import List, Optional
from app.models.computer import Computer


class ComputerRepository:
    def read_computers(self) -> List[Computer]:
        """Read all computers from storage."""
        raise NotImplementedError

    def write_computers(self, computers: List[Computer]) -> None:
        """Write a list of computers to storage."""
        raise NotImplementedError

    def add_computer(self, computer: Computer) -> None:
        """Add a new computer to storage."""
        raise NotImplementedError

    def update_computer(self, computer_id: int, updated_computer: Computer) -> None:
        """Update an existing computer in storage."""
        raise NotImplementedError

    def delete_computer(self, computer_id: int) -> None:
        """Delete a computer from storage."""
        raise NotImplementedError

    def get_computer_by_id(self, computer_id: int) -> Optional[Computer]:
        """Retrieve a computer by ID from storage."""
        raise NotImplementedError

    def get_computers_by_attributes(self, attributes) -> List[Computer]:
        """Retrieve computers filtered by attributes"""
        raise NotImplementedError