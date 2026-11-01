# Import required libraries
import pandas as pd
import numpy as np

# Load the cleaned CSV file
df = pd.read_csv("data/trends_clean.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display the number of rows and columns
print("\nLoaded data:", df.shape)

# Calculate average score and comments
print("\nAverage score   :", df["score"].mean())
print("Average comments:", df["num_comments"].mean())

# Calculate statistics using NumPy
scores = df["score"].to_numpy()

print("\n--- NumPy Stats ---")

# Calculate mean, median and standard deviation
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))

# Find highest and lowest scores
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# Find the category with the most stories
category_count = df["category"].value_counts()
print("\nMost stories in:", category_count.idxmax(),
      "(", category_count.max(), "stories )")

# Find the story with the most comments
most_commented = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:",
      most_commented["title"],
      "—", most_commented["num_comments"], "comments")

# Calculate engagement for each story
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Mark stories as popular if score is above average
average_score = df["score"].mean()
df["is_popular"] = df["score"] > average_score

# Display the new columns
print("\n--- New Columns ---")
print(df[["title", "engagement", "is_popular"]].head())

# Save the analysed data into a new CSV file
output_file = "data/trends_analysed.csv"

df.to_csv(output_file, index=False)

# Print confirmation message
print("\nSaved successfully to", output_file)
print("Total rows saved:", len(df))