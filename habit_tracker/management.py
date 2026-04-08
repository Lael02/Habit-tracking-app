from habits import Habit
from storage import load_habits, save_habits


# Create a new habit and save it
def create_habit(name, frequency):
    habits = load_habits()
    habits.append(Habit(name, frequency))
    save_habits(habits)


# Mark a habit as completed by name
def complete_habit(name):
    habits = load_habits()
    for habit in habits:
        if habit.name == name:
            habit.complete()  # add current timestamp
            break  # stop after finding the habit
    save_habits(habits)


# Delete a habit by name
def delete_habit(name):
    habits = load_habits()
    # keep only habits that don't match the given name
    habits = [h for h in habits if h.name != name]
    save_habits(habits)


# Return all saved habits
def get_all_habits():
    return load_habits()