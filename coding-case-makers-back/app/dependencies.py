from fastapi import Depends

from app.data.database import get_db
# from app.repositories.json_computer_repository import JSONComputerRepository
from app.repositories.db_computer_repository import DBComputerRepository
from app.services.computer_service import ComputerService


def get_computer_service(db=Depends(get_db)) -> ComputerService:
    #repository = JSONComputerRepository()
    repository = DBComputerRepository(db)
    return ComputerService(repository)
