import sqlite3
from typing import Dict, Any
import json
from datetime import datetime, timedelta

class AnalyticsTracker:
    def __init__(self, db_path='foodiebot.db'):
        self.db_path = db_path

    def log_event(self, session_id: str, product_id: str, event_type: str, metadata: Dict = None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO analytics (product_id, event_type, session_id, metadata)
                VALUES (?, ?, ?, ?)
            ''', (product_id, event_type, session_id, json.dumps(metadata or {})))
            conn.commit()

    def get_summary(self, days: int = 30) -> Dict[str, Any]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cutoff = datetime.now() - timedelta(days=days)

            cursor.execute('''
                SELECT product_id, COUNT(*) as rec_count
                FROM analytics
                WHERE event_type = 'recommend' AND timestamp >= ?
                GROUP BY product_id
                ORDER BY rec_count DESC
                LIMIT 10
            ''', (cutoff,))
            most_recommended = cursor.fetchall()

            # You can add more aggregated queries as needed and return as dict
            return {
                "most_recommended": most_recommended,
                "period_days": days
            }
