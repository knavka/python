#"Взращивание" а до b
def plusWhile (a,b,step=1):
    while(a<b):
        print(str(a)+" Пока что нет")
        a=a+step
    print("Дождались! "+str(a))

#Получение целого числа от пользователя с проверкой типа
def getFloat(askstr):
    # Проверка на число
    def isFloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    print(askstr)
    uservalue = input()
    if (not isFloat(uservalue)):
        print("try number")
        return getFloat(askstr)
    else:
        return float(uservalue)

#Запуск функции с вводом параметров пользователем
plusWhile(getFloat("a:"), getFloat("b:"), getFloat("step:"))


