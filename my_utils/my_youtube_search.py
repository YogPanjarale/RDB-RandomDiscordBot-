import json
from discord import raw_models
from youtube_search import YoutubeSearch

'''
 {
        "channel": "Samuel Miller",
        "duration": "1:00",
        "id": "dthvgrxVh5Y",
        "long_desc": "#Shorts #YouTubeShorts.",
        "publish_time": "5 days ago",
        "thumbnails": [
            "https://i.ytimg.com/vi/dthvgrxVh5Y/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBkFp3YSvtn5or9Ov3Llpzh_hrb8w",
            "https://i.ytimg.com/vi/dthvgrxVh5Y/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCYPFWn81O5fHM5QXMiJKgfBGkSRw"   
        ],
        "title": "When programming languages print \"Hello World\"",
        "url_suffix": "/watch?v=dthvgrxVh5Y",
        "views": "39,131 views"
    },
'''


class YoutubeResult(object):
    def __init__(self, item, title: str = '', description: str = '', thumbnail: str = '', url: str = '', views: int = '', publish_time: str = '', duration: str = '', channel: str = '') -> None:
        title = item['title'],
        description = item['long_desc'],
        if description == None:
            description = "None"
        thumbnail = item['thumbnails'][0],
        url = "https://youtube.com"+item['url_suffix'],
        views = item['views']
        publish_time = item['publish_time']
        duration = item['duration']
        channel = item['channel']
        channel_id = item['id']
        super().__init__()
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.url = url
        self.views = views
        self.publish_time = publish_time
        self.duration = duration
        self.channel = channel
        self.id = channel_id

    def to_dict(self,):
        return {
            "title": self.title,
            "description": self.description,
            "thumbnail": self.thumbnail,
            "url": self.url,
            "id": self.id,
            "views": self.views,
            "publish_time": self.publish_time,
            "duration": self.duration,
            "channel": self.channel
        }


def searchYT(term: str, max_result: int = 10):
    results = YoutubeSearch(term, max_results=max_result).to_dict()
    result_list = []
    for item in results:
        ys = YoutubeResult(
            item=item
        )
        r = json.dumps(ys.to_dict(), indent=4, sort_keys=True)
        # print(r)
        result_list.append(ys)
    return result_list


if __name__ == "__main__":
    print("Running File Directly")
    r = searchYT("Hello world")
    for i in r:
        print(json.dumps(i.to_dict(), indent=4, sort_keys=True))
