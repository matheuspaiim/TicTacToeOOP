from tkinter import *
import tkinter as tk


class Interface(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def board():
            player = ""
            
            buttons =  [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]  
            
            label = Label(self, text=f'Vez de {player}', font=('Sans-serif', 20, 'bold'), foreground='#e85151')
            label.place(x=100, y=350)            
            

            for row in range(3):
                for column in range(3):
                    buttons[row][column] = Button(self, text='', font=('Sans-serif', 40, 'bold'), width=3, height=1,
                                                command=lambda row=row, column=column: HumanPlayer.human_play(), bg='#3b3b3b', foreground='white')
                    buttons[row][column].grid(row=row, column=column)        
        board()            


class Easy(tk.Frame):   
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Inter = Interface(self, parent)
        Inter.board()
    
    
class Medium():
    def medium_play():
        ...
 
            
class Hard():
    def hard_play():
        ...
       
        
class HumanPlayer():
    def human_play():
        ...
        
        