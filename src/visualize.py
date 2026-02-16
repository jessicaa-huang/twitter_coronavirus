#!/usr/bin/env python4

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort high → low first
items = sorted(counts[args.key].items(), key=lambda item: item[1], reverse=True)

# take top 10
top_items = items[:10]

# now sort low → high for plotting
top_items = sorted(top_items, key=lambda item: item[1])

keys = [k for k, v in top_items]
values = [v for k, v in top_items]

plt.figure()
plt.bar(keys, values)
plt.xlabel("Keys")
plt.ylabel("Values")
plt.title(f"{args.key} distribution")

plt.xticks(rotation=45)
plt.tight_layout()

# create filename automatically
# make sure output directory exists
os.makedirs("map_outputs", exist_ok=True)

# get just "country" or "lang" from "combined.country"
input_name = os.path.basename(args.input_path).replace("combined.", "")

# remove '#' from key
clean_key = args.key.replace("#", "")

# build full output path
output_file = f"map_outputs/{input_name}{clean_key}.png"

plt.savefig(output_file)



print(f"Saved plot to {output_file}")

