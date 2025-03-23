# import feedparser

# # Define RSS feed URLs for different personas
# rss_feeds = {
#     "Technology": "https://techcrunch.com/feed/",
#     "Finance": "https://feeds.reuters.com/reuters/businessNews",
#     "Sports": "https://www.espn.com/espn/rss/news",
#     "Entertainment": "https://variety.com/feed/",
#     "Science": "https://www.sciencedaily.com/rss/all.xml"
# }

# def fetch_articles(feed_url):
#     """Fetch the latest news articles from an RSS feed."""
#     feed = feedparser.parse(feed_url)
#     articles = []
    
#     for entry in feed.entries[:5]:  # Get the top 5 articles
#         articles.append({
#             "title": entry.title,
#             "summary": entry.summary,
#             "link": entry.link
#         })
    
#     return articles

# # Fetch news for all categories
# for category, url in rss_feeds.items():
#     print(f"\n🔹 {category} News:")
#     articles = fetch_articles(url)
#     for article in articles:
#         print(f"📌 {article['title']}")
#         print(f"   {article['summary']}")
#         print(f"   🔗 Read More: {article['link']}\n")

############################################################

# import feedparser

# # Dictionary containing news categories and their RSS feed URLs
# rss_feeds = {
#     "Technology": "http://feeds.bbci.co.uk/news/technology/rss.xml",
#     "Finance": "http://rss.cnn.com/rss/money_news_international.rss",
#     "Sports": "https://www.espn.com/espn/rss/news",
#     "Entertainment": "https://www.hollywoodreporter.com/t/television/rss/",
#     "Science": "https://science.nasa.gov/rss.xml"
# }

# def fetch_news():
#     for category, url in rss_feeds.items():
#         print(f"\n🔹 {category} News:")
#         feed = feedparser.parse(url)
        
#         # Fetch and display the top 3 news articles for each category
#         for entry in feed.entries[:3]:
#             print(f"🔸 {entry.title}")
#             print(f"   {entry.link}\n")

# # Run the function
# if __name__ == "__main__":
#     fetch_news()

############################################################

# import nltk
# nltk.download('punkt')
# import feedparser
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer

# # Function to summarize text
# def summarize_text(text, num_sentences=2):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, num_sentences)
#     return " ".join(str(sentence) for sentence in summary)

# # Define RSS Feeds for different categories
# rss_feeds = {
#     "Technology": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
#     "Finance": "https://feeds.bbci.co.uk/news/business/rss.xml",
#     "Sports": "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
#     "Entertainment": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
#     "Science": "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
# }

# # Fetch and display summarized news
# for category, url in rss_feeds.items():
#     print(f"\n🔷 {category} News:")
#     feed = feedparser.parse(url)

#     for entry in feed.entries[:3]:  # Fetch top 3 news per category
#         title = entry.title
#         link = entry.link
#         description = entry.summary if hasattr(entry, 'summary') else entry.description

#         summary = summarize_text(description)  # Generate summary

#         print(f"\n📰 {title}\nSummary: {summary}\n🔗 Read more: {link}\n" + "-" * 50)

        ##############################################################################

import feedparser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Define user personas with their interests and sources
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

# Define RSS feeds for different categories
rss_feeds = {
    "Technology": "https://techcrunch.com/feed/",
    "Finance": "https://feeds.reuters.com/reuters/businessNews",
    "Sports": "https://www.espn.com/espn/rss/news",
    "Entertainment": "https://variety.com/feed/",
    "Science": "https://www.sciencedaily.com/rss/all.xml"
}

# Function to summarize news articles
def summarize_text(text, sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return " ".join([str(sentence) for sentence in summary])

# Function to fetch and summarize news for a persona
def fetch_and_summarize_news(persona_name):
    print(f"\n📰 Personalized News for {persona_name}:\n")
    
    persona = user_personas.get(persona_name, {})
    interests = persona.get("interests", [])

    for category, feed_url in rss_feeds.items():
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries[:3]:  # Get top 3 articles per category
            article_text = entry.summary
            article_title = entry.title
            article_link = entry.link

            # Check if the article matches persona interests
            if any(interest.lower() in article_text.lower() for interest in interests):
                summary = summarize_text(article_text, sentences=2)
                print(f"🔹 **{article_title}**")
                print(f"   {summary}")
                print(f"   🔗 [Read Full Article]({article_link})\n")

# Example: Fetch news for Alex Parker
fetch_and_summarize_news("Alex Parker")



############################################################

import feedparser
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

# Function to fetch and summarize news for a persona
def fetch_and_generate_newsletter(persona_name):
    print(f"\n📰 Generating Newsletter for {persona_name}...\n")

    persona = user_personas.get(persona_name, {})
    interests = persona.get("interests", [])
    
    # Create Markdown content
    md_content = f"# 📰 {persona_name}'s Personalized Newsletter\n\n"
    
    for category, feed_url in rss_feeds.items():
        feed = feedparser.parse(feed_url)
        
        # Add category heading
        md_content += f"## 🔹 {category} News\n\n"
        
        for entry in feed.entries[:3]:  # Get top 3 articles per category
            article_text = entry.summary
            article_title = entry.title
            article_link = entry.link

            # Check if article matches persona interests
            if any(interest.lower() in article_text.lower() for interest in interests):
                summary = summarize_text(article_text, sentences=2)
                md_content += f"### {article_title}\n"
                md_content += f"{summary}\n"
                md_content += f"[Read Full Article]({article_link})\n\n"

    # Save to Markdown file
    filename = f"{persona_name.replace(' ', '_')}_newsletter.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(md_content)

    print(f"✅ Newsletter saved as {filename}\n")

# Example: Generate a newsletter for Alex Parker
# Generate newsletters for all personas
for persona in user_personas.keys():
    fetch_and_generate_newsletter(persona)

print("✅ All newsletters generated successfully!")



