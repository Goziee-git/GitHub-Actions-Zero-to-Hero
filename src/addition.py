def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


# Simple test cases
def test_add_numbers():
    # Test case 1: Regular integers
    assert add_numbers(5, 3) == 8
    
    # Test case 2: Negative numbers
    assert add_numbers(-5, 3) == -2
    assert add_numbers(5, -3) == 2
    assert add_numbers(-5, -3) == -8
    
    # Test case 3: Zero
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 5) == 5
    
    # Test case 4: Floating point numbers
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(-2.5, 3.5) == 1.0
    
    print("All tests passed!")


if __name__ == "__main__":
    # Example usage
    a = 10
    b = 20
    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is: {result}")
    
    # Run tests
    test_add_numbers()
