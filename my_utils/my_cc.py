from tinydb import TinyDB,Query
import datetime;
db = TinyDB('./db.json')
q=Query()
def addCC(name:str,description:str,user:str):
    d = datetime.datetime.now()
    timeCreated = d.ctime()
    db.insert({"name":name,"description":description,"user":user,"time-created":timeCreated})
    # print(db.all())
    print(f"Command with name : {name}, and description : {description} Added, by user {user}")
    pass
def searchCC(name:str):
    print(f"Searching for {name}")
    result=db.search(q.name ==name)
    # print(result)
    if len(result)>0:
        return result[0]
    pass
# v = list[dict]
def searchCCByUser(user:str):
    print(f"Searching for CC made by user {user}")
    result=db.search(q.user ==user)
    # print(result)
    return result
def getAllCC():
    result = db.all()
    print(f"Getting all CC ", f"total {len(result)+1}")
    return result