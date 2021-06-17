from os import name
from typing import List, Union
from tinydb import TinyDB,Query
import datetime;
from dataclasses import dataclass
# db:TinyDB = TinyDB('./cc_db.json')
q=Query()
def serverDb(serverId:str)->TinyDB:
    return TinyDB(f'./cc_db/{serverId}.json')
@dataclass()
class ResponseCC():
    name:str
    description:str
    user:str
    time_created:str

listOfResponse = [ResponseCC(name="",description="",user="",time_created="")]
def addCC(serverID:str,name:str,description:str,user:str):
    db = serverDb(serverId=serverID)
    d = datetime.datetime.now()
    timeCreated = d.ctime()
    db.insert({"name":name,"description":description,"user":user,"time_created":timeCreated})
    # print(db.all())
    print(f"Command with name : {name}, and description : {description} Added, by user {user}")
    pass
def searchCC(serverID:str,name:str)->Union[ResponseCC,None]:
    db = serverDb(serverId=serverID)
    print(f"Searching for {name}")
    result=db.search(q.name ==name)
    # print(result)
    if len(result)>0:
        return result[0]
    pass
# v = list[dict]
def searchCCByUser(serverID:str,user:str)->listOfResponse:
    db = serverDb(serverId=serverID)
    print(f"Searching for CC made by user {user}")
    result=db.search(q.user ==user)
    # print(result)
    return result
def deleteCCbyName(serverID:str,name:str,user:str)->str:
    db = serverDb(serverId=serverID)
    r= searchCC(serverId=serverID,name=name)
    if(r):
        if r.user == user:
            db.remove(q.name==name)
            print(f"Deleting CC {name} made by {user} ")
            return "Done"
        return f"CC {name} was not created by {user} not same"
    return "CC not found"
def updateCCnameByName(serverID:str,name:str,newName:str,user:str)->str:
    db = serverDb(serverId=serverID)
    r= searchCC(serverId=serverID,name=name)
    if(r):
        if r.user == user:
            #TODO check if new name already exists
            db.update({"name":newName},q.name == name)
            print(f"Updating CC {r.name} made by {name} to {newName} ")
            return "Done"
        return f"CC {name} was not created by {user} not same"
    return "CC not found"
def updateCCdescriptionByName(serverID:str,name:str,newDescription:str,user:str)->str:
    db = serverDb(serverId=serverID)
    r= searchCC(serverId=serverID,name=name)
    if(r):
        if r.user == user:
            db.update({"description":newDescription},q.name == name)
            print(f"Updating CC {r.name} made by {name} to {newDescription} ")
            return "Done"
        return f"CC {name} was not created by {user} not same"
    return "CC not found"
    # if ( )

def getAllCC(serverID:str)->listOfResponse:
    db = serverDb(serverId=serverID)
    result = db.all()
    print(f"Getting all CC ", f"total {len(result)+1}")
    return result