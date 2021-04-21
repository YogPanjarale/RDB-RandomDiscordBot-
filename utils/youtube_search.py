import urllib.request
import urllib.parse
import re
# from metadata_parser import MetadataParser
import metadata_parser
class YotubeResult(object):
    def __init__(self,title,description,thumbnail,url) -> None:
        super().__init__()
        self.title=title
        self.description=description
        self.thumbnail = thumbnail
        self.url = url

def searchYT(term:str):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+urllib.parse.quote(term))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return list(dict.fromkeys(video_ids))
def searchYTnew(term:str):
    results = searchYT(term)[:10]
    rs = []
    for result in results:
        url = "https://www.youtube.com/results?search_query="+urllib.parse.quote(term)
        page = metadata_parser.MetadataParser(url=url)
        r = YotubeResult(page.metadata['title'],
        page.metadata['description'],
        page.metadata['og:image'],url)
        rs.append(r)
    return rs
if __name__=="__main__":
    print("Running File Directly")
    r =searchYTnew("Hello world")