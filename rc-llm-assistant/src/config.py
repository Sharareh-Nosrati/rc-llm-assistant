#%%

import os
from dotenv import load_dotenv #reading .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY. Create a .env file from .env.example.")