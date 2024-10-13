from app.services.computer_service import ComputerService
from app.services.openai_service import OpenAIService
from app.models.computer import Computer
from typing import List


class ChatbotService:
    def __init__(self, computer_service: ComputerService):
        self.computer_service = computer_service

    def get_computer_info(self, query: str) -> str:
        computers: List[Computer] = self.computer_service.get_computers()
        normalized_query = query.lower()

        relevant_info = [
            computer for computer in computers
            if (computer.brand.lower() in normalized_query or
                computer.model.lower() in normalized_query or
                computer.description.lower() in normalized_query)
        ]

        if relevant_info:
            info_summary = "\n".join(
                [
                    f"Brand: {comp.brand}, Model: {comp.model}, "
                    f"Processor: {comp.processor}, RAM: {comp.ram}GB, "
                    f"Storage: {comp.storage}GB, Price: ${comp.price:.2f}, "
                    f"Rating: {comp.stars} stars, Stock: {comp.stock} units."
                    for comp in relevant_info
                ]
            )
            prompt = (
                f"Based on the following information about computers:\n{info_summary}\n\n"
                f"Please answer the question: {query}"
            )

            return OpenAIService.generate_response(prompt)
        return "No relevant computer information found. Please ask another question about computers."
