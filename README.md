# Foodie_Bot
Here is a well-structured and detailed README content for your GitHub repository, describing your FoodieBot project:

***

# FoodieBot — Intelligent Conversational AI for Fast Food Recommendations

Welcome to **FoodieBot**, a cutting-edge AI-powered chatbot designed to deliver personalized, data-driven fast food recommendations in real-time. This repository houses the complete source code and documentation for a three-phase project that blends AI, database engineering, and conversational intelligence to create an immersive and effective food ordering assistant.

***

## Project Overview

FoodieBot is an intelligent conversational agent built for a fast-food restaurant environment. It interacts naturally with users, understands their preferences, dietary needs, moods, and budget constraints, calculates a dynamic interest score during conversations, and queries a rich product database to recommend the best-fit items. The system also tracks detailed analytics to continuously optimize recommendations and user engagement.

***

## Key Features

### Phase 1: Product Generation & Database Setup
- Automatically generates a comprehensive catalog of **100+ diverse and realistic fast food products** covering categories such as Burgers, Pizza, Fried Chicken, Tacos, Salads, Desserts, and more.
- Each product includes detailed attributes: ingredients, dietary tags, allergens, nutritional info, pricing, chef specials, and mood tags.
- Implements a **high-performance SQLite database** with normalized schema and optimized indices for fast querying.
- Supports product insertion, search, and retrieval with validation and caching.

### Phase 2: Conversational AI & Interest Scoring
- Implements a **robust conversational engine** that analyzes natural language messages to extract user preferences, dietary restrictions, budgets, and mood indicators.
- Maintains conversation context, history, and user engagement patterns over sessions.
- Calculates a **dynamic, evolving Interest Score (0-100%)** based on positive and negative user signals, enabling targeted and timely recommendations.
- Generates **context-aware, adaptive AI responses** using Groq (or alternative AI APIs), with tone adjusted to user interest and conversation phase.

### Phase 3: Advanced Recommendation & Analytics
- Provides a **smart recommendation system** combining:
  - Preference and category-based matching
  - Mood-driven filtering aligned with user emotions
  - Budget-aware filtering to optimize affordability
  - Collaborative filtering simulation to suggest popular combos
  - Avoidance of repetitively recommended products to increase variety
- Implements a **comprehensive analytics framework** tracking all conversation and recommendation events:
  - Interest progression over time
  - Popular and highly converting products
  - Category-level performance
  - Conversion rates and session metrics
- Supports real-time analytics retrieval and detailed session-specific reporting.

### User Interfaces
- **Command Line Interface** for quick testing and interaction.
- Optional **Streamlit-based web app** offering a user-friendly chat interface with live interest score display, product recommendation cards, conversation history, and analytics dashboard.

***

## Technology Stack

- Python 3.x with strong use of dataclasses and type hints
- SQLite for product data storage & analytics tracking
- Groq API and optional alternatives for AI-driven dialogue
- Streamlit for interactive web UI
- Extensive use of logging and error handling frameworks

***

## Getting Started

### Prerequisites
- Python 3.x installed
- API keys for Groq (or configured alternatives)
- Required Python packages (see `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Anussha001/Foodie_Bot.git
   cd Foodie_Bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the `GROQ_API_KEY` environment variable to your Groq access key.

### Running the Project
- **Generate the product catalog and setup the database:**
  ```bash
  python phase1_product_generation.py
  ```
- **Start the chatbot CLI:**
  ```bash
  python phase2_conversational_ai.py
  ```
- **Run Streamlit web interface:**
  ```bash
  streamlit run phase2_conversational_ai.py
  ```
  Access the UI at `http://localhost:8501`

***

## Project Architecture

```
User Input --> Conversational AI --> Interest Score --> 
    Database Query Engine --> Recommendation System --> 
        Response Generator --> User Interface

                       |
                Analytics Logging & Reporting
```

***

## Contribution

Contributions, bug fixes, and enhancements are welcome! Please open issues or submit pull requests for improvements or feature requests.

***

## License

This project is licensed under the MIT License. See the LICENSE file for details.

***

## Contact

For queries or support, please contact [anusshay01@gmail.com].

***

Experience seamless, intelligent food recommendations powered by cutting-edge AI and data science with **FoodieBot**!  

***
