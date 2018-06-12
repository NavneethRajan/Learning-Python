# Write a function that takes a number as an input and returns that number squared

def square(x):
    """
    Returns x ** 2
    :param x: int.
    :return: int x to the power of 2.
    """
    
    return(x ** 2)

a = input("Type in a number: ")

a = int(a)

print(square(a))
       
