study_topics = ["Data Types", "Variables", "Operators", "Ternary Operators", "Control Flow", "Match Case"]
for index, topic in enumerate(study_topics):
    print(f"{index + 1}. {topic}")

for number in range(1, 21):
    if number % 2 == 0:
        print(number)
    
start = 100
while start >= 0:
    print(start)
    start -= 10

module_names = ["for loops", "while loops", "enumerate", "range", "1.4"]

for mod in module_names:
    if mod == "1.4":
        print("Found it!")
        break

syllabus_phases = ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5"]
completion_weeks = ["Week 4", "Week 9", "Week 14", "Week 19", "Week 24"]

for phase, completion in zip(syllabus_phases, completion_weeks):
    print(f"{phase}: {completion}")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)