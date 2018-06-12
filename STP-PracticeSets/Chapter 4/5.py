# Write a function that converts a string to a float and returns the result.
# Use exception handling to catch the exception that could occur.

def float_convert(x):
    """
    Converts string to float
    :param x: str.
    :return: String converted to float
    try:
        return(float(x))
    except ValueError:
        print("That input is invalid.")

a = input("Type a number: ")

b = float_convert(a)

print(b)