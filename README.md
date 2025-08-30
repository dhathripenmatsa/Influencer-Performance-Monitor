# 🎯 Influencer Performance Monitor

**A Python-based tool to track YouTube influencer performance and send automated email reports for marketers.** 📊📧

---

## 📝 Project Overview

Influencer Monitor helps brand teams and marketers monitor YouTube influencers by collecting key metrics:

- 👀 Views, 👍 Likes, 💬 Comments  
- 📈 Engagement Rate (% of audience interacting with content)  
- 🧑‍🤝‍🧑 Subscriber Count (channel reach)  
- ⏱ Video Duration and 📂 Category  
- 🔗 Sponsorship/Link Presence  
- ⭐ Top-performing video highlight  
- 🆕 Recent video performance  

The tool automatically **sends a styled email report once a week** summarizing all key metrics for selected influencers .

---

## ✨ Key Features

- ✅ Fetch latest videos from multiple YouTube channels  
- ✅ Calculate engagement metrics  
- ✅ Highlight top-performing videos  
- ✅ Detect links or sponsorships in video descriptions  
- ✅ Send automated HTML email reports  
- ✅ Configurable channel list via `channels.yaml`  

---

## 📂 Project Structure

Influencer_Monitor/
- │── .env # 🔐 API keys and email credentials
- │── channels.yaml # 📋 List of influencer channels
- │── collector.py # 📡 Fetches data from YouTube API
- │── reporter.py # 📝 Generates email report
- │── emailer.py # 📧 Sends emails
- │── main.py # 🚀 Entry point
- │── requirements.txt # 📦 Python dependencies
- │── Procfile # 🖥 For Heroku deployment
- |── summarizer

## 👩‍💻 Author

**dhathripenmatsa**

