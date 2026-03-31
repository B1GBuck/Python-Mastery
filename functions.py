def describe_developer(name, language, exp_years):
    return f"{name} is a developer who programs in {language} and has {exp_years} years of experience."

developer_1 = describe_developer("Dre", "Python", 10)
print(developer_1)

developer_2 = describe_developer("Alex", "JavaScript", 5)
print(developer_2)


def calculate_total(price, tax_rate=0.08):
    return price * (1 + tax_rate)

print(f"{calculate_total(25.99):.2f}")

total = calculate_total(25.99, tax_rate=0.22)
print(f"{total:.2f}")


def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(3, 4, 5, 5, 6, 7, 8, 9, 1, 2))
print(add_all(6, 7, 8))
print(add_all(9, 1, 2, 9, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9))

def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
build_profile(name="Dre", language="Python", experience=10, location="NYC")

multiply = lambda x, y: x * y
print(multiply(5, 12))

print(multiply(100, 67))

print(multiply(8, 9))