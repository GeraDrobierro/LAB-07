import matplotlib.pyplot as plt
import pandas as pd

# считываю данные из фаила
df = pd.read_csv('data2.csv', delimiter=',')
df = df['Hardness']

# Блок кода, в котором рассчитывается среднеквадратичное отклонение
h1 = []
for i in df:
    h1.append(int(i))
middle = sum(h1)//len(h1)
qsum = []
for i in h1:
    qsum.append(int((i-middle)**2))
q = (sum(qsum)//len(qsum))**(1/2)

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
    xdata = uniq # значения по оси x
    ydata = l # значения по оси y
    plt.xlabel(r'$Hardness$') 
    plt.ylabel(r'$Repetitions$') 
    plt.title(r'График распределения твердости химического материала') 
    plt.bar(xdata, ydata) 
    plt.text(60, 125, rf'$ \sigma={q}$') 
    plt.show()
