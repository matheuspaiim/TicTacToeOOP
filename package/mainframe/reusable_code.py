from tkinter import *

class ReusableCode():

    SMALL_FONT = ('Sans-serif', 10, 'bold')
    MEDIUM_FONT = ('Sans-serif', 20, 'bold')
    BIG_FONT = ('Sans-serif', 40, 'bold')    
             

    def restarting_score(self):       

        score_0_label = Label(self, text='0', font=(ReusableCode.MEDIUM_FONT))
        score_0_label.place(x=120, y=400)  
        
        score_1_label = Label(self, text='0', font=(ReusableCode.MEDIUM_FONT))
        score_1_label.place(x=173, y=400)  
        
        score_break = Label(self, text=':', font=(ReusableCode.MEDIUM_FONT))
        score_break.place(x=149, y=398) 
        
        score_0 = 0
        score_1 = 0
        score_0_label['text'] = 0
        score_1_label['text'] = 0  
                        
    def label(self):
        import package.functionalities.operation
        playerg = package.functionalities.operation.player
        label = Label(self, text=f'Vez de {playerg}', font=(ReusableCode.MEDIUM_FONT), foreground='#e85151')
        label.place(x=100, y=350)             

    def label_x():    
        global label
        label.config(text=("Vez de "+player), foreground="#e85151")
    
        
    def label_o():    
        
        label.config(text=("Vez de "+player), foreground="#3297a8")     
        
        
    def bot_move():  
        
        global player
        
        player = 1
        label.config(text=("Vez de "+player), foreground="#3297a8")
        

    def player_move(): 
        
        global player
        
        player = 0
        label.config(text=("Vez de "+player), foreground="#e85151")    


    def bot_win():  
        
        global player, score_o, score_o_label
        
        label.config(text=(player+" Venceu"), foreground="forestgreen")
        score_o+=1
        score_o_label['text'] = score_o        
    
    
    def player_win():   
        
        global player, score_x, score_x_label 
        
        label.config(text=(player+" Venceu"), foreground="forestgreen")
        score_x+=1
        score_x_label['text'] = score_x    


    def tie():
        
        label.config(text="Empate!", foreground="gold")   
