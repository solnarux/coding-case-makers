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

phone_brands = ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Sony", "Nokia"]
phone_models = [
    "iPhone 14", "Galaxy S22", "Pixel 6", "OnePlus 10", "Xiaomi 12", "Xperia 5", "Nokia G50"
]

phone_descriptions = [
    "Latest smartphone with cutting-edge technology.",
    "Affordable phone with reliable performance.",
    "Compact design with a stunning display.",
    "Perfect for photography enthusiasts.",
    "Long-lasting battery for all-day use.",
    "5G connectivity for faster internet.",
    "Durable and water-resistant design.",
    "Features a high-refresh-rate screen.",
    "Comes with an extensive warranty.",
    "Great for gaming and multitasking."
]

# Possible processors for phones
phone_processors = [
    "Apple A15 Bionic", "Snapdragon 888", "Exynos 2100",
    "Google Tensor", "MediaTek Dimensity 1200"
]

def generate_fake_computers(num_records):
    products = []
    ids_used = set()

    while len(products) < num_records:
        id = fake.unique.random_int(min=1, max=1000)
        if id in ids_used:
            continue
        ids_used.add(id)

        brand = random.choice(brands)
        model = f"{brand} {random.choice(model_types)} {fake.random_int(min=2020, max=2023)}"

        product = {
            "id": id,
            "brand": brand,
            "model": model,
            "processor": fake.random_element(elements=[
                "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
                "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9"]),
            "ram": random.choice(ram_GB_options),
            "storage": random.choice(storage_GB_options),
            "price": round(fake.random_number(digits=4, fix_len=True), 2),
            "description": random.choice(descriptions),
            "stars": round(
                random.choices([5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0], weights=[5, 5, 5, 3, 3, 2, 2, 1, 1])[0],
                1),
            "stock": fake.random_int(min=0, max=100),
            "category": "Computer"
        }
        products.append(product)
    return products


def generate_fake_phones(num_records):
    products = []
    ids_used = set()  # To track unique IDs

    while len(products) < num_records:
        id = fake.unique.random_int(min=1001, max=2000)
        if id in ids_used:
            continue
        ids_used.add(id)

        brand = random.choice(phone_brands)
        model = f"{brand} {random.choice(phone_models)}"

        product = {
            "id": id,
            "brand": brand,
            "model": model,
            "processor": random.choice(phone_processors),  # Add processor
            "ram": random.choice([4, 6, 8]),  # Typical RAM sizes for phones
            "storage": random.choice([64, 128, 256]),
            "price": round(fake.random_number(digits=4, fix_len=True), 2),
            "description": random.choice(phone_descriptions),
            "stars": round(
                random.choices([5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0], weights=[5, 5, 5, 3, 3, 2, 2, 1, 1])[0],
                1),
            "stock": fake.random_int(min=0, max=100),
            "category": "Phone"
        }
        products.append(product)
    return products


def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    num_computers = 50
    num_phones = 50
    fake_products = generate_fake_computers(num_computers) + generate_fake_phones(num_phones)
    save_to_json(fake_products, 'app/data/products.json')