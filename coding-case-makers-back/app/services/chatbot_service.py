from app.services.computer_service import ComputerService
from app.services.openai_service import OpenAIService
from app.models.computer import Computer  # Ensure the import matches your project structure
from typing import List, Optional

class ChatbotService:
    @staticmethod
    def get_computer_info(query: str) -> str:
        computers: List[Computer] = ComputerService.read_computers()

        # Use list comprehension to filter relevant computers
        relevant_info = [
            computer for computer in computers
            if query.lower() in computer['name'].lower() or query.lower() in computer['description'].lower()
        ]

        if relevant_info:
            info_summary = "\n".join(
                [
                    f"Brand: {comp['brand']}, Model: {comp['model']}, "
                    f"Processor: {comp['processor']}, RAM: {comp['ram']}GB, "
                    f"Storage: {comp['storage']}GB, Price: ${comp['price']:.2f}, "
                    f"Rating: {comp['stars']} stars, Stock: {comp['stock']} units."
                    for comp in relevant_info
                ]
            )
            prompt = (
                f"Based on the following information about computers:\n{info_summary}\n\n"
                f"Please answer the question: {query}"
            )
        else:
            prompt = "No relevant computer information found. Please ask another question about computers."

        return OpenAIService.generate_response(prompt)