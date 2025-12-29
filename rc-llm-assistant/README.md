# Restaurants Club - LLM Lead Assistant (Demo)

This is a small demo chatbot-style assistant for GTM teams.

## What it does
Given structured lead data (JSON), it produces:
- a short summary
- lead quality (low/medium/high)
- next best action steps
- a short follow-up message draft

It uses an LLM as an assistant layer (not a source of truth) and outputs structured JSON.

## Setup
1) Create a virtual environment (optional)
2) Install dependencies:
   pip install -r requirements.txt

3) Create .env from .env.example:
   OPENAI_API_KEY=...
   OPENAI_MODEL=gpt-4o-mini

## Run
python -m src.main

## Output
Results are saved under /outputs as a JSON file.



## CLI Chatbot Mode (Interactive)
Run:
python -m src.cli_chatbot

Commands inside CLI:
- sample1 : load a sample lead
- sample2 : load another sample lead
- exit    : quit
You can also paste a JSON object representing a lead.
