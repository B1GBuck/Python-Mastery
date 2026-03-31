def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    return result
print(divide(350, 50))
print(divide(46, 0))

def convert_to_int(value):
    try:
        result = int(value)
    except ValueError:
        return "This is not valid value."
    except TypeError:
        return "This is not an integer. Wrong type."
    return result

print(convert_to_int("100"))
print(convert_to_int("Hello"))
print(convert_to_int(None))

def read_config(my_dict, value):
    try:
        my_dict[value]
    except KeyError:
        print("This key does not exist in the dictionary.")
    else:
        print("This was a successful dictionary lookup.")
    finally:
         print("Config read attempt complete.")

my_dict = {"name": "Dre", "age": 32, "language": "Python"}
read_config(my_dict, "name")
read_config(my_dict, "Java")

class InvalidScoreError(Exception):
    pass

def set_score(score):
    if score < 0 or score > 100:
            raise InvalidScoreError(f"{score} is not a valid score.")
    return score
try:
    print(set_score(65))
except InvalidScoreError as e:
    print(e)
    
try:
    print(set_score(110))
except InvalidScoreError as e:
    print(e)
    
try:
    print(set_score(-5))
except InvalidScoreError as e:
    print(e)