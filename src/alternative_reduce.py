#!/usr/bin/env python4

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('hashtags', nargs='+')
parser.add_argument('--type', required=True, choices=['country', 'lang'])
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

OUTPUT_DIR = "outputs"

# dataset:
# {
#   "#coronavirus": { day_of_year: total_count }
# }
data = {tag: {} for tag in args.hashtags}

for filename in sorted(os.listdir(OUTPUT_DIR)):

    # only process correct file type
    if not filename.endswith(f".{args.type}"):
        continue

    # filename format:
    # geoTwitter20-10-01.zip.country

    date_part = filename.split('.')[0].split('-')[1:]
    month = int(date_part[0])
    day = int(date_part[1])

    # convert to day-of-year
    date_obj = datetime(2020, month, day)
    day_of_year = date_obj.timetuple().tm_yday

    with open(os.path.join(OUTPUT_DIR, filename)) as f:
        counts = json.load(f)

    for tag in args.hashtags:
        if tag in counts:
            total = sum(counts[tag].values())
        else:
            total = 0

        data[tag][day_of_year] = total

# plotting
plt.figure()

for tag in args.hashtags:
    days = sorted(data[tag].keys())
    values = [data[tag][d] for d in days]
    plt.plot(days, values)

plt.xlabel("Day of Year")
plt.ylabel("Tweet Count")
plt.title("Hashtag Usage Over Time")
plt.tight_layout()

os.makedirs("map_outputs/alternative", exist_ok=True)

# clean hashtag names (remove # and unsafe characters)
clean_tags = [tag.replace("#", "") for tag in args.hashtags]

# join multiple hashtags with underscore
tag_part = "_".join(clean_tags)

output_file = f"map_outputs/alternative/{args.type}_{tag_part}_trend.png"

plt.savefig(output_file)
print(f"Saved plot to {output_file}")





