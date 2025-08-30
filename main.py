import yaml
from collector import get_latest_videos
from reporter import build_report
from emailer import send_trend_email

def run():
    with open("channels.yaml", "r") as f:
        channels = yaml.safe_load(f)["channels"]

    channels_data = {}
    for ch in channels:
        name, cid = ch["name"], ch["id"]
        videos = get_latest_videos(cid)
        channels_data[name] = videos

    report = build_report(channels_data)
    print(report)  # Debug
    send_trend_email(report)

if __name__ == "__main__":
    run()
