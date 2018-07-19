def fibbonacci():
    newlist = []

    for i in range (100):
        try:
            a = newlist[i-1]
        except IndexError:
            a = 1
        try:
            b = newlist[i-2]
        except IndexError:
            b = 0
            
        newlist.append(a + b)

    print(newlist)
