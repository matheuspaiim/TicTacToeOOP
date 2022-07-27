from tkinter import *
import tkinter as tk
from tkinter import ttk
from package.functionalities.reusable_code import ReusableCode

class Interface(tk.Frame):

#____________________Visual Board____________________
    
    def board(self): 
        import package.functionalities.operation
        from package.functionalities.operation import Easy, HumanPlayer, Operation
        board = package.functionalities.operation.board     

        for row in range(3):
            for column in range(3):
                board[row][column] = Button(self, text='', font=(ReusableCode.BIG_FONT), width=3, height=1,
                                            command=lambda row=row, column=column: Easy.easy_play(self, row, column), bg='#3b3b3b', foreground='white')
                board[row][column].grid(row=row, column=column)   
                  
                  
#____________________Restart Button____________________
            
        def restart_button(self):
            restart_button = ttk.Button(self, text='Reiniciar', command=Operation.new_game)
            restart_button.place(x=39, y=460)                          
        restart_button(self)
        
        
#____________________Return to menu button____________________       
        
        def reset_score(self):  
            return_button = ttk.Button(self, text='Zerar placar', command=ReusableCode.restarting_score)
            return_button.place(x=194, y=460)                 
        reset_score(self)


#____________________Change Player Button (x)____________________
        
        def x_player():
            import package.functionalities.reusable_code
            player = package.functionalities.reusable_code.player 
            if player != '':
                Operation.new_game()
                ReusableCode.player_move()
                  
        self.python_image_x = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToeOOP/assets/x.png')   
        button_x = ttk.Button(
            self,
            image=self.python_image_x,
            command=x_player
        )
        button_x.place(x=210, y=390)
        
        
#____________________Change Player Button (o)____________________
        
        def o_player(): 
            import package.functionalities.reusable_code
            player = package.functionalities.reusable_code.player 
            if player != '':
                Operation.new_game()
                ReusableCode.player2_move()
                 
        self.python_image_o = tk.PhotoImage(file='C:/Users/mathe/Documents/GitHub/TicTacToeOOP/assets/o.png')
        button_o = ttk.Button(
            self,
            image=self.python_image_o,
            command=o_player
        )
        button_o.place(x=40, y=390)        


#____________________Score and turn label____________________
        
        ReusableCode.label(self)
        ReusableCode.score(self)