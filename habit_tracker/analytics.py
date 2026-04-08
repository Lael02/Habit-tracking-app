from datetime import datetime


# Calculate the longest streak for a single habit
def calculate_streak(habit):
    # Convert completion timestamps into date objects and sort them
    dates = sorted(
        [datetime.fromisoformat(d).date() for d in habit.completions]
    )

    # If there are no completions, streak is 0
    if not dates:
        return 0

    streak = 1
    max_streak = 1

    for i in range(1, len(dates)):

        # Determine expected gap based on frequency
        if habit.frequency == "daily":
            expected_gap = 1
        elif habit.frequency == "weekly":
            expected_gap = 7
        else:
            expected_gap = 1  # fallback just in case

        # Check if the current completion follows the expected pattern
        if (dates[i] - dates[i - 1]).days == expected_gap:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            # Reset streak if the pattern breaks
            streak = 1

    return max_streak


# Find the longest streak across all habits
def longest_streak(habits):
    # Apply calculate_streak to each habit and return the maximum
    streaks = list(map(calculate_streak, habits))
    return max(streaks) if streaks else 0