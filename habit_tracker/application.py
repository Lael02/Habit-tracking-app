from management import (
    create_habit,
    complete_habit,
    delete_habit,
    get_all_habits,
)
from analytics import longest_streak


# Main loop of the application (CLI menu)
def main():
    while True:
        print("\nHabit Tracker")
        print("1. Create Habit")
        print("2. Complete Habit")
        print("3. Delete Habit")
        print("4. List Habits")
        print("5. Show Longest Streak")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Habit name: ")
            freq = input("Frequency (daily/weekly): ")
            create_habit(name, freq)
            print("Habit created!")

        elif choice == "2":
            name = input("Habit to complete: ")
            complete_habit(name)
            print("Habit marked as completed!")

        elif choice == "3":
            name = input("Habit to delete: ")
            delete_habit(name)
            print("Habit deleted!")

        elif choice == "4":
            habits = get_all_habits()
            # Display all habits with their frequency
            for h in habits:
                print(f"- {h.name} ({h.frequency})")

        elif choice == "5":
            habits = get_all_habits()
            # Show the longest streak across all habits
            print("Longest streak:", longest_streak(habits))

        elif choice == "6":
            # Exit the program
            break


if __name__ == "__main__":
    main()