from cProfile import label
from cgitb import text
from re import T
from tkinter import *
import tkinter.font as tkFont
from typing import ValuesView
from unittest import result


i = 0

ventana = Tk()
ventana.geometry("600x500")
ventana.minsize(600,500)
ventana.maxsize(600,500)
ventana.title("Calculadora")
ventana.config(bg="LightPink2")
numero = StringVar(ventana)

ArialBold = tkFont.Font(family="Comic Sans MS", size=15, weight="bold", slant="italic")

screen = Entry(ventana, justify=CENTER)
screen.place(relx=0.05,rely=0.1,relwidth=0.46,relheight=0.1)
screen.configure(font=ArialBold)


def insert(valor):
    global i
    screen.insert(i,valor)
    i+=1

def delete():
    global i
    screen.delete(0,END)
    i=0

def erase():
    global i
    i-=1
    screen.delete(i,END)
    if(i<0):
        i = 0

def doMath():
    global i
    ecuation = screen.get()
    result = eval(ecuation)
    screen.delete(0,END)
    screen.insert(0,result)

def placeCalcPad():
    num1 = Button(text='1',command= lambda: insert(1),bg='RosyBrown1',bd=5)
    num1.place(relx=0.05,rely=0.61,relwidth=0.1,relheight=0.1,)
    num2 = Button(text='2',command= lambda: insert(2),bg='RosyBrown1',bd=5)
    num2.place(relx=0.17,rely=0.61,relwidth=0.1,relheight=0.1,)
    num3 = Button(text='3',command= lambda: insert(3),bg='RosyBrown1',bd=5)
    num3.place(relx=0.29,rely=0.61,relwidth=0.1,relheight=0.1,)  
    num4 = Button(text='4',command= lambda: insert(4),bg='RosyBrown1',bd=5)
    num4.place(relx=0.05,rely=0.49,relwidth=0.1,relheight=0.1,)
    num5 = Button(text='5',command= lambda: insert(5),bg='RosyBrown1',bd=5)
    num5.place(relx=0.17,rely=0.49,relwidth=0.1,relheight=0.1,)
    num6 = Button(text='6',command= lambda: insert(6),bg='RosyBrown1',bd=5)
    num6.place(relx=0.29,rely=0.49,relwidth=0.1,relheight=0.1,)
    num7 = Button(text='7',command= lambda: insert(7),bg='RosyBrown1',bd=5)
    num7.place(relx=0.05,rely=0.37,relwidth=0.1,relheight=0.1,)
    num8 = Button(text='8',command= lambda: insert(8),bg='RosyBrown1',bd=5)
    num8.place(relx=0.17,rely=0.37,relwidth=0.1,relheight=0.1,)
    num9 = Button(text='9',command= lambda: insert(9),bg='RosyBrown1',bd=5)
    num9.place(relx=0.29,rely=0.37,relwidth=0.1,relheight=0.1,)  
    num0 = Button(text='0',command= lambda: insert(0),bg='RosyBrown1',bd=5)
    num0.place(relx=0.05,rely=0.73,relwidth=0.22,relheight=0.1,)
    AC = Button(text='AC',command=lambda:delete(),bg='RosyBrown1',bd=5)
    AC.place(relx=0.05,rely=0.25,relwidth=0.1,relheight=0.1,)
    enter = Button(text='=',command=lambda:doMath(),bg='RosyBrown1',bd=5)
    enter.place(relx=0.41,rely=0.61,relwidth=0.1,relheight=0.22,)
    add = Button(text='+',command=lambda: insert('+'),bg='RosyBrown1',bd=5)
    add.place(relx=0.41,rely=0.37,relwidth=0.1,relheight=0.1,)
    sub = Button(text='-',command=lambda: insert('-'),bg='RosyBrown1',bd=5)
    sub.place(relx=0.41,rely=0.49,relwidth=0.1,relheight=0.1,)
    mult = Button(text='*',command=lambda: insert('*'),bg='RosyBrown1',bd=5)
    mult.place(relx=0.29,rely=0.25,relwidth=0.1,relheight=0.1,)
    div = Button(text='/',command=lambda: insert('/'),bg='RosyBrown1',bd=5)
    div.place(relx=0.17,rely=0.25,relwidth=0.1,relheight=0.1,)
    eraseOne = Button(text='←',command=lambda:erase(),bg='RosyBrown1',bd=5)
    eraseOne.place(relx=0.41,rely=0.25,relwidth=0.1,relheight=0.1,)
    dot = Button(text='.',command=lambda: insert('.'),bg='RosyBrown1',bd=5)
    dot.place(relx=0.29,rely=0.73,relwidth=0.1,relheight=0.1,)

    
    num0.configure(font=ArialBold)
    num1.configure(font=ArialBold)
    num2.configure(font=ArialBold)
    num3.configure(font=ArialBold)
    num4.configure(font=ArialBold)
    num5.configure(font=ArialBold)
    num6.configure(font=ArialBold)
    num7.configure(font=ArialBold)
    num8.configure(font=ArialBold)
    num9.configure(font=ArialBold)
    AC.configure(font=ArialBold)
    enter.configure(font=ArialBold)
    add.configure(font=ArialBold)
    sub.configure(font=ArialBold)
    mult.configure(font=ArialBold)
    div.configure(font=ArialBold)
    eraseOne.configure(font=ArialBold)
    dot.configure(font=ArialBold)

y = 0

valor1 = Entry(ventana,justify=CENTER)
valor1.place(relx=0.6,rely=0.35,relwidth=0.16,relheight=0.05)
valor1.configure(font=ArialBold)
valor2 = Entry(ventana,justify=CENTER)
valor2.place(relx=0.82,rely=0.35,relwidth=0.16,relheight=0.05)
valor2.configure(font=ArialBold)
valor3 = Entry(ventana,justify=CENTER)
valor3.place(relx=0.6,rely=0.45,relwidth=0.16,relheight=0.05)
valor3.configure(font=ArialBold)
incognita = Label(ventana,text='X',textvariable=numero,bg="LightPink2")
incognita.place(relx=0.82,rely=0.45,relwidth=0.16,relheight=0.05)
incognita.configure(font=ArialBold)


def regla3():

    titulo = Label(ventana,text='Regla de 3',bg="LightPink2")
    titulo.place(relx=0.68,rely=0.25)
    titulo.configure(font=ArialBold)
    flecha1 = Label(ventana,text='➔',bg="LightPink2")
    flecha1.place(relx=0.765,rely=0.35,relwidth=0.04,relheight=0.05)
    flecha1.configure(font=ArialBold)
    flecha2 = Label(ventana,text='➔',bg="LightPink2")
    flecha2.place(relx=0.765,rely=0.45,relwidth=0.04,relheight=0.05)
    flecha2.configure(font=ArialBold)
    doRule = Button(ventana,text='Calcular', command=lambda: calcRule(),bd=5)
    doRule.place(relx=0.68,rely=0.55,relwidth=0.2,relheight=0.1)
    doRule.configure(font=ArialBold)

def calcRule():
    global y
    numero1 = valor1.get()
    numero2 = valor2.get()
    numero3 = valor3.get()
    resultado = eval('('+numero2+'*'+numero3+')'+'/'+numero1)
    numero.set(resultado)

placeCalcPad()

regla3()


ventana.mainloop()
