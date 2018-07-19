def largestvalue(list):
    if not list:
        raise Exception("List is None")
    else:
        largest = list[0]
        for a in list:
            if a > largest:
                largest = a
        return largest

print(largestvalue([1,2,3,4,5,99,80,23,12,0,-5]))
