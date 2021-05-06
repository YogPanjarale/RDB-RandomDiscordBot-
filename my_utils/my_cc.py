from tinydb import TinyDB,Query
db = TinyDB('./db.json')
q=Query()
def addCC(name:str,description:str):
    db.insert({"name":name,"description":description})
    print(db.all())
    print(f"Command with name : {name}, and description : {description} Added")
    pass
def searchCC(name:str):
    print(f"Searching for {name}")
    result=db.search(q.name ==name)
    print(result)
    if len(result)>0:
        return result[0]
    pass