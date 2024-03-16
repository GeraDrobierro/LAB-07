import numpy as np
import random
import datetime

#генерируем рандомный список из 1 млн. элементов
randnums_x = list(range(1000000))
random.shuffle(randnums_x)
x = (randnums_x[0:1000000])
randnums_y = list(range(1000000))
random.shuffle(randnums_y)
y = (randnums_y[0:1000000])

# Время поэлементного умнжожения массивов
def randmmassive1(x, y):
    x = np.array(x) # преобразуем списки в массивы
    y = np.array(y)
    start = datetime.datetime.now() # фиксируем время начала выполнения функции
    np.multiply(x, y)
    finish = datetime.datetime.now() # фиксируем время оконачания выполнения функции
    massivetime = finish - start # итоговое время для массивов
    return massivetime

# Время поэлементного умножения списков
def randmmassive2(x, y): # используем списки, созданные в начале
    st = datetime.datetime.now()# фиксируем время начала выполнения функции
    np.multiply(x, y)
    fin = datetime.datetime.now()# фиксируем время оконачания выполнения функции
    listtime = fin - st # итоговое время для массивов
    return listtime

# сравнение времен
def max():
    if randmmassive1(x,y)<randmmassive2(x,y):
        print('1')
    else:
        print('0')

if __name__ == '__main__':
    max()
