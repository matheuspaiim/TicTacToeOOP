import random
import tkinter as tk
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

    def check_winner(self):
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
        return [i for i, x in enumerate(board) if x == '']


#____________________Easy Difficulty____________________
class Easy(Operation, tk.Frame):   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Interface.board(self)
           
    def easy_play(self, row, column):
        import package.functionalities.reusable_code
        player = package.functionalities.reusable_code.player
        randomq = random.randrange(3)
        
        if self.check_winner() is False and board[row][column]['text'] == '':
            
            if player == 'X':

                board[row][column]['text'] = player

                for row in range(1):
                    for column in range(1):
                        if board[random.randrange(3)][random.randrange(3)]['text'] == '':
                            board[random.randrange(3)][random.randrange(3)]['text'] = 'O'
                            ReusableCode.player_move()
                        


            else:

                board[row][column]['text'] = player

                if self.check_winner() is False:
                    board[random.randrange(3)][random.randrange(3)]['text'] = 'X'
                    ReusableCode.player2_move()
        
                elif self.check_winner() is True:
                    ReusableCode.player2_win()
                                            
                elif self.check_winner() == 'Empate':
                    ReusableCode.tie()
                    
                    
 
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

    def human_play(self, row, column):
        import package.functionalities.reusable_code
        player = package.functionalities.reusable_code.player
        
        if self.check_winner() is False and board[row][column]['text'] == '':
            
            if player == 'X':

                board[row][column]['text'] = player
                
                if self.check_winner() is False:
                    ReusableCode.player2_move()

                elif self.check_winner() is True:
                    ReusableCode.player_win()
                    
                elif self.check_winner() == 'Empate':
                    ReusableCode.tie()

            else:

                board[row][column]['text'] = player

                if self.check_winner() is False:
                    ReusableCode.player_move()
        
                elif self.check_winner() is True:
                    ReusableCode.player2_win()
                                            
                elif self.check_winner() == 'Empate':
                    ReusableCode.tie()