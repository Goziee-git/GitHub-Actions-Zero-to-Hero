def get_integer_input(prompt):
    """Get integer input from user with validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result. Returns string if division by zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    print("Simple Calculator Program")
    print("-------------------------")
    
    # Get user inputs
    A = get_integer_input("Enter the first number (A): ")
    B = get_integer_input("Enter the second number (B): ")
    
    # Perform operations
    addition = add(A, B)
    subtraction = subtract(A, B)
    multiplication = multiply(A, B)
    division = divide(A, B)
    
    # Display results
    print("\nResults:")
    print(f"A = {A}, B = {B}")
    print(f"Addition (A + B): {addition}")
    print(f"Subtraction (A - B): {subtraction}")
    print(f"Multiplication (A * B): {multiplication}")
    print(f"Division (A / B): {division}")

def run_tests():
    """Run test cases for calculator functions."""
    print("\nRunning test cases...")
    
    # Test addition
    assert add(5, 3) == 8, "Addition test failed: 5 + 3 should equal 8"
    assert add(-5, 3) == -2, "Addition test failed with negative number"
    assert add(0, 0) == 0, "Addition test failed with zeros"
    
    # Test subtraction
    assert subtract(5, 3) == 2, "Subtraction test failed: 5 - 3 should equal 2"
    assert subtract(3, 5) == -2, "Subtraction test failed: 3 - 5 should equal -2"
    assert subtract(0, 0) == 0, "Subtraction test failed with zeros"
    
    # Test multiplication
    assert multiply(5, 3) == 15, "Multiplication test failed: 5 * 3 should equal 15"
    assert multiply(-5, 3) == -15, "Multiplication test failed with negative number"
    assert multiply(5, 0) == 0, "Multiplication test failed with zero"
    
    # Test division
    assert divide(6, 3) == 2, "Division test failed: 6 / 3 should equal 2"
    assert divide(5, 2) == 2.5, "Division test failed: 5 / 2 should equal 2.5"
    assert divide(0, 5) == 0, "Division test failed: 0 / 5 should equal 0"
    assert divide(5, 0) == "Cannot divide by zero", "Division by zero test failed"
    
    print("All tests passed successfully!")
    return True

if __name__ == "__main__":
    # Run tests first
    tests_passed = run_tests()
    
    if tests_passed:
        # If tests pass, run the main program
        main()
