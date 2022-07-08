from tkinter import *
from package.functionalities.game import Interface, Easy, Medium, Hard, HumanPlayer
import tkinter as tk


SMALL_FONT = ('Sans-serif', 10, 'bold')


class Window(tk.Tk):
   
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand= True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
    
        self.frames = {}
        
        for F in (Menu, Interface, Easy):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Menu(tk.Frame):
         
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        def restart():
            print('teste funcionamento')
                            
        human_button = Button(self, text='Jogar contra um amigo', font=SMALL_FONT, padx=15, pady=2, command=lambda: controller.show_frame(HumanPlayer))
        human_button.place(x=65, y=100)
        
        easy_button = Button(self, text='Fácil', font=SMALL_FONT, padx=10, pady=2, command=lambda: controller.show_frame(Easy))
        easy_button.place(x=128, y=150)  
        
        medium_button = Button(self, text='Médio', font=SMALL_FONT, padx=10, pady=2, command=lambda: controller.show_frame(Medium))
        medium_button.place(x=124, y=200)  
        
        hard_button = Button(self, text='Difícil', font=SMALL_FONT, padx=10, pady=2, command=lambda: controller.show_frame(Hard))
        hard_button.place(x=125, y=250)     
            
        reset_button = Button(self, text='Restart', font=SMALL_FONT, padx=10, pady=2, command=restart)
        reset_button.place(x=120, y=300)
        
        
            
window = Window()
window.geometry("318x470")
window.title("Menu")
window.mainloop()