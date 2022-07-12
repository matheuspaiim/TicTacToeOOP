from tkinter import *
import tkinter as tk
from tkinter import ttk
from package.mainframe.labels import Labels
from package.functionalities.operation import Operation
import package.functionalities.operation
class Interface():
    
    def board(self): 

        buttonsg = package.functionalities.operation.buttons           

        for row in range(3):
            for column in range(3):
                buttonsg[row][column] = Button(self, text='', font=(Labels.BIG_FONT), width=3, height=1,
                                            command=lambda row=row, column=column: HumanPlayer, bg='#3b3b3b', foreground='white')
                buttonsg[row][column].grid(row=row, column=column)        
    
    
        def o_player():  
            ... 
        self.python_image_o = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToe2.0/assets/o.png')
        button_o = ttk.Button(
            self,
            image=self.python_image_o,
            command=o_player
        )
        button_o.place(x=40, y=390)


        def x_player():
            ...
        self.python_image_x = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToe2.0/assets/x.png')   
        button_x = ttk.Button(
            self,
            image=self.python_image_x,
            command=x_player
        )
        button_x.place(x=210, y=390)
        
        
        Labels.label(self)
        Labels.restarting_score(self)

class Easy(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
           
           
class Medium(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
 
            
class Hard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
       
        
class HumanPlayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
        Operation.new_game()
        
        