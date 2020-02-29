#https://drakonhub.com/ide/doc/dzhamah/2
import random
def randomChoice(x):
    m=random.randint(1,4)
    if x==m:
        print("Победа")
    elif x>m:
        print("Введенное число больше загаданного")
    else:
        print("Введенное число меньше заданного")


x=int(input("Введите число от 1 до 4\n"))
randomChoice(x)
