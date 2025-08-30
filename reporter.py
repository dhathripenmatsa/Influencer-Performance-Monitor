def build_report(channels_data):
    report = """
    <html>
    <head>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.5; }
        h1, h2, h3 { color: #2F4F4F; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even){background-color: #f2f2f2;}
        .yes { color: green; font-weight: bold; }
        .no { color: red; font-weight: bold; }
        .summary { background-color: #f9f9f9; padding: 10px; margin-bottom: 15px; border: 1px solid #ddd; }
        .metric { font-weight: bold; }
        .highlight { background-color: #fff3cd; padding: 10px; border-left: 5px solid #ffc107; margin-bottom: 15px; }
    </style>
    </head>
    <body>
    <h1>📊 Influencer Trend Brief</h1>
    """

    for channel, videos in channels_data.items():
        if not videos:
            report += f"<h2>⚠️ No data for {channel}</h2>"
            continue

        subs = videos[0].get("subs", 0)
        try:
            subs_str = f"{int(subs):,}"
        except (ValueError, TypeError):
            subs_str = "Unknown"

        # Calculate average views and engagement
        total_views = sum(v.get("views", 0) for v in videos)
        total_engagement = sum(v.get("engagement", 0) for v in videos)
        avg_views = total_views // len(videos) if videos else 0
        avg_engagement = round(total_engagement / len(videos), 2) if videos else 0
        last_upload = max(v.get("published", "Unknown") for v in videos)

        # Top Performing Video
        top_video = max(videos, key=lambda x: x.get("engagement", 0))

        report += f"<h2>{channel}</h2>"

        # Summary Section
        # Inside the loop for each channel in build_report()

        channel_url = f"https://www.youtube.com/channel/{videos[0].get('id', '')}"

# Summary Section
        report += f"""
        <div class="summary">
            <p><span class="metric">Subscribers:</span> {subs_str}</p>
            <p><span class="metric">Average Views (last {len(videos)} videos):</span> {avg_views:,}</p>
            <p><span class="metric">Average Engagement Rate:</span> {avg_engagement}%</p>
            <p><span class="metric">Last Upload:</span> {last_upload}</p>
            <p><span class="metric">Total Videos Monitored:</span> {len(videos)}</p>
            <p><span class="metric">Channel Link:</span> <a href="https://www.youtube.com/channel/{id}" target="_blank">{channel}</a></p>
        </div>
        """


        # Highlight Top Performing Video
        report += f"""
        <div class="highlight">
            <h3>🏆 Top Performing Video</h3>
            <p><strong>Title:</strong> {top_video.get('title', 'Untitled')}</p>
            <p><strong>Published:</strong> {top_video.get('published', 'Unknown')}</p>
            <p><strong>Views:</strong> {top_video.get('views', 0):,} | <strong>Likes:</strong> {top_video.get('likes', 0):,} | <strong>Comments:</strong> {top_video.get('comments', 0):,}</p>
            <p><strong>Engagement Rate:</strong> {top_video.get('engagement', 0)}%</p>
            <p><strong>Duration:</strong> {top_video.get('duration', 'Unknown')} | <strong>Category:</strong> {top_video.get('category', 'Unknown')}</p>
            <p><strong>Sponsorship Links:</strong> {'✅ Yes' if top_video.get('has_links', False) else '❌ No'}</p>
            <p><strong>Summary:</strong> {top_video.get('description', '')}</p>
        </div>
        """

        # Table for Recent Videos
        report += "<h3>Recent Videos</h3>"
        report += """
        <table>
            <tr>
                <th>Title</th>
                <th>Published</th>
                <th>Views</th>
                <th>Likes</th>
                <th>Comments</th>
                <th>Engagement %</th>
                <th>Duration</th>
                <th>Category</th>
                <th>Sponsorship Links</th>
                <th>Summary</th>
            </tr>
        """
        for v in videos:
            views = v.get("views", 0)
            likes = v.get("likes", 0)
            comments = v.get("comments", 0)
            engagement = v.get("engagement", 0)
            duration = v.get("duration", "Unknown")
            category = v.get("category", "Unknown")
            has_links = v.get("has_links", False)
            description = v.get("description", "")

            report += f"""
            <tr>
                <td>{v.get('title', 'Untitled')}</td>
                <td>{v.get('published', 'Unknown')}</td>
                <td>{views:,}</td>
                <td>{likes:,}</td>
                <td>{comments:,}</td>
                <td>{engagement}%</td>
                <td>{duration}</td>
                <td>{category}</td>
                <td class="{ 'yes' if has_links else 'no' }">{ 'Yes' if has_links else 'No' }</td>
                <td>{description}</td>
            </tr>
            """
        report += "</table>"

    report += "</body></html>"
    return report



