# Write a program with two functions.
# The first function should take an integer as a parameter and return the result of the integer divided by 2.
# The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
# Call the first function, save the result as a variable, and pass it as a parameter to the second function.

def div(x):
    """
    Returns x / 2
    :param x: int.
    :return: int x divided by 2
    """

    return(x / 2)

def multi(x):
    """
    Returns x multiplied by 4
    :param x: int.
    :return: int x multiplied by 4
    """
    
    return(x * 4)

a = div(8)

b = multi(a)

print(b)
