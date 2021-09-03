import mysql.connector as msc
cool = msc.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
elic = cool.cursor()
names = '''select name from admin;'''
elic.execute(names)
l = elic.fetchall()
print(l)
newname= input("enter your name, this is what the system will remember u as:\n")
newpas=input("for security we need u to add a password too (min=5,max=10):\n")
newuser=f'''insert into admin (name,nameid) values("{newname}","{newpas}");'''
elic.execute(newuser)
cool.commit()
print(f"new user {newname} has been created")
print(l)
