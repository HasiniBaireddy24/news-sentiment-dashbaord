# Real-Time News Sentiment Intelligence Dashboard

An interactive dashboard that analyzes real-time news sentiment using Natural Language Processing (NLP).  
The application fetches live news articles based on a user-defined topic and visualizes sentiment insights through interactive charts.



## Project Overview

Every day thousands of news articles are published, making it difficult to quickly understand the overall sentiment around a topic.  
This project solves that problem by automatically analyzing news headlines and descriptions to determine whether the sentiment is positive, negative, or neutral.

The dashboard presents the results using visual analytics so users can quickly understand media sentiment trends.



## Features

- Fetch real-time news articles using NewsAPI
- Perform sentiment analysis using VADER (NLP)
- Interactive dashboard built with Streamlit
- Sentiment distribution visualization
- Sentiment trend analysis over time
- News source sentiment comparison
- Sentiment score distribution
- Automatically generated insights



## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- VADER Sentiment Analysis
- NewsAPI



## Project Workflow

1. User enters a topic to analyze.
2. The application fetches news articles using the NewsAPI.
3. Headlines and descriptions are processed for sentiment analysis.
4. Sentiment scores are calculated using VADER.
5. Results are visualized through interactive charts and metrics.



## How to Run the Project

### 1. Clone the repository
git clone https://github.com/yourusername/news-sentiment-dashboard.git


### 2. Install dependencies
pip install -r requirements.txt


### 3. Add your NewsAPI key

Login to NewsAPI and create your own API key.
Open `news_fetcher.py` and replace:
API_KEY = "YOUR_API_KEY"

with your actual API key.

### 4. Run the application
streamlit run app.py




## Use Cases

- Media sentiment monitoring
- Market sentiment analysis
- Brand reputation tracking
- Public opinion analysis

