import json
import os
from habits import Habit

FILE_NAME = "data.json"


# Load habits from the JSON file
def load_habits():
    # If the file doesn't exist yet, just return an empty list
    if not os.path.exists(FILE_NAME):
        return []

    # Open the file and load the data
    with open(FILE_NAME, "r") as f:
        data = json.load(f)
        # Convert each dictionary into a Habit object
        return [Habit.from_dict(item) for item in data]


# Save habits to the JSON file
def save_habits(habits):
    # Convert Habit objects into dictionaries and write them to the file
    with open(FILE_NAME, "w") as f:
        json.dump([h.to_dict() for h in habits], f, indent=4)