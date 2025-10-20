#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_travel_agent.crew import AiTravelAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("\n🌍 Welcome to AI Travel Agent! 🌍\n")
    print("Please provide the following information for your trip:\n")
    
    # Collect travel information from user
    origin = input("📍 Where are you traveling from? (city, country): ").strip()
    destination = input("✈️  Where do you want to go? (city, country): ").strip()
    date_range = input("📅 When do you want to travel? (e.g., Dec 2025, Summer 2026): ").strip()
    duration = input("⏱️  How long is your trip? (e.g., 7 days, 2 weeks): ").strip()
    interests = input("🎯 What are your interests? (e.g., culture, adventure, food, relaxation): ").strip()
    budget = input("💰 What's your budget range? (e.g., $2000-3000, moderate, luxury): ").strip()
    travelers = input("👥 Number of travelers: ").strip()
    
    print("\n✨ Great! Creating your personalized travel plan...\n")
    
    inputs = {
        'origin': origin,
        'destination': destination,
        'date_range': date_range,
        'duration': duration,
        'interests': interests,
        'budget': budget,
        'travelers': travelers,
        'current_year': str(datetime.now().year),
        'topic': f"travel from {origin} to {destination}"
    }
    
    try:
        AiTravelAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "origin": "New York, USA",
        "destination": "Paris, France",
        "date_range": "June 2026",
        "duration": "7 days",
        "interests": "culture, food, history",
        "budget": "$3000-4000",
        "travelers": "2",
        'current_year': str(datetime.now().year),
        "topic": "travel from New York to Paris"
    }
    try:
        AiTravelAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AiTravelAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "origin": "New York, USA",
        "destination": "Paris, France",
        "date_range": "June 2026",
        "duration": "7 days",
        "interests": "culture, food, history",
        "budget": "$3000-4000",
        "travelers": "2",
        "current_year": str(datetime.now().year),
        "topic": "travel from New York to Paris"
    }
    
    try:
        AiTravelAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
