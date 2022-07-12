from tkinter import *

player = "X"
buttons =  [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]     

class Operation():
 
    def new_game():

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg="#3b3b3b")


    def empty_spaces():
        global spaces, buttons  
        spaces = 9
        
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1
                                    
        if spaces == 0:
            return False
        else:
            return True
    
            
    def check_winner():

        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="forestgreen")
                buttons[row][1].config(bg="forestgreen")
                buttons[row][2].config(bg="forestgreen")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="forestgreen")
                buttons[1][column].config(bg="forestgreen")
                buttons[2][column].config(bg="forestgreen")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="forestgreen")
            buttons[1][1].config(bg="forestgreen")
            buttons[2][2].config(bg="forestgreen")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="forestgreen")
            buttons[1][1].config(bg="forestgreen")
            buttons[2][0].config(bg="forestgreen")
            return True

        elif Operation.empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="gold")
            return "Empate"

        else:
            return False
