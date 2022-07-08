from tkinter import *

MEDIUM_FONT = ('Sans-serif', 20, 'bold')

class Labels():
    
    def restarting_score(self):       

        score_0_label = Label(self, text='0', font=(MEDIUM_FONT))
        score_0_label.place(x=120, y=400)  
        
        score_1_label = Label(self, text='0', font=(MEDIUM_FONT))
        score_1_label.place(x=173, y=400)  
        
        score_break = Label(self, text=':', font=(MEDIUM_FONT))
        score_break.place(x=149, y=398) 
        
        score_0 = 0
        score_1 = 0
        score_0_label['text'] = 0
        score_1_label['text'] = 0  
                        
                    
    def label_0(label, player):    
        label.config(text=(f'Vez de {player}'), foreground='#e85151')
    
        
    def label_1(label, player):    
        label.config(text=(f'Vez de {player}'), foreground='#3297a8') 

        
