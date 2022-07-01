from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont



class Interface():

    def board():
        window = Tk()
        window.title("Jogando contra um amigo")
        frame = Frame(window)
        frame.grid()
        buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        def human_player(row, column):
            buttons[row][column]['text'] == ""
            ...    
        for row in range(3):
            for column in range(3):
                buttons[row][column] = Button(frame, text="", font=('Sans-serif', 40, "bold"), width=3, height=1,
                                            command=lambda row=row, column=column: human_player(row, column), bg="#3b3b3b", foreground="white")
                buttons[row][column].grid(row=row, column=column)    
    
    ...