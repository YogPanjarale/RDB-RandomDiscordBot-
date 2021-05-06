from tinydb import TinyDB,Query

db:TinyDB

def initDB(path):
    db=TinyDB(path)