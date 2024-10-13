import json
from faker import Faker
import random

fake = Faker()

brands = ["Dell", "HP", "Apple", "Lenovo", "Asus", "Acer", "Microsoft", "Razer"]
model_types = [
    "Inspiron", "Pavilion", "MacBook Pro", "ThinkPad", "ZenBook", "Predator",
    "Surface Laptop", "Blade", "Aspire", "Envy"
]

# Predefined descriptions for computer specifications
descriptions = [
    "High performance laptop with excellent battery life.",
    "Lightweight design perfect for travel.",
    "Suitable for gaming and multitasking.",
    "Equipped with the latest generation processor.",
    "Ideal for professionals and students alike.",
    "A sleek design with a vibrant display.",
    "Offers great value for money with powerful specs.",
    "Quiet operation and reliable performance.",
    "Comes with a warranty for peace of mind.",
    "Stylish and functional with a backlit keyboard."
]

ram_GB_options = [8, 16, 32, 64]
storage_GB_options = [256, 512, 1024, 2048]

def generate_fake_computers(num_records):
    computers = []
    for _ in range(num_records):
        brand = random.choice(brands)
        model = f"{brand} {random.choice(model_types)} {fake.random_int(min=2020, max=2023)}"

        computer = {
            "id": fake.unique.random_int(min=1, max=1000),
            "brand": brand,
            "model": model,
            "processor": fake.random_element(elements=[
                "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
                "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9"]),
            "ram": random.choice(ram_GB_options),
            "storage": random.choice(storage_GB_options),
            "price": round(fake.random_number(digits=4, fix_len=True), 2),
            "description": random.choice(descriptions),
            "stars": round(random.choices([5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0], weights=[5, 5, 5, 3, 3, 2, 2, 1, 1])[0], 1),
            "stock": fake.random_int(min=0, max=100)
        }
        computers.append(computer)
    return computers

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    num_computers = 50
    fake_computers = generate_fake_computers(num_computers)
    save_to_json(fake_computers, 'data/computers.json')