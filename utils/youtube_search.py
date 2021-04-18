from googleapiclient.discovery import build
from dotenv import dotenv_values

def get_service():
    # Get developer key from "credentials" tab of api dashboard
    return build("youtube", "v3", developerKey="key")

def search(term, channel):
    service = get_service()
    resp = service.search().list(
        part="id",
        q=term,
        # safeSearch="none" if channel.is_nsfw() else "moderate",
        videoDimension="2d",
        ).execute()
    return resp["items"][0]["id"]["videoId"]