def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Division operation completed.")

# Test cases
print("Case 1:", divide_numbers(10, 2))
# print("\nCase 2:", divide_numbers(10, 0))
# print("\nCase 3:", divide_numbers("10", "2"))