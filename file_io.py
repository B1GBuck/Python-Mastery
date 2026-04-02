def write_notes(filename, strings):
    with open(filename, "w") as f:
        for string in strings:
            f.write(string + "\n")
filename = "study_notes.txt"
strings = ["Python uses open() to work with files", "f.write() does not automatically add a newline", 
           "CSV is one of the most common data formats to work with in Python", "JSON is the standard format for APIs and config files", 
           "Python comes with a huge standard library to work with files and data formats"]
write_notes(filename, strings)

def read_notes(filename):
    with open(filename) as f:
        for index, line in enumerate(f, 1):
            print(index, line.strip())
read_notes(filename)

import csv

def write_csv(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["module", "topic", "status"])
        writer.writerow([1.1, "Python Env and Tools", "Completed"])
        writer.writerow([1.2, "Data Types", "Completed"])
        writer.writerow([1.3, "Control Flow Mastery", "Completed"])
        writer.writerow([1.4, "Loops and Iteration", "In Progress"])
        writer.writerow([1.5, "Functions", "In Progress"])

def read_csv(filename):
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

write_csv("modules.csv")
read_csv("modules.csv")

import json

def save_profile(dict_, filename):
    with open(filename, "w") as f:
        json.dump(dict_, f, indent=4)

def load_profile(filename):
    with open(filename, "r") as f:
        return json.load(f)

dev_profile = {"name": "Dre", "age": 32, "language": "Python", "state": "Texas", "experience": 4}
save_profile(dev_profile, "profile.json")
print(load_profile("profile.json"))

import utils

price = 2599.99
print(utils.calculate_tax(price, tax_rate=0.0825)) #The result of this should be the total after taxes

number = 2957.07654
print(utils.format_currency(number)) #The result of this should be a number formatted to 2 decimal places

score = 85
print(utils.is_valid_score(score)) #This should print True or False if the score is in the range of (0 - 100)

def save_sessions(filename, session_log):
    with open(filename, "w") as f:
        json.dump(session_log, f)

def load_sessions(filename):
    with open(filename, "r") as f:
        if f in filename:
            return json.load(f)
        else:
            return []