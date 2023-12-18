# Two Numbers Challenge

This is a Python project to determine if exactly two out of three integers are positive.

## Description

This project provides a Python function that takes three integers (a, b, and c) as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero) and False otherwise.

## Features

-Determine if exactly two out of three integers are positive
-Simple and straightforward Python function

## Prerequisites

1. Python (version 3.x)
2. Git (optional, for version control)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shazz-Designing/TwoNumbersChallenge.git

2. Navigate to the project directory:

   ```bash
   cd TwoNumbersChallenge

3. Create and activate a virtual environment 

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate   # On Windows

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt


## Usage

1. Import the `check_two_positive` function from the `app` module:

    ```python
    from app import check_two_positive

2. Use the function to check if exactly two out of three integers are positive:

    ```python
    result = check_two_positive(2, 4, -3)
    print(result)  # Output: True


## Testing

Consider writing tests for your code using a testing framework like pytest. Organize your tests in a separate directory (e.g., tests/).

To run tests, use the following command:

    pytest


Contributing

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull reques


License
This project is licensed under the MIT License.
