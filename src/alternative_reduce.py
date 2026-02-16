#!/usr/bin/env python3

# -----------------------------
# Command line arguments
# -----------------------------
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True,
                    help='List of JSON files to include in the plot')
parser.add_argument('--keys', nargs='+', required=True,
                    help='Hashtags to track')
args = parser.parse_args()

# -----------------------------
# Imports
# -----------------------------
import os
import json
from collections import defaultdict
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # no GUI
import matplotlib.pyplot as plt

# -----------------------------
# Aggregate data
# -----------------------------
# Structure: total[hashtag][day_of_year] = total count
total = defaultdict(lambda: defaultdict(int))

for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)

    # Extract date from filename (assumes format geoTwitterYY-MM-DD.zip.*)
    filename = os.path.basename(path)
    year = 2020  # all tweets are from 2020
    month = int(filename.split('-')[1])
    day = int(filename.split('-')[2].split('.')[0])
    day_of_year = datetime(year, month, day).timetuple().tm_yday

    # Sum counts for each requested hashtag
    for k in args.keys:
        if k in tmp:
            total[k][day_of_year] += sum(tmp[k].values())

# -----------------------------
# Plotting
# -----------------------------
plt.figure(figsize=(10,6))

for hashtag in args.keys:
    days = sorted(total[hashtag].keys())
    values = [total[hashtag][d] for d in days]
    plt.plot(days, values, label=hashtag)

plt.xlabel('Day of Year')
plt.ylabel('Tweet Count')
plt.title('Hashtag Trends Over 2020')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()

# -----------------------------
# Save output
# -----------------------------
os.makedirs("map_outputs", exist_ok=True)

# Build descriptive filename from hashtags
clean_tags = [h.replace("#", "") for h in args.keys]
filename = f"map_outputs/hashtags_{'_'.join(clean_tags)}_trend.png"

plt.savefig(filename)
print(f"Saved plot to {filename}")

