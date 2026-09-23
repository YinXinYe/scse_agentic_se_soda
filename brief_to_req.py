"""Step 1 (exercise): ask Qwen to turn the human brief into software
requirements in free-form natural language, run it several times, and
observe whether the output is consistent (it is not -- which is why the
Analyst Agent later forces a strict JSON contract).

Produces: robot_requirements.txt
"""

from ollama import chat

BRIEF_PATH = "brief.txt"
OUTPUT_PATH = "robot_requirements.txt"

MODEL = "qwen3:8b"

# Run several times so we can compare the outputs and judge consistency.
NUM_RUNS = 3

PROMPT_TEMPLATE = (
    "You are a requirements engineer.\n"
    "Read the customer's brief below and produce a clear list of software "
    "requirements for the robot navigation system.\n"
    "Write the requirements as a numbered list in plain English.\n\n"
    "BRIEF:\n{brief}\n"
)


def read_brief(path=BRIEF_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def ask_qwen(brief_text):
    response = chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": PROMPT_TEMPLATE.format(brief=brief_text)},
        ],
    )
    return response.message.content


def main():
    brief = read_brief()

    runs = []
    for i in range(1, NUM_RUNS + 1):
        print(f"Run {i}/{NUM_RUNS} ...")
        runs.append(ask_qwen(brief))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for i, text in enumerate(runs, start=1):
            f.write(f"===== RUN {i} =====\n")
            f.write(text.strip() + "\n\n")

    print(f"Saved {NUM_RUNS} runs to {OUTPUT_PATH}")
    print("Open the file and compare the runs: are they consistent? "
          "Could a program consume this output directly?")


if __name__ == "__main__":
    main()
