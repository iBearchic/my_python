import tkinter
import json
tasks=[]

def addt():
    with open("data_file.json", "w") as write_file:
        tasks.append({"Задача": entry1r.get(),"Категория": entry2r.get(),"Время": entry3r.get()})
        json.dump(tasks, write_file)

def showt():
    with open("data_file.json", "r") as read_file:
        data=json.load(read_file)
        print(data)

def exitb():
    window.destroy()


window=tkinter.Tk(className="Менеджер задач")
frame=tkinter.Frame(window)
frame.pack()

frame2=tkinter.Frame(window)
frame2.pack()

lable1l=tkinter.Label(frame,text="Задача:")
lable1l.grid(row=0,column=0)
entry1r=tkinter.Entry(frame)
entry1r.grid(row=0,column=1)

lable2l=tkinter.Label(frame,text="Категория:")
lable2l.grid(row=1,column=0)
entry2r=tkinter.Entry(frame)
entry2r.grid(row=1,column=1)

lable3l=tkinter.Label(frame,text="Время:")
lable3l.grid(row=2,column=0)
entry3r=tkinter.Entry(frame)
entry3r.grid(row=2,column=1)

butt1=tkinter.Button(frame2,text="Заказать",command=addt)
butt1.pack()
butt2=tkinter.Button(frame2,text="Список задач", command=showt)
butt2.pack()
butt3=tkinter.Button(frame2,text="Выход", command=exitb)
butt3.pack()

window.mainloop()