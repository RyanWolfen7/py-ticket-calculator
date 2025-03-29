import unittest
from io import StringIO
import sys
from unittest.mock import patch

MAX_AGE_RANGE = (0, 80)
DEFAULT_PRICES = {"child": 10.99, "adult": 18.99, "senior": 15.99}
DEFAULT_MATINEE = {"time": 1700, "discount": 0.15}
DEFAULT_TAX = 0.08

def get_age(age=None):
    if age is None: age = input("Please enter your age in years: ")
    try: age = int(age)
    except ValueError:
        print("Age must be a number")
        return get_age()
    if age > MAX_AGE_RANGE[1] or age < MAX_AGE_RANGE[0]:
        print(f"Invalid age. Please enter a value between {MAX_AGE_RANGE[0]} and {MAX_AGE_RANGE[1]}.")
        return get_age()
    return age

def get_time(time=None):
    if time is None: time = input("Please enter the show-time in 24-hour format (e.g. 1700 for 5:00 PM): ")
    try: time = int(time)
    except ValueError:
        print("Time must be a number!")
        return get_time()
    if time > 2400 or time < 0:
        print("Invalid time, must be a number between 0000 and 2400.")
        return get_time()
    return time

def get_price(age, time):
    price = {"base": 0.0, "discount": 0.0, "tax": DEFAULT_TAX, "total": 0.0}
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

class TestTicketCalculator(unittest.TestCase):
    def test_get_age_valid(self):
        with patch('builtins.input', return_value="25"):
            self.assertEqual(get_age(), 25)
    
    def test_get_age_invalid_string(self):
        with patch('builtins.input', side_effect=["abc", "30"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                age = get_age()
                self.assertEqual(age, 30)
                self.assertIn("Age must be a number", fake_out.getvalue())
    
    def test_get_age_out_of_range(self):
        with patch('builtins.input', side_effect=["90", "40"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                age = get_age()
                self.assertEqual(age, 40)
                self.assertIn("Invalid age", fake_out.getvalue())
    
    def test_get_time_valid(self):
        with patch('builtins.input', return_value="1400"):
            self.assertEqual(get_time(), 1400)
    
    def test_get_time_invalid(self):
        with patch('builtins.input', side_effect=["xyz", "1600"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                time = get_time()
                self.assertEqual(time, 1600)
                self.assertIn("Time must be a number!", fake_out.getvalue())
    
    def test_get_time_out_of_range(self):
        with patch('builtins.input', side_effect=["2500", "1200"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                time = get_time()
                self.assertEqual(time, 1200)
                self.assertIn("Invalid time", fake_out.getvalue())
    
    def test_get_price_child_matinee(self):
        # Test child price with matinee discount (before 5pm)
        price = get_price(10, 1400)
        self.assertEqual(price["base"], 10.99)
        self.assertAlmostEqual(price["discount"], 1.6485, places=4)
        self.assertAlmostEqual(price["tax"], 0.74732, places=4)  # Corrected
        self.assertAlmostEqual(price["total"], 10.08882, places=4)  # Corrected
    
    def test_get_price_adult_no_discount(self):
        # Test adult price after matinee (no discount)
        price = get_price(30, 1800)
        self.assertEqual(price["base"], 18.99)
        self.assertEqual(price["discount"], 0.0)
        self.assertAlmostEqual(price["tax"], 1.5192, places=4)
        self.assertAlmostEqual(price["total"], 20.5092, places=4)
    
    def test_get_price_senior_matinee(self):
        # Test senior price with matinee discount
        price = get_price(65, 1600)
        self.assertEqual(price["base"], 15.99)
        self.assertAlmostEqual(price["discount"], 2.3985, places=4)
        self.assertAlmostEqual(price["tax"], 1.08732, places=4)  # Corrected
        self.assertAlmostEqual(price["total"], 14.67882, places=4)  # Corrected

if __name__ == "__main__":
    unittest.main()