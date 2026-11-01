# Import required libraries
import requests
import time
import os
import json
from datetime import datetime
# Set User-Agent header for API requests
headers = {
    "User-Agent": "TrendPulse/1.0"
}
# Fetch top 500 story IDs from Hacker News API
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, headers=headers, timeout=10)

print(response.status_code)

story_ids = response.json()

print("Total Story IDs:", len(story_ids))

# Select the first 500 story IDs
story_ids = story_ids[:500]

all_stories = []
# Fetch individual story details from Hacker News
for index, story_id in enumerate(story_ids):

    print(f"Fetching story {index + 1}/{len(story_ids)}...", flush=True)

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        response = requests.get(
            story_url,
            headers=headers,
            timeout=(3, 8)
        )

        response.raise_for_status()

        story = response.json()

        if story and story.get("title"):
            all_stories.append(story)

    except (requests.RequestException, ValueError) as e:
        print("Failed:", story_id, e)

print("Total Stories Fetched:", len(all_stories))
# Define categories and matching keywords
categories = {
    "technology": ["AI", "software", "tech", "code", "computer",
                   "data", "cloud", "API", "GPU", "LLM"],

    "worldnews": ["war", "government", "country", "president",
                  "election", "climate", "attack", "global"],

    "sports": [
    "NFL", "NBA", "FIFA", "sport", "game",
    "team", "player", "league", "championship",
    "football", "basketball", "cricket", "tennis",
    "soccer", "Olympics", "athlete", "tournament",
    "match", "coach", "hockey"
],

    "science": [
    "research", "study", "space", "physics",
    "biology", "discovery", "NASA", "genome",
    "scientist", "scientific", "experiment",
    "astronomy", "quantum", "planet", "telescope",
    "genetic", "laboratory", "climate"
],

    "entertainment": ["movie", "film", "music", "Netflix",
                      "game", "book", "show", "award", "streaming"]
}
# Create an empty list for each category
category_stories = {category: [] for category in categories}
# Categorize stories and collect required fields
for story in all_stories:

    title = story.get("title", "").lower()

    for category, keywords in categories.items():

        if any(word.lower() in title for word in keywords):

            if len(category_stories[category]) < 25:

                record = {
                    "post_id": story.get("id"),
                     "title": story.get("title"),
                     "category": category,
                     "score": story.get("score", 0),
                     "num_comments": story.get("descendants", 0),
                     "author": story.get("by", "unknown"),
                     "collected_at": datetime.now().isoformat()
                }

                category_stories[category].append(record)

                break

# Display category-wise story counts
for index, (category, stories) in enumerate(category_stories.items()):

    print(category, ":", len(stories))

    # Wait 2 seconds between categories
    if index < len(category_stories) - 1:
        time.sleep(2)

# Combine all categorized stories
collected_stories = []

for category, stories in category_stories.items():
    collected_stories.extend(stories)

# Create data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Generate JSON filename using the current date
filename = datetime.now().strftime("trends_%Y%m%d.json")
filepath = os.path.join("data", filename)

# Save collected stories into JSON file
with open(filepath, "w", encoding="utf-8") as file:
    json.dump(collected_stories, file, indent=4, ensure_ascii=False)

print("Total Collected Stories:", len(collected_stories))
print("JSON file saved successfully:", filepath)
