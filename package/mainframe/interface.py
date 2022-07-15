from tkinter import *
import tkinter as tk
from tkinter import ttk
from package.functionalities.reusable_code import ReusableCode

class Interface():
#____________________Visual Board____________________
    
    def board(self): 
        import package.functionalities.operation
        from package.functionalities.operation import HumanPlayer, Operation
        board = package.functionalities.operation.board           

        for row in range(3):
            for column in range(3):
                board[row][column] = Button(self, text='', font=(ReusableCode.BIG_FONT), width=3, height=1,
                                            command=lambda row=row, column=column: HumanPlayer.human_play(row, column), bg='#3b3b3b', foreground='white')
                board[row][column].grid(row=row, column=column)   
                  
#____________________Restart Button____________________
            
        def restart_button(self):
            human_button = Button(self, text='Restart', font=ReusableCode.SMALL_FONT, padx=15, pady=2, command=Operation.new_game)
            human_button.place(x=114, y=460)                          
        restart_button(self)
        
#____________________Change Player Button (o)____________________
        
        def o_player(): 
            import package.functionalities.reusable_code
            player = package.functionalities.reusable_code.player 
            if player == "O" or player == "X":
                HumanPlayer.human_play(row, column)
                Operation.new_game()
                ReusableCode.label_o()
                ReusableCode.restarting_score()                
                 
        self.python_image_o = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToe2.0/assets/o.png')
        button_o = ttk.Button(
            self,
            image=self.python_image_o,
            command=o_player
        )
        button_o.place(x=40, y=390)

#____________________Change Player Button (x)____________________
        
        def x_player():
            import package.functionalities.reusable_code
            player = package.functionalities.reusable_code.player 
            if player == "X" or player == "O":
                HumanPlayer.human_play(row, column)
                Operation.new_game()
                ReusableCode.label_x()
                ReusableCode.restarting_score() 
                  
        self.python_image_x = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToe2.0/assets/x.png')   
        button_x = ttk.Button(
            self,
            image=self.python_image_x,
            command=x_player
        )
        button_x.place(x=210, y=390)
        
        ReusableCode.label(self)
        ReusableCode.score(self)