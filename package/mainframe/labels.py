from tkinter import *
import package.functionalities.operation
class Labels():

    SMALL_FONT = ('Sans-serif', 10, 'bold')
    MEDIUM_FONT = ('Sans-serif', 20, 'bold')
    BIG_FONT = ('Sans-serif', 40, 'bold')         

    def restarting_score(self):       

        score_0_label = Label(self, text='0', font=(Labels.MEDIUM_FONT))
        score_0_label.place(x=120, y=400)  
        
        score_1_label = Label(self, text='0', font=(Labels.MEDIUM_FONT))
        score_1_label.place(x=173, y=400)  
        
        score_break = Label(self, text=':', font=(Labels.MEDIUM_FONT))
        score_break.place(x=149, y=398) 
        
        score_0 = 0
        score_1 = 0
        score_0_label['text'] = 0
        score_1_label['text'] = 0  
                        
    def label(self):
        playerg = package.functionalities.operation.player
        
        label = Label(self, text=f'Vez de {playerg}', font=(Labels.MEDIUM_FONT), foreground='#e85151')
        label.place(x=100, y=350)             
                        


        
