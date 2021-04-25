import json
from youtube_search import YoutubeSearch

class YoutubeResult(object):
    def __init__(self,title:str,description:str,thumbnail:str,url:str,views:int) -> None:
        super().__init__()
        self.title=title
        self.description=description
        self.thumbnail = thumbnail
        self.url = url
        self.views= views
    def to_dict(self,):
        return {
            "title": self.title,
            "description":self.description,
            "thumbnail":self.thumbnail,
            "url":self.url,
            "views":self.views
        }

def searchYT(term:str):
    results = YoutubeSearch(term,max_results=5).to_dict();
    result_list=[]
    for item in results:
        ys = YoutubeResult(
            title=item['title'],
            description=item['long_desc'],
            thumbnail=item['thumbnails'][0],
            url="https://youtube.com"+item['url_suffix'],
            views=item['views']
        )
        result_list.append(ys)
    return result_list
if __name__=="__main__":
    print("Running File Directly")
    r =searchYT("Hello world")
    for i in r:
        print(json.dumps(i.to_dict(), indent=4, sort_keys=True))