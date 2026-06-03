import json
import os

MEMORY_FILE = "memory.json"

def save_memory(topic, report):

    memory = {}

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    memory[topic] = report

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)