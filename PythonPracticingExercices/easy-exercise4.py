def checkNumberinList(num, l):
    if num in l:
        return True
    return False


l = [1, 2, 3, 4, 5]
print(checkNumberinList(5, l))
print(checkNumberinList(0, l))
print(checkNumberinList(20, l))
print(checkNumberinList(3, l))
