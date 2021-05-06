from tinydb import TinyDB,Query
db = TinyDB('./db.json')

def addCC(name:str,description:str):
    db.insert({"name":name,"description":description})
    print(db.all())
    print(f"Command with name : {name}, and description : {description} Added")
    pass