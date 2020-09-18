import json
import os

DATA_PATH = os.getenv("DATA_PATH") or os.path.dirname(os.path.abspath(__file__)) + "/../data/"
GOALS_PATH = DATA_PATH + "goals.json"
CURRENT_GOAL_PATH = DATA_PATH + "current_goal.txt"

with open(GOALS_PATH, "w+") as f:
    try:
        x = json.load(f)
        if not x:
            f.seek(0, 0)
            f.truncate(0)
            json.dump([], f, indent=4)
    except FileNotFoundError:
        f.seek(0, 0)
        f.truncate(0)
        json.dump([], f, indent=4)
    except json.JSONDecodeError:
        f.seek(0, 0)
        f.truncate(0)
        json.dump([], f, indent=4)


def get_goals() -> list:
    with open(GOALS_PATH, "r") as f:
        return json.load(f)


def get_goal(id_: int) -> dict:
    x = list(filter(lambda x: x["id"] == id_, get_goals()))
    return x[0] if x else {}


def get_current_goal() -> str:
    with open(CURRENT_GOAL_PATH, "r") as f:
        return f.read()


def set_goals(goals: list) -> bool:
    with open(GOALS_PATH, "w") as f:
        json.dump(goals, f, indent=4)
    with open(CURRENT_GOAL_PATH, "w") as f:
        goal = goals[0]["name"] if goals else "None"
        f.write(goal)
    return True


def add_goal(goal: dict) -> list:
    goals = get_goals()
    goals.append(goal)
    set_goals(goals)
    return goals


def remove_goal(goal: dict) -> list:
    goals = get_goals()
    try:
        goals.remove(goal)
        set_goals(goals)
        return goals
    except ValueError:
        return goals
