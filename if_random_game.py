<<<<<<< HEAD
=======
#https://drakonhub.com/ide/doc/dzhamah/2
>>>>>>> 66866c22582920a72504d4cf71bf1e8625d9f140
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
