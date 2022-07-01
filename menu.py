from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from human import Human_Player



class Menu():
    def initialize():
        window = Tk()
        window.title("Menu")
        
        
        def restart():
            print("teste funcionamento")
            
        
        def human_player():
            window.destroy()
            Human_Player.play()

            
        human_button = Button(window, text="Jogar contra um amigo", font=('Sans-serif', 10, 'bold'), padx=15, pady=5, command=human_player)
        human_button.place(x=10, y=10)       
        reset_button = Button(window, text="Restart", font=('Sans-serif', 10, 'bold'), padx=15, pady=5, command=restart)
        reset_button.place(x=60, y=60)
        window.mainloop()
        