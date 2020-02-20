#Первые упражнения
from operator import add
def fun(x):
    return add(pow(x,4),pow(4,x))

def fun1(x,y):
    return add(pow(y,4),pow(4,x))

#Упражнение на среднее
def div(a,b):
    return a/b

def average(a,b,c):
    return div(add(add(a,b),c),3)




