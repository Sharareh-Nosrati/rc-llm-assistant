import json
from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL
from .prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_lead_assistant_output(lead: dict) -> dict:
    lead_json = json.dumps(lead, ensure_ascii=False)
    user_prompt = USER_PROMPT_TEMPLATE.format(lead_json=lead_json)

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
    )

    content = resp.choices[0].message.content.strip()

    # Parse JSON safely
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        # If model output is not valid JSON, return a controlled error payload
        return {
            "error": "Model did not return valid JSON",
            "raw_output": content,
            "exception": str(e)
        }
