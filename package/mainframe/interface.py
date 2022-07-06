from re import L
from tkinter import *
import tkinter as tk
from tkinter import ttk

class Interface():

    def board():
        from package.functionalities.difficulties import Human_Player
        
        window = Tk()
        window.title('Jogando contra um amigo')
        player = ""

        frame = Frame(window)
        frame.grid(ipady=80)
        
        buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]  
        
        

        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text='', font=('Sans-serif', 40, 'bold'), width=3, height=1,
                                            command=lambda row=row, column=column: Human_Player.human_play(), bg='#3b3b3b', foreground='white')
                buttons[row][column].grid(row=row, column=column)        
    
        
        def restarting_score():       

            score_0_label = Label(window, text='0', font=(
                'Sans-serif', 20, 'bold'))
            score_0_label.place(x=120, y=400)  
            
            score_1_label = Label(window, text='0', font=(
                'Sans-serif', 20, 'bold'))
            score_1_label.place(x=173, y=400)  
            
            score_break = Label(window, text=':', font=(
                'Sans-serif', 20, 'bold'))
            score_break.place(x=149, y=398) 
            
            score_0 = 0
            score_1 = 0
            score_0_label['text'] = 0
            score_1_label['text'] = 0  
            
            label = Label(window, text=f'Vez de {player}', font=('Sans-serif', 20, 'bold'), foreground='#e85151')
            label.place(x=100, y=350)
            
                        
        def label_0(label, player):    
            label.config(text=(f'Vez de {player}'), foreground='#e85151')
        
            
        def label_1(label, player):    
            label.config(text=(f'Vez de {player}'), foreground='#3297a8')     
    
        restarting_score() 
        
    
        def button_0():  
            ...
                
        icon_0 = tk.PhotoImage(file='./assets/o.png')
        button_0 = ttk.Button(
            window,
            image=icon_0,
            command=button_0
            )

        button_0.place(x=40, y=110)

        def button_1():  
            ...
   
        icon_1 = tk.PhotoImage(file='./assets/x.png')
        button_1 = ttk.Button(
            window,
            image=icon_1,
            command=button_1
            )

        button_1.place(x=40, y=110)
                
            
