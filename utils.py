def calculate_tax(price, tax_rate=0.0825):
    return price * (1 + tax_rate)

def format_currency(number):
    return f"${number:.2f}"

def is_valid_score(score):
    return True if 0 <= score <= 100 else False

if __name__ == "__main__":
    price = 3599.99
    print(calculate_tax(price, tax_rate=0.0825)) #This is the total after tax

    number = 295647.09876
    print(format_currency(number)) #This is the number formatted to 2 decimal places

    score = 85
    print(is_valid_score(score)) #This should print True or False if the score is in the range of (0 - 100)
    score = 105
    print(is_valid_score(score))
    score = -5
    print(is_valid_score(score))