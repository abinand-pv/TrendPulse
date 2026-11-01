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

## Task 2 – Data Processing and Cleaning

### Objective
To clean and process the Hacker News data collected in Task 1 using the Pandas library.

### File Used
- Input: `data/trends_20261102.json`
- Python file: `task2_data_processing.py`
- Output: `data/trends_clean.csv`

### Libraries Used
- **Pandas:** To load, clean and process the data.
- **Glob:** To find the JSON file in the data folder.

### Data Cleaning Steps
1. Loaded the JSON file into a Pandas DataFrame.
2. Checked and removed duplicate stories using `post_id`.
3. Removed rows with missing values in `post_id`, `title`, and `score`.
4. Converted `score` and `num_comments` into integer data types.
5. Removed stories with a score below 5.
6. Removed extra spaces from story titles.
7. Saved the cleaned data as `data/trends_clean.csv`.

### Output Results

| Description | Result |
|---|---:|
| Stories loaded | 106 |
| After removing duplicates | 106 |
| After removing null values | 106 |
| After removing low scores | 101 |
| Final cleaned stories | 101 |

### Stories by Category

| Category | Stories |
|---|---:|
| Technology | 25 |
| Entertainment | 24 |
| World News | 23 |
| Science | 17 |
| Sports | 12 |

### Conclusion
Task 2 successfully cleaned the collected Hacker News data using Pandas. A total of 101 cleaned stories were saved in CSV format. This dataset will be used for further analysis in Task 3.
