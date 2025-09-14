import os
import json
from fast_food_generator import FastFoodProductGenerator  # Your class extracted from notebook
from database import FoodieBotDatabase

def main():
    db_path = "foodiebot.db"
    if os.path.exists(db_path):
        os.remove(db_path)  # Remove existing DB for clean slate

    generator = FastFoodProductGenerator()
    database = FoodieBotDatabase(db_path)

    print("Generating fast food products...")
    products = generator.generate_products()

    with open('data/generated_products.json', 'w') as f:
        json.dump(products, f, indent=2)
    print("Saved product data to data/generated_products.json")

    print("Inserting products into database...")
    success = database.insert_products(products)
    if success:
        print("Database populated successfully.")
    else:
        print("Failed to insert products into the database.")

if __name__ == "__main__":
    main()
