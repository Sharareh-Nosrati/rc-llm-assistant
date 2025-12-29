# LLM Lead Assistant (Chatbot Demo)

This repository contains a small LLM-based chatbot demo built to support
Sales and Marketing teams with lead review and follow-up.

## What it does
Given structured lead data (JSON), the assistant returns:
- a short lead summary
- lead quality (low / medium / high)
- suggested next best actions
- a draft follow-up message

The LLM is used strictly as an assistant layer, not as a source of truth.

## Why this exists
In many GTM teams, lead qualification and follow-up are manual and inconsistent.
This demo shows how an LLM can be used to:
- reduce manual effort
- standardize lead understanding
- improve response speed

The focus is on clarity, reliability, and practical business use.

## How it works (high level)
1. Lead data is provided as structured JSON
2. The LLM processes only the given input
3. The output is returned in a clear, readable format

## Guardrails
- Uses only provided input data
- Does not invent facts
- Outputs are advisory, not automatic actions

## How to run locally
```bash
pip install -r requirements.txt
cp .env.example .env
# add your OpenAI API key to .env
python -m src.cli_chatbot
