from pickle import EMPTY_SET
import random
from tkinter import *
import tkinter as tk
from zoneinfo import available_timezones

from pkg_resources import empty_provider
from package.mainframe.interface import Interface
from package.functionalities.reusable_code import ReusableCode

#____________________Board buttons____________________

board =  [['', '', ''],
          ['', '', ''],
          ['', '', '']]  
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

    def available_moves():
        ...
        
    def random_move():
        ...            

        
#____________________Easy Difficulty____________________
class Easy(Operation, tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
           
    def easy_play(row, column):
        import package.functionalities.reusable_code
        player = package.functionalities.reusable_code.player
        
        if Operation.check_winner() is False:
            
            if player == 'X':

                board[row][column]['text'] = player
                
                if Operation.check_winner() is False:
                    board[random.randrange(3)][random.randrange(3)]['text'] = 'O'
                    ReusableCode.player_move()

                elif Operation.check_winner() is True:
                    ReusableCode.player_win()
                    
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()

            else:

                board[row][column]['text'] = player

                if Operation.check_winner() is False:
                    board[random.randrange(3)][random.randrange(3)]['text'] = 'X'
                    ReusableCode.player2_move()
        
                elif Operation.check_winner() is True:
                    ReusableCode.player2_win()
                                            
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()   
                    
                    
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
 
    # This is the minimax function. It considers all
    # the possible ways the game can go and returns
    # the value of the board
    def minimax(board, depth, isMax):
        score = Hard.evaluate(board)
    
        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 10):
            return score - depth
    
        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -10):
            return score + depth
    
        # If there are no more moves and no winner then
        # it is a tie
        if (Hard.empty_spaces() == False):
            return 0
    
        # If this maximizer's move
        if (isMax):    
            best = -1000
    
            # Traverse all cells
            for row in range(3):        
                for column in range(3):
                
                    # Check if cell is empty
                    if (board[row][column]['text'] == ''):
                    
                        # Make the move
                        board[row][column]['text'] = 'X'
    
                        # Call minimax recursively and choose
                        # the maximum value
                        best = max( best, Hard.minimax(board,
                                                depth + 1,
                                                not isMax) )
    
                        # Undo the move
                        board[row][column]['text'] = ''
            return best
    
        # If this minimizer's move
        else:
            best = 1000
    
            # Traverse all cells
            for row in range(3):        
                for column in range(3):
                
                    # Check if cell is empty
                    if (board[row][column]['text'] == ''):
                    
                        # Make the move
                        board[row][column]['text'] = 'O'
    
                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, Hard.minimax(board, depth + 1, not isMax))
    
                        # Undo the move
                        board[row][column]['text'] = ''
            return best
    
    # This will return the best possible move for the player
    def findBestMove(board):
        bestVal = -1000
        bestMove = (-1, -1)
    
        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for row in range(3):    
            for column in range(3):
            
                # Check if cell is empty
                if (board[row][column]['text'] == ''):
                
                    # Make the move
                    board[row][column]['text'] = 'X'
    
                    # compute evaluation function for this
                    # move.
                    moveVal = Hard.minimax(board, 0, False)
    
                    # Undo the move
                    board[row][column]['text'] = ''
    
                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal > bestVal):               
                        bestMove = (row, column)
                        bestVal = moveVal
        return bestMove
    
    bestMove = findBestMove(board)
 
       
#____________________Play with a friend____________________        
class HumanPlayer(Operation, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)

    def human_play(row, column):
        import package.functionalities.reusable_code
        player = package.functionalities.reusable_code.player
        
        if Operation.check_winner() is False:
            
            if player == 'X':

                board[row][column]['text'] = player
                
                if Operation.check_winner() is False:
                    ReusableCode.player2_move()

                elif Operation.check_winner() is True:
                    ReusableCode.player_win()
                    
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()

            else:

                board[row][column]['text'] = player

                if Operation.check_winner() is False:
                    ReusableCode.player_move()
        
                elif Operation.check_winner() is True:
                    ReusableCode.player2_win()
                                            
                elif Operation.check_winner() == 'Empate':
                    ReusableCode.tie()