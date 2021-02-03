from tkinter import *
import time 
import csv
data = []
with open("saves.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
data=(data)
print(data)
f.close()
count=int(data.index([1]))
print(count)

print("1")
count = 0 #количество кликов
mult = 1 #умножение кликов
autoclickers = 0 #количество автокликов
pricemlt = 1 #цена умножения
autoprice = 1 #цена автокликов











def autoclickbuy(event):
    global count
    global autoprice
    global autoclickers #
    if count < 7*autoprice:
        nem()
    else:
        count -= 7*autoprice #
        autoclickers += 1+autoclickers #
        autoprice= autoprice*2
        albl.config(text="("+str(autoclickers)+")Купить авто клик: "+str(7*autoprice))
        btn['text']=str(count)
        sec()

def autoclick():
    global win
    global count
    global autoclickers
    count += autoclickers #
    win.after(1000, autoclick) #
    btn['text']=str(count)


def vajutame(event):
    global count
    global mult
    count = count+mult
    btn['text']=str(count)
def mltclickbuy(event):
    global count
    global pricemlt
    global mult
    if count < 5*pricemlt:
        nem()
    elif count >= 5*pricemlt:
        mult = mult*2
        count = count - 5*pricemlt
        pricemlt= pricemlt*4
        btn['text']=str(count)
        sec()
        lbl.config(text="(x"+str(mult)+") Купить двойной клик: "+str(5*pricemlt))
def nem():
    balbl.config(text="не хватает кридитов!",bg="red")
def sec():
    balbl.config(text="куплено!",bg="green")



win=Tk()
win.title("Akna nimetus")
win.geometry("1000x700")

btn=Button(win,text="Vajuta \nsiia",fg="white", bg="black", font="Arial 50",width=17,height=3,relief=SUNKEN)
lbl=Label(win,text="(x2)Купить двойной клик: 5",fg="white", bg="black", font="Arial 40", width=25,height=3)
albl=Label(win,text="(1) Купить ауто клик: 7",fg="white", bg="black", font="Arial 40", width=25,height=3)
balbl=Label(win,text="...",fg="white", bg="black", font="Arial 40", width=25,height=3)
ex=Label(win,text="...",fg="black", bg="gray", font="Arial 40", width=5,height=3)
var=IntVar()
var.set(3)

btn.bind("<Button-1>",vajutame)
lbl.bind("<Button-1>",mltclickbuy)
albl.bind("<Button-1>",autoclickbuy)
btn.pack()

lbl.pack()
btn.pack()
albl.pack()
balbl.pack()
autoclick() 
win.mainloop()








