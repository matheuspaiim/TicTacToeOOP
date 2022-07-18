from tkinter import *
import tkinter as tk
from package.mainframe.interface import Interface
from package.functionalities.reusable_code import ReusableCode

#____________________Board buttons____________________

board =  [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]  
class Operation():
#____________________Restart Board____________________   
 
    def new_game():
        for row in range(3):
            for column in range(3):
                board[row][column].config(text='', bg='#3b3b3b')

#____________________Check if there are still empty spaces on the board____________________

    def empty_spaces():
        for row in range(3):
            for column in range(3):
                if (board[row][column]['text'] == ''):
                    return True
        return False
    
#____________________Checks for a winner____________________            

    def check_winner():
        for row in range(3):
            if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != '':
                board[row][0].config(bg='forestgreen')
                board[row][1].config(bg='forestgreen')
                board[row][2].config(bg='forestgreen')
                return True

        for column in range(3):
            if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != '':
                board[0][column].config(bg='forestgreen')
                board[1][column].config(bg='forestgreen')
                board[2][column].config(bg='forestgreen')
                return True

        if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
            board[0][0].config(bg='forestgreen')
            board[1][1].config(bg='forestgreen')
            board[2][2].config(bg='forestgreen')
            return True

        elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
            board[0][2].config(bg='forestgreen')
            board[1][1].config(bg='forestgreen')
            board[2][0].config(bg='forestgreen')
            return True

        elif Operation.empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    board[row][column].config(bg='gold')
            return 'Empate'

        else:
            return False

#____________________Easy Difficulty____________________
class Easy(tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
           
#____________________Medium Difficulty____________________           
class Medium(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
 
#____________________Hard Difficulty____________________            
class Hard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
       
#____________________Play with a friend____________________        
class HumanPlayer(Operation, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)

    def human_play(row, column):
        import package.functionalities.reusable_code
        player = package.functionalities.reusable_code.player
        if board[row][column]['text'] == '' and Operation.check_winner() is False:

            if player == 'X':

                board[row][column]['text'] = player
                
                if Operation.check_winner() is False:
                    ReusableCode.bot_move()

                elif Operation.check_winner() is True:
                    ReusableCode.player_win()
                    
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()

            else:

                board[row][column]['text'] = player

                if Operation.check_winner() is False:
                    ReusableCode.player_move()
        
                elif Operation.check_winner() is True:
                    ReusableCode.bot_win()
                                            
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()

