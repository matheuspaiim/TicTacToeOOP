from tkinter import *

player = 'X'
opponent = 'O'
class ReusableCode():

    SMALL_FONT = ('Sans-serif', 10, 'bold')
    MEDIUM_FONT = ('Sans-serif', 20, 'bold')
    BIG_FONT = ('Sans-serif', 40, 'bold') 

#____________________Show the scores on the board____________________

    def score(self):
        global score_x_label, score_o_label, score_x, score_o
        score_x = 0
        score_o = 0
             
        score_x_label = Label(self, text='0', font=(ReusableCode.MEDIUM_FONT))
        score_x_label.place(x=120, y=400)  
        
        score_o_label = Label(self, text='0', font=(ReusableCode.MEDIUM_FONT))
        score_o_label.place(x=173, y=400)  
        
        score_break = Label(self, text=':', font=(ReusableCode.MEDIUM_FONT))
        score_break.place(x=149, y=398)         

#____________________Reset the score to 0____________________

    def restarting_score(): 
        global score_x_label, score_o_label, score_x, score_o
        score_x = 0
        score_o = 0
        score_x_label['text'] = 0
        score_o_label['text'] = 0  
                       
#____________________Label____________________    
                    
    def label(self):
        global player, label
        label = Label(self, text=f'Vez de {player}', font=(ReusableCode.MEDIUM_FONT), foreground='#e85151')
        label.place(x=100, y=350)             
        
        
#____________________Changes player move____________________        
    def player2_move():  
        global player, label
        player = 'O'
        label.config(text=('Vez de O'), foreground='#3297a8')

    def player_move():       
        global player, label 
        player = 'X'
        label.config(text=('Vez de X'), foreground='#e85151')    

        
#____________________Set winner on the screen____________________

    def player2_win():  
        global player, label, score_o, score_o_label
        label.config(text=(player+' Venceu'), foreground='forestgreen')
        score_o+=1
        score_o_label['text'] = score_o        
    
    
    def player_win():   
        global player, label, score_x, score_x_label 
        label.config(text=(player+' Venceu'), foreground='forestgreen')
        score_x+=1
        score_x_label['text'] = score_x    

#____________________Set a tie on the screen____________________

    def tie():
        global label
        label.config(text='Empate!', foreground='gold')   