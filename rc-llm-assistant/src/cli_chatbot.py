import json
from typing import Dict, Any

from .llm_client import generate_lead_assistant_output

WELCOME = """
Restaurants Club - LLM Lead Assistant (CLI Demo)
Type lead data as JSON, or type:
- sample1  -> loads a sample lead
- sample2  -> loads a second sample lead
- exit     -> quit
"""

SAMPLE_1 = {
    "lead_id": "L-1001",
    "name": "Mario Rossi",
    "restaurant_name": "Trattoria Milano",
    "restaurant_type": "Italian",
    "city": "Milan",
    "source": "meta",
    "utm_campaign": "winter_offer_2025",
    "actions": ["menu_viewed", "reservation_started"],
    "notes": "Interested but did not complete reservation"
}

SAMPLE_2 = {
    "lead_id": "L-1002",
    "name": "Giulia Bianchi",
    "restaurant_name": "Neon Ramen",
    "restaurant_type": "Japanese",
    "city": "Pisa",
    "source": "google",
    "utm_campaign": "search_brand_2025",
    "actions": ["menu_viewed", "reservation_completed", "payment_completed"],
    "notes": "Converted quickly, high intent"
}


def pretty_print(output: Dict[str, Any]) -> None:
    """Print in a readable way for demo purposes."""
    if "error" in output:
        print("\n[ERROR] Model output issue:")
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    print("\n--- Assistant Output ---")
    print(f"Summary: {output.get('summary', '')}")
    print(f"Lead quality: {output.get('lead_quality', '')}")

    nba = output.get("next_best_action", [])
    if isinstance(nba, list):
        print("Next best actions:")
        for i, item in enumerate(nba, start=1):
            print(f"  {i}. {item}")
    else:
        print(f"Next best actions: {nba}")

    print("\nFollow-up message draft:")
    print(output.get("follow_up_message", ""))
    print("------------------------\n")


def run():
    print(WELCOME)

    while True:
        user_in = input("lead-json> ").strip()

        if user_in.lower() in {"exit", "quit"}:
            print("Bye.")
            break

        if user_in.lower() == "sample1":
            lead = SAMPLE_1
        elif user_in.lower() == "sample2":
            lead = SAMPLE_2
        else:
            try:
                lead = json.loads(user_in)
                if not isinstance(lead, dict):
                    print("Please provide a JSON object (dictionary).")
                    continue
            except json.JSONDecodeError:
                print("Invalid JSON. Tip: type 'sample1' to try a sample.")
                continue

        output = generate_lead_assistant_output(lead)
        pretty_print(output)


if __name__ == "__main__":
    run()
