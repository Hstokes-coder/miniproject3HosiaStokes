# Mini Project 3: NFL Team Scoring Analysis

## Project Question

Which NFL team scored the most total points in a regular season?

## Dataset Used

`spreadspoke_scores.csv` — a historical NFL game-by-game dataset covering
regular season and playoff games from 1966 to 2025. Each row is one game and
includes the season, week, home team, away team, home score, away score, and
whether the game was a playoff game.

## Tools / Libraries Used

- Python 3
- pandas
- matplotlib

## What the Code Does

`nfl_points.py` answers the project question in a few steps:

1. **Load the data.** Reads `spreadspoke_scores.csv` into a DataFrame.
2. **Filter out playoff games.** Keeps only rows where `schedule_playoff` is
   `False`, since the question is about regular-season scoring.
3. **Combine home and away scoring into one table.** In the raw data, a
   team's points are split across two columns (`score_home` and
   `score_away`) depending on whether they played at home or away. The
   script splits the data into a "home" table and an "away" table, renames
   their columns to the same names (`season`, `team`, `points`), and stacks
   them into one long table called `team_points` with one row per team per
   game.
4. **Group by season and team.** Uses `groupby(['season', 'team'])['points'].sum()`
   to add up every team's points within each season, producing one total
   per team per year.
5. **Find the top 10.** Sorts those season totals from highest to lowest and
   keeps the top 10.
6. **Print basic statistics.** Uses `.describe()` on all team-season totals
   to summarize the full distribution (count, mean, std, min, quartiles, max).
7. **Create and save a bar chart.** Plots the top 10 team-seasons as a bar
   chart and saves it as `charts/top_10_nfl_scoring.png`.

## Main Result

The **2013 Denver Broncos** scored the most points of any team in a single
regular season, with **606 total points**.

## Top 10 Highest-Scoring Regular Seasons

| Season | Team | Total Points |
|---|---|---:|
| 2013 | Denver Broncos | 606 |
| 2007 | New England Patriots | 589 |
| 2018 | Kansas City Chiefs | 565 |
| 2024 | Detroit Lions | 564 |
| 2011 | Green Bay Packers | 560 |
| 2012 | New England Patriots | 557 |
| 1998 | Minnesota Vikings | 556 |
| 2011 | New Orleans Saints | 547 |
| 1983 | Washington Redskins | 541 |
| 2000 | St. Louis Rams | 540 |

## Summary of Basic Statistics

Across all 1,770 team-seasons in the dataset:

- **Average (mean) points per team per season:** ~329.5
- **Standard deviation:** ~76.6
- **Minimum:** 103 points
- **25th percentile:** 278 points
- **Median (50th percentile):** 326 points
- **75th percentile:** 379 points
- **Maximum:** 606 points

The 2013 Broncos' 606 points is well above the typical range, showing just
how historic that scoring season was compared to a normal team-season.

## Chart

Running the program generates the chart at `charts/top_10_nfl_scoring.png`.

## How to Run This Project

1. Make sure Python 3 is installed, along with pandas and matplotlib:
   ```
   python3 -m pip install -r requirements.txt
   ```
2. Keep `nfl_points.py` and `spreadspoke_scores.csv` in the same folder.
3. Run the script:
   ```
   python3 nfl_points.py
   ```
4. The script will print the first few rows of data, the top 10
   highest-scoring team-seasons, and the basic statistics to the console. It
   will also display the bar chart and save it as `charts/top_10_nfl_scoring.png`.


## AI Usage

Claude Code was used as a debugging and learning assistant during development. It helped identify and fix Python errors, verify that the renamed CSV file matched the filename used in the script, explain Pandas methods such as `groupby()` and `.describe()`, and check that the chart output and file paths were working correctly. Claude Code was also used to review parts of the README for consistency with the finished project. The code and results were reviewed and tested before submission.
