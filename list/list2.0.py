from random import randrange

#Создание списка целых чисел в заданных пределах, заданной длины
def createlist(length, maxel):
    list = []
    for i in range(0, length):
        list.append(randrange(maxel))
    return list

#Проверка на целое число
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


#Получение целого числа от пользователя с проверкой типа
def getUserInt(askstr):
    print(askstr)
    uservalue = input()
    if (not isInt(uservalue)):
        print("Значение должно быть целым числом\n")
        return getUserInt(askstr)
    else:
        return int(uservalue)

#Диалог с пользователем по созданию списка целых чисел в заданных пределах, заданной длины
def consoleDialogCreateList():
    print(createlist(getUserInt("Длина списка:"), getUserInt("Максимальное значение:")))


consoleDialogCreateList()