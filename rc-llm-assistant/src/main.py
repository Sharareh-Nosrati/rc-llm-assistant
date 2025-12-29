#%%
import json
from pathlib import Path
from datetime import datetime

from .llm_client import generate_lead_assistant_output

DATA_PATH = Path("data/sample_leads.json")
OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)


def main():
    leads = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    results = []
    for lead in leads:
        out = generate_lead_assistant_output(lead)
        results.append({
            "lead_id": lead.get("lead_id"),
            "input": lead,
            "assistant_output": out
        })

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = OUT_DIR / f"lead_assistant_results_{ts}.json"
    out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Done. Results saved to: {out_file}")

if __name__ == "__main__":
    main()



# %%
