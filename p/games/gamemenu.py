from tkinter import *
from ttt import tictactoe
from rps import rock_paper_scissor
from oddeven import odd_even
from sandl import snakes_and_ladders
from Obstruction import *
from hangman import *
from Game import *
from paswdgen import *
from football import *

gmenu={0:"Tictactoe is a common pen and paper game where you fill a 3x3 grid with X's and O's and win if all 3 cells of a diagonal , row or coloumn happen to contain your symbol"
,1:"Rock paper scissors is the most popular game and doesnt really need an explanation"
,2:"This game is also called hand cricket and uses different variations of hand signs as numbers (from 1 to 10), you choose to bat or ball and players get OUT if they show the same hand sign(number)"
,3:"Snake and Ladders is a game where 2 or more people play with a dice and try reaching 100 first , but in between are snakes that bring you down from your current rank and ladders that push you ahead from your current rank"
,4:"Football just like odd even also relies on hand signs (1 to 3) , if u continue getting unlike signs 3 times , u get a chance at a goal which has signs that go from 4 to 6 , if thats unlike too , its a goal , else the ball is with the opponent"
,5:"Hangman is the game with currently 1000 words , everytime u guess a letter wrong , a letter is added to 'HANGMAN' if the word is complete , u lose"
,6:"Finder is a fantasy game with exploration , store , armies , kingdoms , arena , etc"
,7:"A password creator (encrypted) and decryptor made using the arrangment of keys in the keyboard"
,8:"Obstruction is another pen and paper where the blocks around where you put symbol is occupied and the person who makes the last valid move wins"
,9:""}

def explain(number):
    gm = Tk()
    bb=gmenu[number]
    gm.geometry("300x250")
    gm.configure(background='grey')
    gm.title('Game Info')
    explainer = Label(gm,text =f"{bb}").place(x = 100,y = 100)
    explainer.pack()
    gm.mainloop()
explain(4)
def ttt():
    tictactoe()
    explain(0)
def rockpaperscissors():
    rock_paper_scissor() 
    explain(1)
def oddoreven():
    odd_even() 
    explain(2)
def snakes():
    snakes_and_ladders()
    explain(3)
def f():
    fb()  
    explain(4)
def hm():
    hang() 
    explain(5)
def finders():
    explain(6)
    find() 
def encryptors():
    encr()
    explain(7)
def ob():
    obstr()
    explain(8)
def l():
    #ludo()
    print("ludo to be added later")
    explain(9)
def gamemenu():
    win = Tk()
    win.geometry("930x100")
    win.configure(background='grey')
    win.title('Game Menu')
    tictac = Button(win, text="TicTacToe", command=ttt,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 50 , y = 12)
    tictac = Button(win, text="Rock-Paper-Scissors", command=rockpaperscissors,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 200, y = 12)
    tictac = Button(win, text="Odd-Even", command=oddoreven,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 420 , y = 12)
    tictac = Button(win, text="Snakes & Ladders", command=snakes,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 570 , y = 12)
    tictac = Button(win, text="Football", command=f,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 780 , y = 12)
    tictac = Button(win, text="Hangman", command=hm,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 50, y = 60)
    tictac = Button(win, text="Obstruction", command=ob,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 230 , y = 60)
    tictac = Button(win, text="Finder", command=find,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 430 , y = 60)
    tictac = Button(win, text="Encryptor", command=encryptors,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 595 , y = 60)
    tictac = Button(win, text="Ludo", command=l,padx=20, pady =5,bg='yellow',fg='green')
    tictac.place(x = 790 , y = 60)
    win.mainloop()
gamemenu()