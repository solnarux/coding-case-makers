import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define a list of brands and realistic model types
brands = ["Dell", "HP", "Apple", "Lenovo", "Asus", "Acer", "Microsoft", "Razer"]
model_types = [
    "Inspiron", "Pavilion", "MacBook Pro", "ThinkPad", "ZenBook", "Predator",
    "Surface Laptop", "Blade", "Aspire", "Envy"
]


def generate_fake_computers(num_records):
    computers = []
    for _ in range(num_records):
        brand = random.choice(brands)  # Choose a random brand
        model = f"{brand} {random.choice(model_types)} {fake.random_int(min=2020, max=2023)}"  # Generate model

        computer = {
            "id": fake.unique.random_int(min=1, max=1000),  # Unique ID
            "brand": brand,  # Brand name
            "model": model,  # Model name
            "processor": fake.random_element(elements=[
                "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
                "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9"]),
            "ram": fake.random_int(min=4, max=64) * 4,  # RAM in GB
            "storage": fake.random_int(min=256, max=2048) * 128,  # Storage in GB
            "price": round(fake.random_number(digits=4, fix_len=True), 2),  # Price in dollars
        }
        computers.append(computer)
    return computers


def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    num_computers = 50  # Number of fake computers to generate
    fake_computers = generate_fake_computers(num_computers)
    save_to_json(fake_computers, 'data/computers.json')
