from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(model="gpt-4o-mini")

# Define the chatbot context
context = """
You are a helpful chatbot developed for Makers Tech e-commerce. 
You are tasked with helping customers with their queries such as stock and prices of the items. 
If the information cannot be answered with the context and information, respond with 
"I can't respond to that, How else may I help you?". 
Try to give concise answers and stick to the role as much as possible.

The context is: We have 3 Sneakers in Stock and 2 T-shirts in Stock. 
Sneakers cost $50 and T-shirts cost $20.
"""

# Function to handle conversations
def chatbot_conversation(prompt: str, conversation_history: list):
    # Add initial system message if the conversation just started
    if len(conversation_history) == 0:
        conversation_history.append(SystemMessage(content=context))
    
    # Append the human prompt to the conversation history
    conversation_history.append(HumanMessage(content=prompt))
    
    # Invoke the chat model with the conversation history
    response = chat.invoke(conversation_history)
    
    # Append the AI response to the conversation history
    conversation_history.append(AIMessage(content=response.content))
    
    # Return the AI response and updated conversation history
    return response.content, conversation_history


# Example usage
conversation_history = []
response, conversation_history = chatbot_conversation("I want to know how much sneakers cost?", conversation_history)
print(response)

response, conversation_history = chatbot_conversation("Ok and how many do you have?", conversation_history)
print(response)