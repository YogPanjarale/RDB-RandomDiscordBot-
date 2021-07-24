import mysql.connector
  
  
db = mysql.connector.connect(host='localhost',
                        database='mgsb',
                        user='MG',
                        password='mg@123',
                        )

mg = db.cursor()
helpcommands = '''create table help(
                Cnames varchar(10) not null,
                Cdesc varchar (60) not null
                )'''
mg.execute(helpcommands)
db.close()

