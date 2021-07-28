from os import name
from tinydb import TinyDB
from datetime import datetime, time
from dataclasses import dataclass
from tinydb.queries import Query
import json
db: TinyDB = TinyDB("./newsdb.json")
q: Query = Query()


@dataclass
class NewsObject():
    title: str
    description: str
    added_by: str
    time_created: str = datetime.now().ctime()
    timestamp: str = datetime.now().__str__()

    def tojson(self):
        return {"title": self.title, "description": self.description, "added_by": self.added_by, "time_created": self.time_created, "timestamp": self.timestamp, }


ListOfNewsType = [NewsObject(
    title="news title", description="news Description", added_by="Yog")]


def addNews(n: NewsObject):
    db.insert(n.tojson())
    # n.
    print(
        f"News Added by {n.added_by} at time : {n.time_created}.\nTitle : {n.title} ; description : {n.description}")


def getAllNews() -> ListOfNewsType:
    r = db.all()
    r1 = []
    for i in r:
        r1.append(NewsObject(**i))
    print("Searched for all news got {} news".format(len(r1)))
    return r1

if __name__=="__main__":
    addNews(NewsObject(title="news 1",description="td1",added_by="yog"))
    addNews(NewsObject(title="news 2",description="td2",added_by="yog"))
    addNews(NewsObject(title="news 3",description="td3",added_by="yog"))
    r=getAllNews()
    print(r)
