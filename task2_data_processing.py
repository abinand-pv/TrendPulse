# Import required libraries
import pandas as pd
import json
import glob
import os

# Find the JSON file inside the data folder
json_files = glob.glob("data/trends_*.json")

# Check whether JSON file exists
if not json_files:
    print("JSON file not found in data folder")
else:
    json_file = json_files[0]

    # Load JSON data into Pandas DataFrame
    df = pd.read_json(json_file)

    # Print the number of rows loaded
    print("Loaded", len(df), "stories from", json_file)

    # Remove duplicate stories using post_id
    df.drop_duplicates(subset="post_id", keep="first", inplace=True)

    # Print rows remaining after removing duplicates
    print("After removing duplicates:", len(df))    

    # Remove rows with missing required values
    df.dropna(subset=["post_id", "title", "score"], inplace=True)

    # Print rows remaining after removing missing values
    print("After removing nulls:", len(df))    

    # Convert score and num_comments into integer type
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)

    print("Data types corrected successfully")

    # Remove stories with score less than 5
    df = df[df["score"] >= 5]

    # Print rows remaining after removing low scores
    print("After removing low scores:", len(df))

    # Remove extra spaces from story titles
    df["title"] = df["title"].str.strip()

    print("Extra spaces removed from titles")

    # Save cleaned data as CSV file
    output_file = "data/trends_clean.csv"
    df.to_csv(output_file, index=False)

    # Print confirmation message
    print("Saved", len(df), "rows to", output_file)

    # Display stories per category
    print("\nStories per category:")
    print(df["category"].value_counts())