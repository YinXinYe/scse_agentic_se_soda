# SCSE 26 — Project: Requirements Engineering

Group: **Soda**

Turn a human-language robot-navigation brief into explicit, machine-readable
software requirements using an **Analyst Agent** backed by Qwen.

## How it works

1. `brief_to_req.py` — first exercise: asks Qwen for free-form requirements and
   runs several times to show that the output is *not* consistent.
2. `analyst_agent.py` — the Analyst Agent:
   - `run_analyst(brief_text)` sends a strict system prompt to Qwen, converts
     the returned JSON into Python data, validates it, and returns the
     validated requirements.
   - `validate_requirements(data)` enforces the JSON contract (exact keys,
     correct types, no missing/extra keys).
3. `run_analyst.py` — reads `brief.txt`, calls the agent, and saves the result
   to `artifacts/requirements.json`.

## Requirements JSON contract

```json
{
  "goal": "string",
  "allowed_actions": ["FORWARD", "LEFT", "RIGHT", "STOP"],
  "safe_stop": true,
  "avoid_obstacles": true
}
```

## Running

Requires an Ollama server with the `qwen3:8b` model:

```bash
python brief_to_req.py     # -> robot_requirements.txt
python run_analyst.py      # -> artifacts/requirements.json
```
