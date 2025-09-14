import sqlite3
import json
from typing import List, Dict, Any

class RecommendationEngine:
    def __init__(self, db_path='foodiebot.db'):
        self.db_path = db_path

    def recommend(self, user_preferences: Dict[str, Any], limit: int = 8) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            query = "SELECT * FROM products WHERE active = TRUE"
            params = []

            # Filter by categories, tags, price, etc.
            if 'preferred_categories' in user_preferences:
                cats = user_preferences['preferred_categories']
                placeholders = ','.join('?' for _ in cats)
                query += f" AND category IN ({placeholders})"
                params.extend(cats)

            if 'max_budget' in user_preferences:
                query += " AND price <= ?"
                params.append(user_preferences['max_budget'])

            query += " ORDER BY popularity_score DESC LIMIT ?"
            params.append(limit)

            cursor.execute(query, params)
            rows = cursor.fetchall()

            results = []
            for row in rows:
                product = dict(row)
                for field in ['ingredients', 'dietary_tags', 'mood_tags', 'allergens']:
                    product[field] = json.loads(product[field]) if product[field] else []
                results.append(product)
            return results
