from random import randrange

def createlist(length, maxel):
    list=[]
    for i in range(0,length):
        list.append(randrange(maxel))
    return list

def consoleDialogCreateList():
    print("Длина списка:")
    length = int(input())
    print("Максимальное значение:")
    maxel = int(input())

    print(createlist(length, maxel))

consoleDialogCreateList()
