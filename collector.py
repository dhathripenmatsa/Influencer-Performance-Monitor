import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YT_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing YT_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)


def get_channel_stats(channel_id):
    """Fetch channel subscriber count + upload playlist ID safely"""
    request = youtube.channels().list(
        part="statistics, contentDetails",
        id=channel_id
    )
    response = request.execute()
    if not response.get("items"):
        return 0, None  # No data

    stats = response["items"][0].get("statistics", {})
    subs = int(stats.get("subscriberCount", 0) or 0)

    uploads_id = response["items"][0].get("contentDetails", {}) \
        .get("relatedPlaylists", {}) \
        .get("uploads")

    return subs, uploads_id


def get_latest_videos(channel_id, max_results=5):
    """Fetch latest videos with engagement metrics safely"""
    subs, uploads_id = get_channel_stats(channel_id)
    if not uploads_id:
        return []

    request = youtube.playlistItems().list(
        part="snippet, contentDetails",
        playlistId=uploads_id,
        maxResults=max_results
    )
    playlist = request.execute()

    videos = []
    for item in playlist.get("items", []):
        video_id = item.get("contentDetails", {}).get("videoId")
        if not video_id:
            continue

        title = item.get("snippet", {}).get("title", "Untitled")
        published = item.get("contentDetails", {}).get("videoPublishedAt", "Unknown")
        description = item.get("snippet", {}).get("description", "")

        vid_req = youtube.videos().list(
            part="statistics, contentDetails, snippet",
            id=video_id
        )
        vid_res = vid_req.execute()
        if not vid_res.get("items"):
            continue

        vdata = vid_res["items"][0]
        stats = vdata.get("statistics", {})

        views = int(stats.get("viewCount", 0) or 0)
        likes = int(stats.get("likeCount", 0) or 0)
        comments = int(stats.get("commentCount", 0) or 0)
        engagement = round(((likes + comments) / views * 100), 2) if views > 0 else 0
        duration = vdata.get("contentDetails", {}).get("duration", "Unknown")
        category = vdata.get("snippet", {}).get("categoryId", "Unknown")
        has_links = "http" in description.lower()

        videos.append({
            "id": video_id,
            "title": title,
            "published": published,
            "views": views,
            "likes": likes,
            "comments": comments,
            "engagement": engagement,
            "duration": duration,
            "category": category,
            "subs": subs,
            "has_links": has_links,
            "description": description[:150] + "..." if len(description) > 150 else description,
            "recent": True
        })

    return videos
