from tkinter import *


class Interface():

    def board():
        from package.functionalities.difficulties import Human_Player
        from package.mainframe.labels import Labels
        
        window = Tk()
        window.title('Jogando contra um amigo')
        player = "x"
        label = Label(window, text=f'Vez de {player}', font=('Sans-serif', 20, 'bold'), foreground='#e85151')
        label.grid(pady=70)
        frame = Frame(window)
        frame.grid()
        
        buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]  
        


        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text='', font=('Sans-serif', 40, 'bold'), width=3, height=1,
                                            command=lambda row=row, column=column: Human_Player.human_play(), bg='#3b3b3b', foreground='white')
                buttons[row][column].grid(row=row, column=column)        