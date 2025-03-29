# Week 3 Program: Ticket Price Calculator

This program calculates the total ticket price for a movie based on the user's age and the showtime. It includes features such as discounts for matinee shows and tax calculations.

## Features
- **Age-based Pricing**: Different ticket prices for children, adults, and seniors.
- **Matinee Discount**: A discount is applied for shows before 5:00 PM.
- **Tax Calculation**: Adds a tax to the final ticket price.

## Files
- `Clark_Ryan_Wk3_Program.py`: Contains the main program logic and unit tests.

## How to Run
1. Ensure you have Python installed on your system.
2. Run the program using the following command:
   ```bash
   python Clark_Ryan_Wk3_Program.py
   ```
3. Follow the prompts to input your age and showtime.

## Testing
The program includes unit tests to validate its functionality. To run the tests, execute:
```bash
python Test_Clark_Ryan_Wk3_Program.py
```
### Code Coverage
To measure test coverage and generate an HTML report:
1. Install the `coverage` package if not already installed:
   ```bash
   pip install coverage
   ```
2. Run the tests with coverage:
   ```bash
   coverage run Test_Clark_Ryan_Wk3_Program.py
   ```
3. Generate an HTML report:
   ```bash
   coverage html
   ```
4. Open the `htmlcov/index.html` file in your browser to view the coverage report.

## Configuration
- **Age Range**: Configurable via `MAX_AGE_RANGE` (default: 0 to 80).
- **Prices**: Configurable via `DEFAULT_PRICES` for children, adults, and seniors.
- **Matinee Discount**: Configurable via `DEFAULT_MATINEE` (default: 15% discount before 5:00 PM).
- **Tax Rate**: Configurable via `DEFAULT_TAX` (default: 8%).

## License
This project is for educational purposes and is not licensed for commercial use.