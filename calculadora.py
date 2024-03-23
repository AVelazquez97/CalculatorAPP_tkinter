#!/usr/bin/python3

import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, RIGHT
from functools import partial

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def validate():
    return  

class Calculator():
    def __init__(self):
        self.results_length = 0
        self.entry_font = ("Book Antiqua", "25", "normal")

        # -------- main_window configs -----------
        self.main_window = tk.Tk()
        self.main_window.title("Calculadora")
        self.path = resource_path('calculator-bw.ico')
        self.main_window.iconbitmap(self.path)
        self.main_window.geometry("400x350")
        # -------- main_window configs -----------

        # -------- styles --------
        self.ac_button_style = ttk.Style()
        self.ac_button_style.configure("AC.TButton", font= ("Comic sens MC","12","bold"),  
	                                   relief = "raised", background="#DF9889")

        self.frm_style = ttk.Style()
        self.frm_style.configure("Frames.TFrame", background="Grey", relief = 'sunken')

        self.frm_left_inf_style = ttk.Style()
        self.frm_left_inf_style.configure("FrameLeftInf.TButton", background="Orange")

        self.btn_style_num = ttk.Style()
        self.btn_style_num.configure("Numbers.TButton", font=("Book Antiqua", "14", "normal"), background="Orange")

        self.btn_style_op = ttk.Style()
        self.btn_style_op.configure("Operators.TButton", font=("Book Antiqua", "18", "normal"), foreground="Black",
                                     background="Grey")
        # -------- end styles --------

        # ------------- frames configs -------------
        self.frame_sup = ttk.Frame(self.main_window, style="Frames.TFrame")
        self.frame_inf = ttk.Frame(self.main_window, style="Frames.TFrame")
        self.frame_right_inf = ttk.Frame(self.frame_inf, style="Frames.TFrame")
        self.frame_left_inf = ttk.Frame(self.frame_inf, style="FrameLeftInf.TButton")

        # frames position
        self.frame_sup.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        self.frame_inf.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
        self.frame_left_inf.pack(expand=True, fill=BOTH, side=LEFT)
        self.frame_right_inf.pack(expand=True, fill=BOTH, side=RIGHT)
        # ------------- frames configs -------------
       
        # ------------ result box configs ------------
        self.results_box = ttk.Entry(self.frame_sup, font=self.entry_font)
        self.results_box.place(relx=0, rely=0, relwidth=0.8, relheight=1)
        # ------------ end result box configs ------------

        # ------------ button clean entry ------------
        self.ac_button = ttk.Button(self.frame_sup, text= "AC", style="AC.TButton", command=lambda: self.erase_all())
        self.ac_button.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
        #------------ end button clean entry ------------

        # -------- number buttons config --------
        self.numbers = [["1", "2", "3"],
                        ["4", "5", "6"],
                        ["7", "8", "9"],
                        ["π", "0", "."]]

        # -------- creation and position --------
        j=0
        for row in self.numbers:
            i=0
            for option in row:
                self.btn = ttk.Button(self.frame_left_inf, text=option, style="Numbers.TButton", 
                                      command=partial(self.insert_to_box, option))
                self.btn.place(relx=i, rely=j, relwidth=0.34, relheight=0.25)
                i+=0.33
            j+=0.25

        # -------- end number buttons config --------

        # ------------- operator buttons config -------------
        self.operators = [["√", "^"],
                          ["*", "/"],
                          ["+", "-"],
                          ["DEL", "="]]
        # -------- creation and position --------
        j=0
        for row in self.operators:
            i=0
            for option in row:
                if option == "DEL":
                    self.btn = ttk.Button(self.frame_right_inf, text=option, style="Operators.TButton", 
                                      command=lambda: self.erase())
                elif option == "=":
                    self.btn = ttk.Button(self.frame_right_inf, text=option, style="Operators.TButton", 
                                      command=lambda: self.operation())
                else:                   
                    self.btn = ttk.Button(self.frame_right_inf, text=option, style="Operators.TButton", 
                                          command=partial(self.insert_to_box, option))
                self.btn.place(relx=i, rely=j, relwidth=0.50, relheight=0.25)
                i+=0.50
            j+=0.25
        
        # ------------- end operator buttons configs -------------

        self.main_window.mainloop()
    
    def insert_to_box(self, data):
        if data == "π":
            data = "3.1416"
            self.results_length += 6
        elif data == "√":
            data = "3.1416"
        else:
            self.results_length += 1
        
        self.results_box.insert(self.results_length, data)

    def erase(self):
        if self.results_length >= 0:
            self.results_box.delete(self.results_length, last=None)
            self.results_length-=1
      
    def operation(self):
        ecuacion = self.results_box.get()
        if self.results_length !=0:		
            try:
                result = str(eval(ecuacion))
                self.results_length = len(result) 
            except:
                result = 'ERROR'

            self.results_box.delete(0,'end')
            self.results_box.insert(0,result)

    def erase_all(self):
        self.results_box.delete(0, 'end')
        self.results_length = 0	

def main():
    calculator_app = Calculator()
    
if __name__ == '__main__':
    main()
