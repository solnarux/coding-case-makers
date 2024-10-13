from app.services.computer_service import ComputerService
from app.repositories.json_computer_repository import JSONComputerRepository


def get_computer_service() -> ComputerService:
    repository = JSONComputerRepository()
    return ComputerService(repository)
