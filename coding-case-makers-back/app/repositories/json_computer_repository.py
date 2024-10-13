import json
from typing import List, Optional
from app.models.computer import Computer
from app.repositories.computer_repository import ComputerRepository


class JSONComputerRepository(ComputerRepository):
    JSON_FILE_PATH = 'app/data/computers.json'

    def read_computers(self, **kwargs) -> List[Computer]:
        """Read computers from JSON file and filter based on provided attributes."""
        with open(self.JSON_FILE_PATH, 'r') as file:
            computers_data = json.load(file)
            filtered_computers = []

            for data in computers_data:
                computer = Computer(**data)
                match = True

                for key, value in kwargs.items():
                    if key in ['min_price', 'max_price']:
                        if key == 'min_price' and computer.price < value:
                            match = False
                            break
                        if key == 'max_price' and computer.price > value:
                            match = False
                            break
                    elif getattr(computer, key, None) != value:
                        match = False
                        break

                if match:
                    filtered_computers.append(computer)

            return filtered_computers

    def get_computer_by_id(self, computer_id: int) -> Optional[Computer]:
        computers = self.read_computers()
        for computer in computers:
            if computer.id == computer_id:
                return computer
        return None

    def get_computers_by_attributes(self, **kwargs) -> List[Computer]:
        computers = self.read_computers()
        filtered_computers = computers

        for key, value in kwargs.items():
            filtered_computers = [comp for comp in filtered_computers if getattr(comp, key, None) == value]

        return filtered_computers

    def write_computers(self, computers: List[Computer]) -> None:
        with open(self.JSON_FILE_PATH, 'w') as file:
            json.dump([comp.model_dump() for comp in computers], file, indent=4)

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
