# Calculator Project

A Python calculator program with basic arithmetic, exponent, logarithmic, and trigonometric functions.

## Features

- **Basic arithmetic**: addition, subtraction, multiplication, division
- **Exponentiation**: power function with arbitrary exponents
- **Logarithms**: logarithm with configurable base (defaults to natural log)
- **Trigonometric functions**: sine, cosine, tangent (angles in radians)
- Input validation (e.g., division by zero, invalid log values)

## Project Structure

```
.
├── calculator.py    # Main calculator module
├── test_calculator.py  # Test suite
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (No external dependencies are required beyond Python's standard library `math` module.)

## Usage

```python
from calculator import add, subtract, multiply, divide, exponent, logarithmic, sine, cosine, tangent

# Basic arithmetic
result = add(5, 3)        # 8
result = subtract(5, 3)   # 2
result = multiply(5, 3)   # 15
result = divide(6, 3)     # 2.0

# Exponentiation
result = exponent(2, 3)   # 8

# Logarithms
result = logarithmic(100, 10)  # 2 (log base 10)
result = logarithmic(1)        # 0 (natural log of 1)

# Trigonometry (angles in radians)
result = sine(0)          # 0
result = cosine(0)        # 1
result = tangent(0)       # 0
```

Run the demo included in `calculator.py`:
```bash
python calculator.py
```

## Running Tests

```bash
python -m unittest test_calculator.py -v
```

All 7 tests cover:
- Addition, subtraction, multiplication
- Division with zero-division error handling
- Exponentiation including fractional powers
- Logarithm with base validation and positive value requirement
- Trigonometric functions at key angles (0, π/2)