
from typing import List

from fastapi import APIRouter, HTTPException

from app.models.computer import Computer
from app.services.computer_service import ComputerService

router = APIRouter()


@router.get("/computers", response_model=List[Computer])
async def get_computers():
    """Get a list of all computers."""
    try:
        computers = ComputerService.read_computers()
        return computers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/computers/{computer_id}", response_model=Computer)
async def get_computer(computer_id: int):
    """Get a specific computer by ID."""
    try:
        computers = ComputerService.read_computers()
        for computer in computers:
            if computer['id'] == computer_id:
                return computer
        raise HTTPException(status_code=404, detail="Computer not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/computers", response_model=Computer)
async def add_computer(computer: Computer):
    """Add a new computer."""
    try:
        ComputerService.add_computer(computer.dict())
        return computer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/computers/{computer_id}", response_model=Computer)
async def update_computer(computer_id: int, updated_computer: Computer):
    """Update an existing computer."""
    try:
        ComputerService.update_computer(computer_id, updated_computer.dict())
        return updated_computer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/computers/{computer_id}")
async def delete_computer(computer_id: int):
    """Delete a computer by ID."""
    try:
        ComputerService.delete_computer(computer_id)
        return {"detail": "Computer deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))