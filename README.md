# Coronavirus Twitter Analysis (2020)

This project analyzes geotagged tweets sent in 2020 to track the spread and discussion of coronavirus-related topics on social media. Using Python and a MapReduce-style workflow, we processed over a billion tweets to visualize hashtag usage across countries and languages, and to observe trends over the year.

## Project Overview

We processed the 2020 geotagged tweets dataset using a MapReduce approach:

1. **Map Step (`map.py`)**: Counts occurrences of specific hashtags by language and country for each daily dataset.  
2. **Reduce Step (`reduce.py`)**: Merges daily counts into comprehensive datasets for languages and countries.  
3. **Visualization (`visualize.py`)**: Generates bar graphs showing the top 10 countries or languages for a selected hashtag.  
4. **Alternative Reduce (`alternative_reduce.py`)**: Generates line plots showing hashtag usage over time, with one line per hashtag and the x-axis representing the day of the year.

## Key Outputs

The analysis produced four main plots:

- `country_coronavirus.png` – Top 10 countries tweeting #coronavirus.  
- `country_코로나바이러스.png` – Top 10 countries tweeting #코로나바이러스.  
- `lang_coronavirus.png` – Top 10 languages for #coronavirus tweets.  
- `lang_코로나바이러스.png` – Top 10 languages for #코로나바이러스 tweets.  

Additionally, the alternative reduce script generated descriptive trend plots for hashtags over the year, e.g., `map_outputs/country_코로나바이러스_trend.png`.

## Technologies and Techniques

- **Python** for data processing and visualization.  
- **MapReduce paradigm** for parallel processing of large-scale datasets.  
- **Matplotlib** for generating plots.  
- **JSON** for structured data representation.  

## What This Demonstrates

- Handling and processing extremely large datasets (~1.1 billion tweets).  
- Working with multilingual text and geolocation metadata.  
- Applying parallel processing concepts with MapReduce.  
- Generating clear, descriptive visualizations suitable for reporting and presentation.
