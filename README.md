# TrendPulse

## Hacker News Trending Data Collection using Python

### Project Description
TrendPulse is a Python-based project that collects trending stories from the Hacker News API and categorizes them into five categories.

### Task 1 – Data Collection
- Fetches the top 500 Hacker News story IDs.
- Collects story details using the Hacker News API.
- Categorizes stories into Technology, World News, Sports, Science, and Entertainment.
- Collects up to 25 stories per category.
- Saves the collected data in JSON format.

### Technologies Used
- Python
- Requests
- JSON
- Hacker News API

### Project Structure
- `task1_data_collection.py` – Data collection program
- `data/trends_20261102.json` – Collected dataset
- `requirements.txt` – Required Python package

### How to Run
Install the required package:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python task1_data_collection.py
```


### Output
The program successfully collected 106 categorized stories and saved them as a JSON file.

### Data Source
[Hacker News API](https://github.com/HackerNews/API)
