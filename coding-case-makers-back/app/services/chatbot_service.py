from app.services.product_service import ProductService
from app.services.openai_service import OpenAIService
from app.models.product import Product
from typing import List

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class ChatbotService:
    def __init__(self, computer_service: ProductService):
        self.computer_service = computer_service

    def get_computer_info(self, query: str) -> str:
        computers: List[Product] = self.computer_service.get_computers()
        normalized_query = query.lower()

        relevant_info = [
            computer for computer in computers
            if (computer.brand.lower() in normalized_query or
                computer.model.lower() in normalized_query or
                computer.description.lower() in normalized_query or
                str(computer.stock) in normalized_query or
                computer.processor.lower() in normalized_query
                )
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

    def get_computer_info_RAG(self, query: str) -> str:
        computers: List[Product] = self.computer_service.get_computers()
        normalized_query = query.lower()

        info_embeddings = []
        info_texts = []

        for computer in computers:
            info_text = (
                f"Brand: {computer.brand}, Model: {computer.model}, "
                f"Processor: {computer.processor}, RAM: {computer.ram}GB, "
                f"Storage: {computer.storage}GB, Price: ${computer.price:.2f}, "
                f"Rating: {computer.stars} stars, Stock: {computer.stock} units."
            )
            info_embeddings.append(OpenAIService.embed_text(info_text))
            info_texts.append(info_text)

        query_embedding = OpenAIService.embed_text(normalized_query)
        similarities = cosine_similarity([query_embedding], info_embeddings)
        top_5_indices = np.argsort(similarities[0])[-5:][::-1]

        relevant_info = [info_texts[i] for i in top_5_indices]

        if relevant_info:
            info_summary = "\n".join(relevant_info)
            prompt = (
                f"Based on the following information about computers:\n{info_summary}\n\n"
                f"Please answer the question: {query}"
            )
            return OpenAIService.generate_response(prompt)

        return "No relevant computer information found. Please ask another question about computers."