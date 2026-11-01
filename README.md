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

## Task 3 – Data Analysis using Pandas and NumPy

### Objective
To analyse the cleaned Hacker News data using Pandas and NumPy and identify important trends and patterns.

### File Used
- Input: `data/trends_clean.csv`
- Python file: `task3_analysis.py`
- Output: `data/trends_analysed.csv`

### Libraries Used
- **Pandas:** To load and analyse the CSV data.
- **NumPy:** To calculate statistical values.

### Analysis Performed
1. Loaded the cleaned CSV file.
2. Displayed the first five rows and dataset shape.
3. Calculated average score and average comments.
4. Calculated mean, median, standard deviation, maximum and minimum scores.
5. Identified the category with the most stories.
6. Found the story with the highest number of comments.

### Statistical Results

| Analysis | Result |
|---|---:|
| Total stories | 101 |
| Mean score | 158.72 |
| Median score | 71 |
| Standard deviation | 354.21 |
| Maximum score | 3300 |
| Minimum score | 5 |
| Most stories category | Technology (25) |
| Highest comments | 1091 |

### New Columns Added
- **engagement:** Calculated using `num_comments / (score + 1)`.
- **is_popular:** Returns True when a story's score is greater than the average score; otherwise False.

### Output
The analysed dataset was saved successfully as `data/trends_analysed.csv` with 101 rows and 9 columns.

### Conclusion
Task 3 successfully analysed the cleaned Hacker News dataset using Pandas and NumPy. Statistical values, popular categories and highly commented stories were identified. Two new columns were added for further analysis. The final dataset is ready for Task 4 visualization.
