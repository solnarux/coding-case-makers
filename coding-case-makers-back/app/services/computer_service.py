import json
from typing import List, Dict, Any

class ComputerService:
    JSON_FILE_PATH = 'app/data/computers.json'

    @classmethod
    def read_computers(cls) -> List[Dict[str, Any]]:
        with open(cls.JSON_FILE_PATH, 'r') as file:
            return json.load(file)

    @classmethod
    def write_computers(cls, computers: List[Dict[str, Any]]) -> None:
        with open(cls.JSON_FILE_PATH, 'w') as file:
            json.dump(computers, file, indent=4)

    @classmethod
    def add_computer(cls, computer: Dict[str, Any]) -> None:
        computers = cls.read_computers()
        computers.append(computer)
        cls.write_computers(computers)

    @classmethod
    def update_computer(cls, computer_id: int, updated_data: Dict[str, Any]) -> None:
        computers = cls.read_computers()
        for computer in computers:
            if computer['id'] == computer_id:
                computer.update(updated_data)
                break
        cls.write_computers(computers)

    @classmethod
    def delete_computer(cls, computer_id: int) -> None:
        computers = cls.read_computers()
        computers = [computer for computer in computers if computer['id'] != computer_id]
        cls.write_computers(computers)