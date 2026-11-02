# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the analysed CSV file
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it does not exist
os.makedirs("outputs", exist_ok=True)

# Display the loaded data information
print("Data loaded successfully!")
print("Dataset shape:", df.shape)
print("Total stories:", len(df))

# Chart 1: Top 10 Stories by Score

# Select the top 10 stories based on score
top_stories = df.nlargest(10, "score").copy()

# Shorten story titles to 50 characters
top_stories["short_title"] = top_stories["title"].apply(
    lambda title: title if len(title) <= 50 else title[:47] + "..."
)

# Create horizontal bar chart
plt.figure(figsize=(12, 7))

plt.barh(top_stories["short_title"], top_stories["score"])

# Add chart title and labels
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Display highest score at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Save chart before displaying it
plt.savefig("outputs/chart1_top_stories.png")

# Display chart
plt.show()

print("Chart 1 saved successfully!")

# Chart 2: Stories per Category

# Count stories in each category
category_counts = df["category"].value_counts()

# Create bar chart
plt.figure(figsize=(9, 5))

plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.Set2.colors[:len(category_counts)]
)

# Add title and labels
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()

# Save chart before displaying
plt.savefig("outputs/chart2_categories.png")

# Display chart
plt.show()

print("Chart 2 saved successfully!")

# Chart 3: Score vs Comments

# Separate popular and not popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Create scatter plot
plt.figure(figsize=(9, 6))

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)

# Add title, labels and legend
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()

# Save chart before displaying
plt.savefig("outputs/chart3_scatter.png")

plt.show()

print("Chart 3 saved successfully!")
# Bonus: TrendPulse Dashboard

# Create dashboard with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(22, 8))

# Chart 1: Top 10 Stories
axes[0].barh(top_stories["short_title"], top_stories["score"])
axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].invert_yaxis()

# Chart 2: Stories per Category
axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.Set2.colors[:len(category_counts)]
)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].tick_params(axis="x", rotation=45)

# Chart 3: Score vs Comments
axes[2].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    alpha=0.7
)
axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    alpha=0.7
)
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].legend()

# Add dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=18)

plt.tight_layout()

# Save dashboard
fig.savefig("outputs/dashboard.png")

# Display dashboard
plt.show()

print("Dashboard saved successfully!")

