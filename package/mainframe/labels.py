from tkinter import *
import tkinter as tk
from tkinter import ttk
from package.mainframe.interface import Interface

class Labels():

    def restarting_score():

        score_0 = 0
        score_1 = 0
        score_0_label['text'] = 0
        score_1_label['text'] = 0  
        

        score_0_label = Label(Interface.window, text='0', font=(
            'Sans-serif', 20, 'bold'))
        score_0_label.place(x=120, y=120)  
        
        score_1_label = Label(Interface.window, text='0', font=(
            'Sans-serif', 20, 'bold'))
        score_1_label.place(x=173, y=120)  
         
        score_break = Label(Interface.window, text=':', font=(
            'Sans-serif', 20, 'bold'))
        score_break.place(x=149, y=118)     
             
    def label_0(label, player):    
        label.config(text=(f'Vez de {player}'), foreground='#e85151')
    
        
    def label_1(label, player):    
        label.config(text=(f'Vez de {player}'), foreground='#3297a8')     
        
        
    def button_0():  

        icon_0 = tk.PhotoImage(file='./assets/o.png')
        button_0 = ttk.Button(
            Interface.window,
            image=icon_0,
            command=button_0
        )

        button_0.place(x=40, y=110)

    def button_1():  

        icon_1 = tk.PhotoImage(file='./assets/o.png')
        button_1 = ttk.Button(
            Interface.window,
            image=icon_1,
            command=button_1
        )

        button_1.place(x=40, y=110)