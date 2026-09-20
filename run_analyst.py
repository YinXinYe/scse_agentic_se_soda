"""Runner: read the brief, run the Analyst Agent, and save the validated
software requirements as artifacts/requirements.json.
"""

import json
import os

from analyst_agent import run_analyst

BRIEF_PATH = "brief.txt"
ARTIFACTS_DIR = "artifacts"
OUTPUT_PATH = os.path.join(ARTIFACTS_DIR, "requirements.json")


def read_brief(path: str = BRIEF_PATH) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    brief_text = read_brief()

    # Call the agent and receive the final validated software requirements.
    requirements = run_analyst(brief_text)

    # Save them as JSON inside the artifacts folder.
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(requirements, f, indent=2)

    print(f"Saved validated requirements to {OUTPUT_PATH}:")
    print(json.dumps(requirements, indent=2))


if __name__ == "__main__":
    main()
