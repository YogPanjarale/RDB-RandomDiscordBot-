from tkinter import *
from ttt import tictactoe
from rps import rock_paper_scissor
from oddeven import odd_even
from sandl import snakes_and_ladders
win = Tk()
def ttt():
    tictactoe()  
    return
def rockpaperscissors():
    rock_paper_scissor() 
    return
def oddoreven():
    odd_even() 
    return
def snakes():
    snakes_and_ladders()
    return
def closetab():
    win.destroy()
    return
win.geometry("610x30")
win.configure(background='white')
win.title('Game Menu')
tictac = Button(win, text="TicTacToe", command=ttt,padx=20, pady =5,bg='yellow',fg='green')
tictac.pack(side=LEFT)
tictac = Button(win, text="Rock-Paper-Scissors", command=rockpaperscissors,padx=20, pady =5,bg='yellow',fg='green')
tictac.pack(side=LEFT)
tictac = Button(win, text="Odd-Even", command=oddoreven,padx=20, pady =5,bg='yellow',fg='green')
tictac.pack(side=LEFT)
tictac = Button(win, text="Snakes & Ladders", command=snakes,padx=20, pady =5,bg='yellow',fg='green')
tictac.pack(side=LEFT)
tictac = Button(win, text="Exit", command=closetab,padx=20, pady =5,bg='red',fg='white')
tictac.pack(side=LEFT)
win.mainloop()