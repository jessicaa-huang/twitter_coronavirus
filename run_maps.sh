#!/bin/bash
shopt -s nullglob

# Input folder containing tweet zip files
input_folder="/data/Twitter dataset"

# Output folder
output_folder="./outputs"

# Process all 2020 zip files
for file in "$input_folder"/geoTwitter20-*.zip; do
  nohup python3 ./src/map.py \
    --input_path "$file" \
    --output_folder "$output_folder" &

  wait
done

echo "All files done processing"
