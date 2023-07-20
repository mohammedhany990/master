
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
x=5

def get(x,func):
    func2 = ""
    for i in range(len(func)):
        if func[i] == 'x':
            func2 += 'X'
            continue
        func2 += func[i]
        
    func = func2
    func2 = ""
    for i in range(len(func)):
        if func[i] == '*' and func[i + 1] == 'X':
            continue
        func2 += func[i]
    func = func2
    if re.findall('^', func):
        func = func.replace('^', "**")

    z = func.split(' ')
    sum = 0
    lis = list()
    for i in z:
        if i == '-' or i == '*' or i == '+' or i == '/':
            lis.append(i)
            continue

        if i.isdigit():
            lis.append(int(i))
            continue
        if i[0] =='-':
            yes = 1
            if i[1:].isdigit():
                lis.append(int(i))
                yes = 0
            if yes == 0:
                continue

        id = i.index('X')
        if len(i) == 1:
            lis.append(x)
            # print(f"1  {x}")
            continue

        coef = 1
        if len(i) > 1 and i[0] != 'X':
            coef = int(i[0:id])

        power = 1
        if i[id:] != 'X':
            power = int(i[id + 3:])

        ans = coef * (x ** power)
        lis.append(ans)

    for i in lis:
        if i == '*':
            id = lis.index(i)
            l = lis[id - 1]
            r = lis[id + 1]
            lis[id - 1] = 0
            lis[id + 1] = l * r
            lis.remove(lis[id - 1])
            id = lis.index(i)
            lis.remove(lis[id])
        elif i == '/':
            id = lis.index(i)
            l = lis[id - 1]
            r = lis[id + 1]
            lis[id - 1] = 0
            lis[id + 1] = float(l / r)
            lis.remove(lis[id - 1])
            id = lis.index(i)
            lis.remove(lis[id])

    for i in lis:
        if i == '-':
            id = lis.index(i)
            lis[id + 1] = -lis[id + 1]
            lis.remove(lis[id])
        elif i == '+':
            lis.remove('+')

    for i in lis:
        sum += i
    return sum


func = str(input("Enter Your Function: "))
mn = int(input("Enter Minimum Number : "))
mx = int(input("Enter Maximum Number : "))

x = np.linspace(mn, mx, 1000)  

y = []
for i in x:
    ans = get(i,func)
    y.append(ans)

print(x)
print(y)


fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(x, y)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Function')

plt.show()


