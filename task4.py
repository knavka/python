def compare(a,b,c):
    if (a>b):
        print(str(a)+'>'+str(b))
        print('Свершилось!')
    elif (a < b):
        print(str(a) + '<' + str(b))
        print('Да ну!')
    else:
        print(str(a) + '=' + str(b))
        print('А если так?')
        compare(a+c,b-c,c)

print("Введите а:")
a=int(input())

print("Введите b:")
b=int(input())

print("Введите c:")
c=int(input())

compare(a,b,c)

