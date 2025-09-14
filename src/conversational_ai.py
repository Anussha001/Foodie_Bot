from groq import Groq
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class ConversationalAI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = Groq(api_key=api_key)
        self.model = "moonshotai/kimi-k2-instruct-0905"

    def generate_response(self, user_message: str, context: Any, recommended_products: List[Dict[str, Any]], interest_score: float) -> str:
        try:
            system_prompt = self._build_system_prompt(context, recommended_products, interest_score)
            messages = [{"role": "system", "content": system_prompt}]
            for msg in context.conversation_history[-6:]:
                messages.append({"role": "user", "content": msg['user']})
                messages.append({"role": "assistant", "content": msg['bot']})
            messages.append({"role": "user", "content": user_message})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=450,
                temperature=self._adaptive_temperature(interest_score),
                top_p=0.9
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return "Sorry, I'm having some trouble right now. Could you please try again?"

    def _build_system_prompt(self, context, products, interest_score) -> str:
        # Compose prompt describing conversation state and recommended products
        prompt = f"You are FoodieBot, an intelligent fast food recommendation AI.\nInterest Score: {interest_score:.1f}%\n"
        if products:
            prompt += "Recommend the following products as appropriate:\n"
            for i, p in enumerate(products[:3], 1):
                prompt += f"{i}. {p['name']} - ${p['price']}\n"
        prompt += "Respond naturally, explaining your recommendations briefly.\n"
        return prompt

    def _adaptive_temperature(self, interest_score: float) -> float:
        if interest_score > 70:
            return 0.6
        elif interest_score > 40:
            return 0.8
        else:
            return 0.9
