topics_studied = ["Python Env and Tools", "Data Types", "Variables", "Control Flow", "Loops and Iteration", "Functions"]

topics_studied.append("Error Handling")
print(topics_studied)

topics_studied.insert(0, "Collections")
print(topics_studied)

topics_studied.remove("Data Types")
print(topics_studied)

topics_studied.pop()
print(topics_studied)

dev_profile = {
    "name": "Dre",
    "age": 32,
    "language": "Python",
    "state": "Texas",
    "experience": 4
}

dev_profile["gender"] = "M"
print(dev_profile)

dev_profile["state"] = "New York"
print(dev_profile)

dev_profile.pop("gender")
print(dev_profile)

print(dev_profile.get("name"))

non_changing = ("Config. Settings", "Date and Time", "Employee Data")
#The values I chose for this tuple represent information that if changed could cause issues in a program

def trying_to_change(non_changing):
    try:
        non_changing[1] = "DB Information"
    except TypeError:
        print("This is a Tuple and cannot be changed.")
print(non_changing)

trying_to_change(non_changing)

developer = {"App Builds", "Feature Updates", "User Facing Prod."}
engineer = {"Structure Application", "Architecture", "High Level Principles"}

print(f"Intersection: {developer & engineer}") #This will print the intersection of the two sets, which is an empty set since there are no common elements between the developer and engineer sets.
print(f"Union: {developer | engineer}") #This will print the union of the two sets, which includes all unique elements from both sets. The output will be: {'App Builds', 'Feature Updates', 'User Facing Prod.', 'Structure Application', 'Architecture', 'High Level Principles'}
print(f"Difference: {developer - engineer}") #This will print the difference between the developer and engineer sets, which includes elements that are in the developer set but not in the engineer set. The output will be: {'App Builds', 'Feature Updates', 'User Facing Prod.'}

squared_list = [num * num for num in range(1, 11)]
print(squared_list)

keys_to_cube = [1, 2, 3, 4, 5]

cubed_dictionary = {key : key ** 3 for key in keys_to_cube}
print(cubed_dictionary)