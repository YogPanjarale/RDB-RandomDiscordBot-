from tkinter import *
from functools import partial


import mysql.connector as msc
cool = msc.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
elic = cool.cursor()
print("LOGIN")
login = '''select name from admin;'''
elic.execute(login)
log = elic.fetchall()
print(log)
tkWindow = Tk()  
def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    tkWindow.mainloop()
    return
logins = input("would you like to login or create a new user?:\nUse 'login' for logging in a user or use 'new' for adding yourself as a new user\n")
for i in logins:
    if 'login' in logins:
        #window
        
        tkWindow.geometry('270x80')  
        tkWindow.title('ELIC LOGIN')

        #username label and text entry box
        usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

        #password label and password entry box
        passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

        validateLogin = partial(validateLogin, username, password)

        #login button
        loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

        tkWindow.mainloop()
        names = f'''select name from admin where name = "{username.get()}";'''
        elic.execute(names)
        l = elic.fetchall()
        a = list(l)
        b = str(a).replace("[","")
        c=str(b).replace(']','')
        d = str(c).replace(',','')
        e=str(d).replace("'","")
        f=str(e).replace('(',"")
        g = str(f).replace(')','')
        if g==username.get():
            paswd = f'''select nameid from admin where name = "{username.get()}";'''
            elic.execute(paswd)
            ll = elic.fetchall()
            aa = list(ll)
            bb = str(aa).replace("[","")
            cc=str(bb).replace(']','')
            dd = str(cc).replace(',','')
            ee=str(dd).replace("'","")
            ff=str(ee).replace('(',"")
            gg = str(ff).replace(')','')
            for i in password.get():
                if gg==password.get():
                    print(f"welcome back {g}")
                    break
                else:
                    print('incorrect password')
                    break
            break
    elif 'new' in logins:
        newname= input("enter your name, this is what the system will remember u as:\n")
        newpas=input("for security we need u to add a password too (min=5,max=10):\n")
        newuser=f'''insert into admin (name,nameid) values("{newname}","{newpas}");'''
        elic.execute(newuser)
        cool.commit()
        print(f"new user {newname} has been created")
        break
cool.close()
