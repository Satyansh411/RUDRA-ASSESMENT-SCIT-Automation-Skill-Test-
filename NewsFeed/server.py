from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load news data from JSON file
def load_news():
    with open("news_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/news")
def get_news():
    news_data = load_news()
    return jsonify(news_data)

if __name__ == "__main__":
    app.run(debug=True)






