# Write a function that takes 3 required parameters and 2 optional parameters

def f(x, y, z, a = 10, b = 20, c = 30):
    """
    Returns (x + y + z) * (a + b + c)
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :param c: int.
    :return: int (sum of x, y, and z) multiplied by (sum of a, b, and c),
    """
    
    return((x + y + z) * (a + b + c))

result = f(1, 2, 3)
print(result)
