import tkinter
import random

def click():
    if entry.get().lower()==dic[word.get()]:
        label4.config(text="Угадали!")
        word.set(random.choice(list(dic.keys())))
    else:
        label4.config(text="Не угадали!")


dic={"dog":"собака","cat":"кошка","pig":"свинья",
"horse":"лошадь","wolf":"волк","tiger":"тигр",
"solve":"решить","start":"начать"}

window=tkinter.Tk()
frame=tkinter.Frame(window)
frame.pack()

label=tkinter.Label(frame, text="Случайное слово:")
label.pack()

word=tkinter.StringVar()
word.set(random.choice(list(dic.keys())))

label2=tkinter.Label(frame, textvariable=word)
label2.pack()

label3=tkinter.Label(frame, text="Укажите перевод слова:")
label3.pack()

entry=tkinter.Entry(frame)
entry.pack()

label4=tkinter.Label(frame)
label4.pack()

button=tkinter.Button(frame, text="Готово!", command=click)
button.pack()

window.mainloop()