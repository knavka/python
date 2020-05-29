from random import randrange

#Создание списка целых чисел в заданных пределах, заданной длины
def createlist(length, maxel):
    list = []
    for i in range(0, length):
        list.append(randrange(maxel))
    return list

#Получение целого числа от пользователя с проверкой типа
def getInt(askstr):
    # Проверка на целое число
    def isInt(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
    print(askstr)
    uservalue = input()
    if (not isInt(uservalue)):
        print("значение должно быть целым числом")
        return getInt(askstr)
    else:
        return int(uservalue)

#Диалог с пользователем по созданию списка целых чисел в заданных пределах, заданной длины
def consoleDialogCreateList():
    print(createlist(getInt("Длина списка:"), getInt("Максимальное значение:")))


consoleDialogCreateList()