# Python Calculator Project

This project contains a simple Python calculator program with basic arithmetic operations and built-in tests.

## Project Structure

```
python-project/
├── src/
│   └── calculator.py
├── tests/
├── requirements.txt
└── README.md
```

## Features

The calculator supports:
- Addition
- Subtraction
- Multiplication
- Division (with division by zero handling)
- Built-in test cases

## Running the Program Locally

To run the program locally:

```bash
cd python-project
python src/calculator.py
```

This will execute the calculator program which:
1. Runs all tests to verify functionality
2. Prompts for user input to perform calculations

## Tests

The calculator includes built-in tests that verify:
- Basic arithmetic operations
- Edge cases (negative numbers, zeros)
- Error handling (division by zero)

## GitHub Actions Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/python-tests.yml`.

### Workflow Details

The GitHub Actions workflow:
1. Triggers on push to main branch and pull requests
2. Sets up Python environment
3. Installs dependencies from requirements.txt
4. Runs the tests in calculator.py
5. Notifies on success

## Customizing the Project

You can extend this calculator by:
- Adding more mathematical operations
- Implementing a more sophisticated user interface
- Adding more comprehensive test cases
- Integrating with a test framework like pytest
