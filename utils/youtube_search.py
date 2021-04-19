import urllib.request
import urllib.parse
import re

def searchYT(term:str):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+urllib.parse.quote(term))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return list(dict.fromkeys(video_ids))