# X Analysis Tool

A Python tool for collecting and analyzing posts from X (formerly Twitter). This tool provides insights into sentiment, key players, and trends based on search queries.

## Features

- Data Collection: Scrape X posts based on keywords or hashtags
- Sentiment Analysis: Analyze the sentiment of collected posts
- Engagement Metrics: Track likes, retweets, and replies
- Top Posters: Identify the most active users
- Trend Analysis: Basic trend detection in the collected data

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd SOCMINTracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your X API credentials

## Usage

Run the main script with your desired search query:
```bash
python src/main.py
```

The script will:
1. Collect tweets based on the query
2. Analyze sentiment and engagement
3. Identify top posters
4. Display results in the console

## Project Structure

- `src/`
  - `x_collector.py`: Handles data collection from X
  - `analyzer.py`: Processes and analyzes the collected data
  - `main.py`: Main script demonstrating usage
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (not tracked in git)

## Requirements

- Python 3.8+
- X API credentials
- Dependencies listed in requirements.txt
