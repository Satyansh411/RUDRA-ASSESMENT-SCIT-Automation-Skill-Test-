import nltk
import feedparser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import os

# Download necessary NLTK data
nltk.download('punkt')

# Define RSS feeds for different categories
rss_feeds = {
    "Technology": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "Finance": "https://feeds.bbci.co.uk/news/business/rss.xml",
    "Sports": "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
    "Entertainment": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
    "Science": "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
}

# Define personas
personas = {
    "Tech Enthusiast": ["Technology"],
    "Investor": ["Finance"],
    "Sports Fan": ["Sports"],
    "Entertainment Lover": ["Entertainment"],
    "Science Geek": ["Science"],
    "General Reader": list(rss_feeds.keys())  # All categories
}

# Function to summarize text
def summarize_text(text, num_sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Function to fetch and generate newsletters per persona
def fetch_and_generate_newsletters():
    if not os.path.exists("newsletters"):  # Ensure directory exists
        os.makedirs("newsletters")
    
    for persona, categories in personas.items():
        newsletter_content = f"✅ {persona} - Daily News Summary\n\n"
        print(f"\n✅ Generating newsletter for: {persona}\n")
        
        for category in categories:
            print(f"🔷 {category} News")
            newsletter_content += f"## 🔷 {category} News\n\n"
            feed = feedparser.parse(rss_feeds[category])
            
            for entry in feed.entries[:3]:  # Fetch top 3 news per category
                title = entry.title
                link = entry.link
                description = entry.summary if hasattr(entry, 'summary') else entry.description
                summary = summarize_text(description)
                
                newsletter_content += f"### 📰 {title}\n"
                newsletter_content += f"Summary: {summary}\n"
                newsletter_content += f"🔗 [Read more]({link})\n\n"
                newsletter_content += "--------------------------------------------------\n\n"
                
                print(f"📰 {title}")
                print(f"Summary: {summary}")
                print(f"🔗 Read more: {link}\n")
                print("--------------------------------------------------")
        
        # Save newsletter as a markdown file
        file_name = f"{persona.replace(' ', '_')}_newsletter.md"
        file_path = os.path.join("newsletters", file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(newsletter_content)
    
    print("\n✅ All newsletters generated successfully!")

# Execute the function
fetch_and_generate_newsletters()