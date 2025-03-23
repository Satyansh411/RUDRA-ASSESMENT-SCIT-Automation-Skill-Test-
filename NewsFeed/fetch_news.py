import feedparser
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Define user personas with their interests
user_personas = {
    "Alex Parker": {
        "interests": ["AI", "cybersecurity", "blockchain", "startups", "programming"],
        "sources": ["TechCrunch", "Wired", "Ars Technica", "MIT Tech Review"]
    },
    "Priya Sharma": {
        "interests": ["Global markets", "startups", "fintech", "cryptocurrency", "economics"],
        "sources": ["Bloomberg", "Financial Times", "Forbes", "CoinDesk"]
    },
    "Marco Rossi": {
        "interests": ["Football", "F1", "NBA", "Olympic sports", "esports"],
        "sources": ["ESPN", "BBC Sport", "Sky Sports F1", "The Athletic"]
    },
    "Lisa Thompson": {
        "interests": ["Movies", "celebrity news", "TV shows", "music", "books"],
        "sources": ["Variety", "Rolling Stone", "Billboard", "Hollywood Reporter"]
    },
    "David Martinez": {
        "interests": ["Space exploration", "AI", "biotech", "physics", "renewable energy"],
        "sources": ["NASA", "Science Daily", "Nature", "Ars Technica Science"]
    }
}

# Define RSS feeds
rss_feeds = {
    "Technology": "https://techcrunch.com/feed/",
    "Finance": "https://feeds.reuters.com/reuters/businessNews",
    "Sports": "https://www.espn.com/espn/rss/news",
    "Entertainment": "https://variety.com/feed/",
    "Science": "https://www.sciencedaily.com/rss/all.xml"
}

# Function to summarize news
def summarize_text(text, sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return " ".join([str(sentence) for sentence in summary])

# Function to fetch and generate news for all personas
def fetch_news():
    news_data = {}

    for persona_name, persona in user_personas.items():
        interests = persona.get("interests", [])
        persona_news = []

        for category, feed_url in rss_feeds.items():
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:3]:  # Get top 3 articles per category
                article_text = entry.summary
                article_title = entry.title
                article_link = entry.link

                # Check if article matches persona interests
                if any(interest.lower() in article_text.lower() for interest in interests):
                    summary = summarize_text(article_text, sentences=2)
                    persona_news.append({
                        "title": article_title,
                        "summary": summary,
                        "link": article_link,
                        "category": category
                    })

        news_data[persona_name] = persona_news

    # Save the data as a JSON file
    with open("news_data.json", "w", encoding="utf-8") as file:
        json.dump(news_data, file, indent=4)

    print("✅ News data saved to news_data.json")

# Run the function
fetch_news()
