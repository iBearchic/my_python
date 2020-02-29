def promotion(date, amount):
    if(date=="завтра"):
        if(amount>=20):#25% скидка
            return 0.75
        else:#5% скидка
            return 0.95
    elif(date=="сегодня"):
        if(amount>=20):#20% скидка
            return 0.8
        else:
            return 1

def ticketPrice(film, date, time, amount):
    p=promotion(date, amount)
    if(film=="Паразиты"):
        if(time==12):
            print("Стоимость заказа: ",250*amount*p," рублей")
        elif(time==16):
            print("Стоимость заказа: ",350*amount*p," рублей")
        else:
            print("Стоимость заказа: ",450*amount*p," рублей")
    elif(film=="1917"):
        if(time==10):
            print("Стоимость заказа: ",250*amount*p," рублей")
        elif(time==13):
            print("Стоимость заказа: ",350*amount*p," рублей")
        else:
            print("Стоимость заказа: ",350*amount*p," рублей")
    else:
        if(time==10):
            print("Стоимость заказа: ",350*amount*p," рублей")
        elif(time==14):
            print("Стоимость заказа: ",450*amount*p," рублей")
        else:
            print("Стоимость заказа: ",450*amount*p," рублей")

            
film=input("Выберите фильм из предложенных: Паразиты, 1917, Соник в кино\n")
date=input("Выберите дату: сегодня или завтра\n")
if (film=="Паразиты"):
    time=input("Выберите время сеанса: 12:00, 16:00, 20:00\n")
elif (film=="1917"):
    time=input("Выберите время сеанса: 10:00, 13:00, 16:00\n")
else:
    time=input("Выберите время сеанса: 10:00, 14:00, 18:00\n")
time=int(time[:2])
amount=int(input("Сколько билетов покупаем?\n"))
ticketPrice(film, date, time, amount)




