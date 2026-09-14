import pandas as pd
import matplotlib.pyplot as plt

# Load the NFL dataset
df = pd.read_csv("spreadspoke_scores.csv")

# Keep only regular-season games
df = df[df['schedule_playoff'] == False]

# Show the first 5 rows
print(df.head())

# Home-team scoring data
home = df[['schedule_season', 'team_home', 'score_home']].rename(
    columns={
        'schedule_season': 'season',
        'team_home': 'team',
        'score_home': 'points'
    }
)

# Away-team scoring data
away = df[['schedule_season', 'team_away', 'score_away']].rename(
    columns={
        'schedule_season': 'season',
        'team_away': 'team',
        'score_away': 'points'
    }
)

# Combine home and away scoring into one table
team_points = pd.concat([home, away], ignore_index=True)

# Add up points for each team in each season
season_totals = team_points.groupby(
    ['season', 'team']
)['points'].sum()

# Sort from highest to lowest
top_10 = season_totals.sort_values(
    ascending=False
).head(10)

print("\nTop 10 highest-scoring regular seasons:")
print(top_10)

# Basic statistics
print("\nBasic statistics for team-season point totals:")
print(season_totals.describe())

# Make a bar chart of the top 10
top_10.plot(kind="bar")

plt.title("Top 10 Highest-Scoring NFL Regular Seasons")
plt.xlabel("Season and Team")
plt.ylabel("Total Points")
plt.tight_layout()

# Save the graph as an image
plt.savefig("top_10_nfl_scoring.png", bbox_inches="tight")

# Show the graph
plt.show()