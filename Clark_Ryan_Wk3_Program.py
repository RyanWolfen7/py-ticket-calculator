"""
Description: This program calculates the target heart rate based on the user's age and exercise intensity levels.
Name: Ryan Clark
Date: 03/29/2025
Assignment: Week 3 - Programming Assignment 3
Version: 0.0.1
"""

MAX_AGE_RANGE = (0, 80) 
DEFAULT_PRICES = {
    "child": 10.99,
    "adult": 18.99,
    "senior": 15.99
}
DEFAULT_MATINEE = {
    "time": 1700, # 5pm
    "discount": 0.15 # 15% 
}
DEFAULT_TAX = 0.08 # 8% tax

def get_age(age=None):
    if age is None: age = input("Please enter your age in years: ")
    try: age = int(age) # changes type string to int
    except ValueError: # if unable prints message and callsback self
        print("Age must be a number")
        return get_age()
    if age > MAX_AGE_RANGE[1] or age < MAX_AGE_RANGE[0]: 
        print(f"Invalid age. Please enter a value between {MAX_AGE_RANGE[0]} and {MAX_AGE_RANGE[1]}.")
        return get_age() # if not valid prints message and callsback self
    return age

def get_time(time=None):
    if time is None: time = input("Please enter the show-time in 24-hour format (e.g. 1700 for 5:00 PM): ")
    try: time = int(time) # changes type string to int
    except ValueError: # if unable prints message and callsback self
        print("Time must be a number!")
        return get_time()
    if time > 2400 or time < 0: # checs if number is between 0 and 2400 for 24h time format
        print("Invalid time, must be a number between 0000 and 2400.")
        return get_time() # if not valid prints message and callsback self
    return time

def get_price(age, time):
    price = {
        "base": 0.0,
        "discount": 0.0,
        "tax": DEFAULT_TAX,
        "total": 0.0
    }
    if age <= 12:
        price["base"] = DEFAULT_PRICES["child"]
    elif age >= 60:
        price["base"] = DEFAULT_PRICES["senior"]
    else:
        price['base'] = DEFAULT_PRICES["adult"]

    price['total'] = price['base']
    if time < DEFAULT_MATINEE['time']:
        price["discount"] = price["base"] * DEFAULT_MATINEE["discount"]
        price["total"] = price["total"] - price["discount"]
    
    price['tax'] = price["total"] * DEFAULT_TAX
    price["total"] = price['total'] + price['tax']

    return price

def print_price(base, discount, tax, total):
    print('--------------------------------')
    print(f"Your base ticket price = ${base:.2f}")
    print(f"Discount applied = ${discount:.2f}")
    print(f"Tax = ${tax:.2f}")
    print(f"Your final ticket price = ${total:.2f}")

age = get_age()
time = get_time()
price = get_price(age, time)
print_price(**price)