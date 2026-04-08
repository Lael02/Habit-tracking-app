from datetime import datetime

class Habit:
    # Initialize a habit with name, frequency, and optional data
    def __init__(self, name, frequency, created_at=None, completions=None):
        self.name = name
        self.frequency = frequency  # can be "daily" or "weekly"
        # If no creation date is given, use the current time
        self.created_at = created_at or datetime.now().isoformat()
        # Store all completion timestamps (empty list if none is provided)
        self.completions = completions or []

    # Mark the habit as completed by adding the current timestamp
    def complete(self):
        self.completions.append(datetime.now().isoformat())
    
    # Convert the habit object into a dictionary (for saving to JSON)
    def to_dict(self):
        return {
            "name": self.name,
            "frequency": self.frequency,
            "created_at": self.created_at,
            "completions": self.completions,
        }

    # Create a Habit object from a dictionary (when loading from JSON)
    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["frequency"],
            data["created_at"],
            data["completions"],
        )