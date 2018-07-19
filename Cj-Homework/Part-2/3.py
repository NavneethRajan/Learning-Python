def listfind(list , x):
    if not list:
        raise Exception("List is none")
    elif x in list:
        print (True)
    else:
        print(False)


listfind([1,2,3,4,5] , 9)
