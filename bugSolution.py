def function_with_uncommon_error(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a / b
            return result
        else:
            print("Error: Unsupported operand type(s) for /: 'int' and 'str'")
            return None
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

result = function_with_uncommon_error(10, 2)
print(result)

result = function_with_uncommon_error(10, "hello")
print(result)