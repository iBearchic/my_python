import random
def randomChoice(x):
    m=random.randint(1,4)
    if x==m:
        print("Победа")
    else:
        print("Попробуйте еще раз!")


x=int(input("Введите число от 1 до 4\n"))
randomChoice(x)
