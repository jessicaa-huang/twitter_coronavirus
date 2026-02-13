#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--output_folder', default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime
import json
from collections import Counter, defaultdict

# load keywords
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
]

# initialize counters
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# make output folder if it doesn't exist
os.makedirs(args.output_folder, exist_ok=True)

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file inside the zip
    for i, filename in enumerate(archive.namelist()):
        print(f"[{datetime.datetime.now()}] Processing {args.input_path} -> {filename}")

        # open the inner file
        with archive.open(filename) as f:

            for line in f:
                tweet = json.loads(line)
                text = tweet['text'].lower()
                lang = tweet['lang']

                # handle country code: default to 'none' if missing
                country = 'none'
                if tweet.get('place') and tweet['place'].get('country_code'):
                    country = tweet['place']['country_code']

                # count hashtags and _all
                for hashtag in hashtags:
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1
                        counter_country[hashtag][country] += 1
                    counter_lang['_all'][lang] += 1
                    counter_country['_all'][country] += 1

# define output file paths
output_base = os.path.join(args.output_folder, os.path.basename(args.input_path))
output_path_lang = output_base + '.lang'
output_path_country = output_base + '.country'

# save results
print(f"Saving language counts to {output_path_lang}")
with open(output_path_lang, 'w') as f:
    f.write(json.dumps(counter_lang))

print(f"Saving country counts to {output_path_country}")
with open(output_path_country, 'w') as f:
    f.write(json.dumps(counter_country))

print(f"[{datetime.datetime.now()}] Finished processing {args.input_path}")

