import json
class InvalidCategoryError(Exception):
    pass

APP_NAME = "Budget Tracker"
BUDGET_LIMIT = 500.00
TRACKING_ACTIVE = True

expense_log = []
category_totals = {
    "food" : 0.00,
    "transport" : 0.00,
    "entertainment" : 0.00,
    "misc" : 0.00
}

def add_expense(category, amount, description="No description"):
    expense_dict = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expense_log.append(expense_dict)
    category_totals[category] += amount
    return expense_dict

def get_expenses_by_category(category):
    try:
        filtered_expenses = [c for c in expense_log if c["category"] == category]
    except KeyError:
        raise InvalidCategoryError("Category key not found in expense record")
    return filtered_expenses

def save_expenses(filename):
    with open(filename, "w") as f:
        json.dump(expense_log, f)

def load_expenses(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
if __name__ == "__main__":
    add_expense("food", 630.00)
    add_expense("transport", 720.00, description="Don't be late")
    add_expense("misc", 130.00, description="Insurance has gotten expensive")

    save_expenses("expenses.json")
    loaded = load_expenses("expenses.json")
    for expenses in loaded:
        print(expenses)
    print(get_expenses_by_category("food"))