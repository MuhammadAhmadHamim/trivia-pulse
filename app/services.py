import requests
import json


FACTS_API_URL = "https://api.api-ninjas.com/v1/facts"
FALLBACK_FACTS = [
    "Honey never spoils. Archaeologists have found 3000-year-old honey in Egyptian tombs that was still edible.",
    "A group of flamingos is called a 'flamboyance'.",
    "The shortest war in history lasted 38 to 45 minutes — between Britain and Zanzibar in 1896.",
    "Octopuses have three hearts and blue blood.",
    "The Eiffel Tower can grow by more than 6 inches in summer due to thermal expansion.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries are not.",
]


def get_random_fact() -> str:
    """
    Fetch a random fact from the uselessfacts API.
    Falls back to a local fact if the request fails.
    """
    try:
        response = requests.get(FACTS_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        fact = data.get("text", "").strip()
        if fact:
            return fact
    except (requests.RequestException, json.JSONDecodeError, KeyError):
        pass

    import random
    return random.choice(FALLBACK_FACTS)