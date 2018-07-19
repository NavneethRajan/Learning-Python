a = input("Type in a string: ")

def palindrome(x):

    newlist = []

    xlist = list(x)

    for i in range(len(xlist)):
        newlist.append(xlist[(len(xlist) - 1) - (i)])

    print(newlist == list(x))

palindrome(a)
