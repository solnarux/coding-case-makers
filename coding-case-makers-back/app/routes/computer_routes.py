from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models.computer import Computer
from app.services.computer_service import ComputerService
from app.dependencies import get_computer_service

router = APIRouter()


@router.get("/computers", response_model=List[Computer])
async def get_computers(service: ComputerService = Depends(get_computer_service)):
    """Get a list of all computers."""
    return service.get_computers()


@router.get("/computers/{computer_id}", response_model=Computer)
async def get_computer(computer_id: int, service: ComputerService = Depends(get_computer_service)):
    """Get a specific computer by ID."""
    computer = service.get_computer_by_id(computer_id)
    if computer is None:
        raise HTTPException(status_code=404, detail="Computer not found")
    return computer


@router.post("/computers", response_model=Computer)
async def add_computer(computer: Computer, service: ComputerService = Depends(get_computer_service)):
    """Add a new computer."""
    service.add_computer(computer)
    return computer


@router.put("/computers/{computer_id}", response_model=Computer)
async def update_computer(computer_id: int, updated_computer: Computer,
                          service: ComputerService = Depends(get_computer_service)):
    """Update an existing computer."""
    service.update_computer(computer_id, updated_computer)
    return updated_computer


@router.delete("/computers/{computer_id}")
async def delete_computer(computer_id: int, service: ComputerService = Depends(get_computer_service)):
    """Delete a computer by ID."""
    service.delete_computer(computer_id)
    return {"detail": "Computer deleted successfully"}
