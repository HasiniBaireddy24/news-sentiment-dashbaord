import streamlit as st
import pandas as pd
import plotly.express as px

from news_fetcher import fetch_news
from sentiment_analysis import analyze_sentiment

st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

# ------------------------------
# UI Styling
# ------------------------------

st.markdown("""
<style>

/* Metric cards */
div[data-testid="stMetric"] {
    border-radius: 10px;
    padding: 15px;
    border: 1px solid rgba(128,128,128,0.2);
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
}

/* Metric label */
div[data-testid="stMetricLabel"] {
    font-size: 16px;
}

/* Metric value */
div[data-testid="stMetricValue"] {
    font-size: 30px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.title("Real-Time News Sentiment Intelligence Dashboard")

# ------------------------------
# Topic Search
# ------------------------------

query = st.text_input("Enter Topic to Analyze", "technology")

if st.button("Fetch News"):

    df = fetch_news(query)

    sentiments = []
    scores = []

    for i in range(len(df)):
        text = str(df["title"][i]) + " " + str(df["description"][i])

        sentiment, score = analyze_sentiment(text)

        sentiments.append(sentiment)
        scores.append(score)

    df["sentiment"] = sentiments
    df["score"] = scores

    df["publishedAt"] = pd.to_datetime(df["publishedAt"])

# ------------------------------
# KPI METRICS
# ------------------------------

    total_news = len(df)
    positive_news = len(df[df["sentiment"] == "Positive"])
    negative_news = len(df[df["sentiment"] == "Negative"])
    neutral_news = len(df[df["sentiment"] == "Neutral"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Articles", total_news)
    col2.metric("Positive News", positive_news)
    col3.metric("Negative News", negative_news)
    col4.metric("Neutral News", neutral_news)

# ------------------------------
# MARKET SENTIMENT
# ------------------------------

    avg_sentiment = df["score"].mean()

    if avg_sentiment > 0.05:
        market = "🟢 Positive Market Sentiment"
    elif avg_sentiment < -0.05:
        market = "🔴 Negative Market Sentiment"
    else:
        market = "⚪ Neutral Market Sentiment"

    st.subheader("Overall Market Mood")
    st.write(market)

# ------------------------------
# NEWS TABLE
# ------------------------------

    st.subheader("News Articles")

    st.dataframe(df[["title", "source", "sentiment", "score"]])

# ------------------------------
# SENTIMENT DISTRIBUTION
# ------------------------------

    st.subheader("Sentiment Distribution")

    fig1 = px.pie(df, names="sentiment", title="News Sentiment Breakdown")

    fig1.update_traces(
        textfont_color="white",
        textfont_size=18
    )

    st.plotly_chart(fig1, use_container_width=True)

# ------------------------------
# SENTIMENT TREND
# ------------------------------

    st.subheader("Sentiment Trend Over Time")

    df_sorted = df.sort_values("publishedAt")

    fig2 = px.line(
        df_sorted,
        x="publishedAt",
        y="score",
        title="Sentiment Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ------------------------------
# SOURCE SENTIMENT ANALYSIS
# ------------------------------

    st.subheader("News Source Sentiment Analysis")

    source_sentiment = df.groupby(["source", "sentiment"]).size().reset_index(name="count")

    fig3 = px.bar(
        source_sentiment,
        x="source",
        y="count",
        color="sentiment",
        title="Sentiment by News Source"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ------------------------------
# SENTIMENT SCORE HISTOGRAM
# ------------------------------

    st.subheader("Sentiment Score Distribution")

    fig4 = px.histogram(df, x="score", nbins=20)

    st.plotly_chart(fig4, use_container_width=True)

# ------------------------------
# INSIGHTS SECTION
# ------------------------------

    st.subheader("Key Insights")

    dominant_sentiment = df["sentiment"].value_counts().idxmax()
    dominant_count = df["sentiment"].value_counts().max()

    most_active_source = df["source"].value_counts().idxmax()
    source_count = df["source"].value_counts().max()

    if avg_sentiment > 0.05:
        market_mood = "Positive"
    elif avg_sentiment < -0.05:
        market_mood = "Negative"
    else:
        market_mood = "Neutral"

    st.write(f"• Dominant sentiment: **{dominant_sentiment}** ({dominant_count} articles)")
    st.write(f"• Most active news source: **{most_active_source}** ({source_count} articles)")
    st.write(f"• Overall market mood: **{market_mood}**")