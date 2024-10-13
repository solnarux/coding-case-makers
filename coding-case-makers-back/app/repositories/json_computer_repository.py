import json
from typing import List, Optional
from app.models.computer import Computer
from app.repositories.computer_repository import ComputerRepository

class JSONComputerRepository(ComputerRepository):
    JSON_FILE_PATH = 'app/data/computers.json'

    def read_computers(self) -> List[Computer]:
        with open(self.JSON_FILE_PATH, 'r') as file:
            computers_data = json.load(file)
            return [Computer(**data) for data in computers_data]

    def get_computer_by_id(self, computer_id: int) -> Optional[Computer]:
        computers = self.read_computers()
        for computer in computers:
            if computer.id == computer_id:
                return computer
        return None

    def write_computers(self, computers: List[Computer]) -> None:
        with open(self.JSON_FILE_PATH, 'w') as file:
            json.dump([comp.dict() for comp in computers], file, indent=4)

    def add_computer(self, computer: Computer) -> None:
        computers = self.read_computers()
        computers.append(computer)
        self.write_computers(computers)

    def update_computer(self, computer_id: int, updated_computer: Computer) -> None:
        computers = self.read_computers()
        for index, computer in enumerate(computers):
            if computer.id == computer_id:
                computers[index] = updated_computer
                break
        self.write_computers(computers)

    def delete_computer(self, computer_id: int) -> None:
        computers = self.read_computers()
        computers = [computer for computer in computers if computer.id != computer_id]
        self.write_computers(computers)

