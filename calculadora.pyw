#!/usr/bin/python3

from tkinter import Frame, Scale, Tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, RIGHT, TOP

#Recibe dos números mediante 2 cajas de texto y devuelve el resultado en otra
def suma():
    n1 = float(txt2.get())
    n2 = float(txt3.get())
    r = n1 + n2
    txt1.delete(0, 'end')
    txt1.insert(0,r)
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')

#Recibe dos números e imprime en pantalla el resultado de restarle el 2do al 1ero
def resta():
    n1 = float(txt2.get())
    n2 = float(txt3.get())
    r = n1 - n2
    txt1.delete(0, 'end')
    txt1.insert(0,r)
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')

#Recibe dos números e imprime en pantalla el resultado de multiplicarlos entre sí
def multiplicacion():
    n1 = float(txt2.get())
    n2 = float(txt3.get())
    r = n1 * n2
    txt1.delete(0, 'end')
    txt1.insert(0,r)
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')

#Recibe dos números e imprime en pantalla el resultado de dividir el 1ero entre el 2
def division():
    n1 = float(txt2.get())
    n2 = float(txt3.get())
    r = n1 / n2
    txt1.delete(0, 'end')
    txt1.insert(0,r)
    txt2.delete(0, 'end')
    txt3.delete(0, 'end')

#Limita el ingreso a únicamente números
def validate_entry(text):
    return text.isdecimal()

#Variable global que almacena una fuente
timesBoldIt = ("Times", "20", "bold italic")


# -------- main_window configs -----------
main_window = Tk()
main_window.title("Calculadora")
main_window.iconbitmap('calculator-bw.ico')
main_window.geometry("550x350")
# -------- main_window configs -----------


# ------------- frames configs -------------
# frames creation
frameSup = Frame(main_window, highlightbackground="grey", highlightthickness=1)
frameInf = Frame(main_window)
frameLeftInf = Frame(frameInf, bg="Orange", highlightbackground="grey", highlightthickness=1)
frameRightInf = Frame(frameInf, highlightbackground="grey", highlightthickness=1)

# frames position
frameSup.pack(expand=True, fill=BOTH, side=TOP)
frameInf.pack(expand=True, fill=BOTH, side=TOP)
frameLeftInf.pack(expand=True, fill=BOTH, side=LEFT)
frameRightInf.pack(expand=True, fill=BOTH, side=RIGHT)
# ------------- frames configs -------------


# ------------- labels configs -------------
# labels creation
label1 = ttk.Label(frameLeftInf, text="Ingrese el primer valor: ", font=("arial", "10", "bold"))
label2 = ttk.Label(frameLeftInf, text="Ingrese el segundo valor: ", font=("arial", "10", "bold"))

# labels position
label1.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)
label2.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.8)
# ------------- labels configs -------------


# ------------ text box configs ------------
txt1 = ttk.Entry(frameSup, font=timesBoldIt, validate="key", validatecommand=(main_window.register(validate_entry), "%S"))
txt2 = ttk.Entry(frameLeftInf, font=timesBoldIt, validate="key", validatecommand=(main_window.register(validate_entry), "%S"))
txt3 = ttk.Entry(frameLeftInf, font=timesBoldIt, validate="key", validatecommand=(main_window.register(validate_entry), "%S"))

txt1.place(relx=0, rely=0, relheight=1, relwidth=1)
txt2.place(relx=0.1, rely=0.2, relheight=0.2, relwidth=0.8)
txt3.place(relx=0.1, rely=0.7, relheight=0.2, relwidth=0.8)
# ------------ text box configs ------------


# ------------- buttons configs -------------
# buttons creation
btnSum = ttk.Button(frameRightInf, text="+", command=suma)
btnRes = ttk.Button(frameRightInf, text="-", command=resta)
btnMul = ttk.Button(frameRightInf, text="*", command=multiplicacion)
btnDiv = ttk.Button(frameRightInf, text="/", command=division)

# buttons position
btnSum.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
btnRes.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
btnMul.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
btnDiv.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
# ------------- buttons configs -------------

main_window.mainloop() #end program

