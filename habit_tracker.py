import json
class InvalidHabitError(Exception):
    pass

APP_NAME = "Habit Tracker"
GOAL_STREAK = 30
TRACKER_ACTIVE = True

habit_log = []
habit_streaks = {
    "exercise": 0,
    "reading": 0,
    "coding": 0,
    "hydration": 0
}

def add_habit(habit, completed, note="No Note"):
    habit_dict = {
        "habit": habit,
        "completed": completed,
        "note": note
    }
    habit_log.append(habit_dict)
    if completed:
        habit_streaks[habit] += 1
    return habit_dict

def get_completed_habits(habit):
    try:
        filtered_entries = [e for e in habit_log if e["habit"] == habit and e["completed"]]
    except KeyError:
        raise InvalidHabitError("Habit key not in log entry")
    return filtered_entries

def save_habits(filename):
    with open(filename, "w") as f:
        json.dump(habit_log, f)
    
def load_habits(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
        
if __name__ == "__main__":
    add_habit("exercise", True)
    add_habit("coding", False, note="Still practicing this coding stuff")
    add_habit("reading", True, note="This current book is great")

    save_habits("habits.json")

    loaded = load_habits("habits.json")

    for habits in loaded:
        print(habits)
            
    print(get_completed_habits("coding"))