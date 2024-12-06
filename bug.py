def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /: 'int' and 'str'")
        return None

# This is the line that may produce an uncommon error in Python
# This is because a TypeError may occur at runtime if type of inputs is not checked correctly
result = function_with_uncommon_error(10, "hello")
print(result)