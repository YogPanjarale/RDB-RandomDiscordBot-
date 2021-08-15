import random as r
import mysql.connector as m
cur = m.connect(host='localhost',database='mgsb',user='MG',password='xxxx')
game = cur.cursor()


def adder(numbers):
    aa= "update test set coins=coins+%s where paswd ='mukund';"
    params=(numbers)
    game.execute(aa%params)
    cur.commit()