from tkinter import *
from package.functionalities.difficulties import Easy, Medium, Hard, Human_Player
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
        
        frame = Menu(window, self)
        
        self.frames[Menu] = frame
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Menu)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class Menu(tk.Frame):
    
    def initialize():   
         
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
        
        
            def restart():
                print('teste funcionamento')
        
                            
            human_button = Button(window, text='Jogar contra um amigo', font=SMALL_FONT, padx=15, pady=2, command=Human_Player.human_play)
            human_button.place(x=10, y=10)
            
            easy_button = Button(window, text='Fácil', font=SMALL_FONT, padx=10, pady=2, command=Easy.easy_play)
            easy_button.place(x=65, y=50)  
            
            medium_button = Button(window, text='Médio', font=SMALL_FONT, padx=10, pady=2, command=Medium.medium_play)
            medium_button.place(x=62, y=85)  
            
            hard_button = Button(window, text='Difícil', font=SMALL_FONT, padx=10, pady=2, command=Hard.hard_play)
            hard_button.place(x=63, y=120)     
                
            reset_button = Button(window, text='Restart', font=SMALL_FONT, padx=10, pady=2, command=restart)
            reset_button.place(x=60, y=160)
        
window = Window()
window.mainloop()
        