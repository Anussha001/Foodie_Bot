import sqlite3
import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class FoodieBotDatabase:
    def __init__(self, db_path: str = "foodiebot.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        logger.info("Initializing database...")
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    description TEXT,
                    ingredients TEXT,
                    price REAL NOT NULL,
                    calories INTEGER,
                    prep_time TEXT,
                    dietary_tags TEXT,
                    mood_tags TEXT,
                    allergens TEXT,
                    popularity_score INTEGER DEFAULT 0,
                    chef_special BOOLEAN DEFAULT FALSE,
                    limited_time BOOLEAN DEFAULT FALSE,
                    spice_level INTEGER DEFAULT 0,
                    image_prompt TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    active BOOLEAN DEFAULT TRUE
                )
            ''')

            # Add indexes for performance as needed

            conn.commit()
        logger.info("Database initialized successfully.")

    def insert_products(self, products: List[Dict[str, Any]]) -> bool:
        logger.info(f"Inserting {len(products)} products into DB.")
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for product in products:
                    cursor.execute('''
                        INSERT OR REPLACE INTO products (
                            product_id, name, category, description, ingredients,
                            price, calories, prep_time, dietary_tags, mood_tags,
                            allergens, popularity_score, chef_special, limited_time,
                            spice_level, image_prompt, created_at, last_updated
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        product['product_id'],
                        product['name'],
                        product['category'],
                        product['description'],
                        json.dumps(product['ingredients']),
                        product['price'],
                        product['calories'],
                        product['prep_time'],
                        json.dumps(product['dietary_tags']),
                        json.dumps(product['mood_tags']),
                        json.dumps(product['allergens']),
                        product['popularity_score'],
                        product['chef_special'],
                        product['limited_time'],
                        product['spice_level'],
                        product['image_prompt'],
                        product['created_at'],
                        product['last_updated'],
                    ))
                conn.commit()
            logger.info("Products inserted successfully.")
            return True
        except Exception as e:
            logger.error(f"Error inserting products: {e}")
            return False
