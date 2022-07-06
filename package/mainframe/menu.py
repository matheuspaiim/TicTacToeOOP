from tkinter import *
from package.functionalities.difficulties import Easy, Medium, Hard, Human_Player

class Menu():
    
    def initialize():
        
        window = Tk()
        window.title('Menu')
        
        
        def restart():
            print('teste funcionamento')
    
                        
        human_button = Button(window, text='Jogar contra um amigo', font=('Sans-serif', 10, 'bold'), padx=15, pady=2, command=Human_Player.human_play)
        human_button.place(x=10, y=10)
        
        easy_button = Button(window, text='Fácil', font=('Sans-serif', 10, 'bold'), padx=10, pady=2, command=Easy.easy_play)
        easy_button.place(x=65, y=50)  
        
        medium_button = Button(window, text='Médio', font=('Sans-serif', 10, 'bold'), padx=10, pady=2, command=Medium.medium_play)
        medium_button.place(x=62, y=85)  
        
        hard_button = Button(window, text='Difícil', font=('Sans-serif', 10, 'bold'), padx=10, pady=2, command=Hard.hard_play)
        hard_button.place(x=63, y=120)     
            
        reset_button = Button(window, text='Restart', font=('Sans-serif', 10, 'bold'), padx=10, pady=2, command=restart)
        reset_button.place(x=60, y=160)
        
        window.mainloop()
        