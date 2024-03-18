import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# считываю данные из фаила
df = pd.read_csv('data2.csv', delimiter=',')
df = df['Hardness']
# формирую уникальный список из значений тверодсти указанных элементов
y = []
for i in df:
    y.append(int(i))
uniq = []
for j in y:
    if j not in uniq:
        uniq.append(j)
# Блок кода в котором рассчитывается количество повторяющихся значений твердости
A = [int(x) for x in df]
count = {}
for e in A:
    count[e] = count.get(e, 0) + 1
doubles = {element: count for element, count in count.items() if count > 1}

# список, где хранятся числа, показывающее кол-во повторений опредленной твердости в списке uniq
l = []
for i in doubles:
    l.append(doubles[i])

# график
if __name__ == '__main__':
    xdata = uniq
    ydata = l

    plt.bar(xdata, ydata)
    plt.show()

