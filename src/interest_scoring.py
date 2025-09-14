import re
from typing import Dict, Any
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

@dataclass
class ConversationContext:
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    dietary_restrictions: list = field(default_factory=list)
    current_interest_score: float = 0.0
    conversation_depth: int = 0
    last_interest_boost: datetime = None

class InterestScoringEngine:
    ENGAGEMENT_FACTORS = {
        'specific_preferences': 15,
        'dietary_restrictions': 10,
        'budget_mention': 8,
        'mood_indication': 20,
        'question_asking': 12,
        'enthusiasm_words': 10,
        'price_inquiry': 25,
        'order_intent': 35,
        'basic_engagement': 5,
        'food_mention': 12,
        'category_mention': 18
    }

    NEGATIVE_FACTORS = {
        'hesitation': -12,
        'budget_concern': -18,
        'dietary_conflict': -25,
        'rejection': -30
    }

    def analyze_message(self, message: str, context: ConversationContext) -> Dict[str, float]:
        message_lower = message.lower()
        scores = {}

        for factor, points in self.ENGAGEMENT_FACTORS.items():
            pattern = re.compile(r'\b' + re.escape(factor) + r'\b')
            if pattern.search(message_lower):
                scores[factor] = points
                logger.debug(f"Positive pattern matched: {factor} +{points}")

        for factor, points in self.NEGATIVE_FACTORS.items():
            pattern = re.compile(r'\b' + re.escape(factor) + r'\b')
            if pattern.search(message_lower):
                scores[factor] = points
                logger.debug(f"Negative pattern matched: {factor} {points}")

        return scores

    def calculate_interest_score(self, scores: Dict[str, float], current_score: float) -> float:
        score_change = sum(scores.values())
        decay_factor = 0.98 if current_score > 0 else 1.0
        decayed = current_score * decay_factor
        new_score = max(0, min(100, decayed + score_change))
        logger.debug(f"Interest score updated: {current_score} -> {new_score} (change {score_change})")
        return new_score
