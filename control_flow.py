hour = 22
if hour > 0 and hour <= 11:
    print("Morning")

elif hour > 11 and hour <= 15:
    print("Afternoon")

elif hour > 15 and hour <= 19:
    print("Evening")

else:
    print("Night")

has_venv = True
python_version = False

if has_venv and python_version:
    print("Dev enviornment is ready to go!")
else:
    print("Something is not quite right with your Dev enviornment setup.")

greeting = "Hello early riser" if hour < 12 else "You woke up later than most people"
print(greeting)

day = "Sunday"

match day:
    case"Monday":
        print("Today is Monday and the topic to study is Ternary Operators")
    case "Wednesday":
        print("Today is Wednesday and the topic to study is Control Flow")
    case "Friday":
        print("Today is Friday and the topic to study is Match Case")
    case "Sunday":
        print("Today is Sunday and it is the beginnig of the week, so we will review all the topics covered this week.")
    case _:
        print("Today is quiz and exam days to review all the topics discussed so far this week.")