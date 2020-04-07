import tkinter
def click():
    if entry.get().isdigit():
        counter.set(int(entry.get())*9/5+32)
    else:
        counter.set("Ошибка ввода")


window=tkinter.Tk()
frame=tkinter.Frame(window)
frame.pack()

counter=tkinter.IntVar()

label=tkinter.Label(frame, text="Температура в Цельсиях")
label.pack()
entry=tkinter.Entry(frame)
entry.pack()

label=tkinter.Label(frame, textvariable=counter)
label.pack()

button=tkinter.Button(frame,text="Конвертировать", command=click)
button.pack()

window.mainloop()