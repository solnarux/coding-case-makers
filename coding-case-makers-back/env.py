from dotenv import load_dotenv
import os

load_dotenv()

env = {
    'DATABASE_URL': os.getenv("DATABASE_URL"),
    'OPENAI_API_KEY': os.getenv("OPENAI_API_KEY"),
    'ORGANIZATION_ID': os.getenv("ORGANIZATION_ID"),
    'PROJECT_ID': os.getenv("PROJECT_ID")
}