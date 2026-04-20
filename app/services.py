import json
import random
import os


FACTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "facts.json")


def get_random_fact() -> str:
    """
    Load a random fact from the curated facts.json file.
    Falls back to a hardcoded fact if the file is missing or malformed.
    """
    try:
        with open(FACTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        facts = data.get("facts", [])
        if facts:
            return random.choice(facts)["fact"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass

    return "A neutron star is so dense that a teaspoon of its material would weigh 10 million tons on Earth."


def get_random_fact_by_category(category: str) -> str:
    """
    Optional: pull a fact from a specific category.
    Falls back to fully random if category not found.
    """
    try:
        with open(FACTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        filtered = [f for f in data.get("facts", []) if f.get("category") == category]
        if filtered:
            return random.choice(filtered)["fact"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass

    return get_random_fact()