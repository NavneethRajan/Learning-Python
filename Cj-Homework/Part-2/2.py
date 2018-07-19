list = [1,2,3,4]

def reverselist(list):
    reversedlist = []
    if not list:
        raise Exception("List is none")
    else:
        for i in range(len(list)):
            reversedlist.append(list[((len(list) -1) - (i))])

        print(reversedlist)
            
reverselist(list)
