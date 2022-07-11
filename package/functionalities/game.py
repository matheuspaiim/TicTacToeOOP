from tkinter import *
import tkinter as tk
from tkinter import ttk
from package.mainframe.labels import Labels
class Interface(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        
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

        Labels.restarting_score(self)

class Easy(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    
class Medium(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ...
 
            
class Hard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ...
       
        
class HumanPlayer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ...
        
        