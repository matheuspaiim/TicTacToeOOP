from tkinter import *
from package.functionalities.operation import Easy, Hard, HumanPlayer
from package.functionalities.reusable_code import ReusableCode
import tkinter as tk

#____________________Mainframe and frame selection____________________
class Window(tk.Tk):
   
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='assets/TTT.ico')
        tk.Tk.wm_title(self, 'Jogo da Velha')  
        window = tk.Frame(self)
        window.pack(side='top', fill='both', expand= True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (Menu, Easy, Hard, HumanPlayer):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
    
        self.show_frame(Menu)
                    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#____________________First Page (Menu)____________________
class Menu(tk.Frame):
         
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
             
        human_button = Button(self, text='Jogar contra um amigo', font=ReusableCode.SMALL_FONT, padx=15, pady=10, command=lambda: controller.show_frame(HumanPlayer), cursor="hand2")
        human_button.place(x=65, y=150)
        
        easy_button = Button(self, text='Fácil', font=ReusableCode.SMALL_FONT, padx=18, pady=10, command=lambda: controller.show_frame(Easy), state= DISABLED)
        easy_button.place(x=119, y=200)  
        
        hard_button = Button(self, text='Difícil', font=ReusableCode.SMALL_FONT, padx=15, pady=10, command=lambda: controller.show_frame(Hard), state= DISABLED)
        hard_button.place(x=120, y=250)           


window = Window()
window.geometry('318x510')
window.mainloop()