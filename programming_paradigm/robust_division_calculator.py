def safe_divide(numerator, denominator) :
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
    except ValueError:
        return 'Error: Please enter numeric values only.'
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    except TypeError:
        return 'Error: Please provide two numbers.'
    else:
        return f"The result of the division is {result}"
