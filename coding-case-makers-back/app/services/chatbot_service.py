from app.services.computer_service import ComputerService
from app.services.openai_service import OpenAIService

class ChatbotService:
    @staticmethod
    def get_computer_info(query: str) -> str:
        computers = ComputerService.read_computers()

        relevant_info = []
        for computer in computers:
            if query.lower() in computer['name'].lower() or query.lower() in computer['description'].lower():
                relevant_info.append(computer)

        if relevant_info:
            info_summary = "\n".join(
                [f"Name: {comp['name']}, Description: {comp['description']}" for comp in relevant_info]
            )
            prompt = f"Based on the following information about computers:\n{info_summary}\n\nAnswer the question: {query}"
        else:
            prompt = f"No relevant computer information found. Please ask another question about computers."

        return OpenAIService.generate_response(prompt)