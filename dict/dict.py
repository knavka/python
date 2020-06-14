#Функция производит слияние любого числа словарей
    #при наличии дублирующих ключей - берется значение из словаря, следующего в списке аргументов функции правее
def mergeDicts (*dicts):
    resultdict={}
    for dict in dicts:
        resultdict.update(dict)
    return resultdict


dict1={"a":1, "b":2}
dict2={"c":3, "d":4}
dict3={"a":5,"c":6}

print(mergeDicts(dict1, dict2, dict3))

