from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(tweet):
    """Analyse le sentiment d'un tweet avec VADER"""
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(tweet)
    
    if sentiment_score['compound'] >= 0.05:
        return "positif"
    elif sentiment_score['compound'] <= -0.05:
        return "négatif"
    else:
        return "neutre"

# Tester quelques phrases
examples = [
    "J'adore ce produit, il est genial !",
    "C'est horrible, je déteste ça...",
    "C'est un produit.",
]

for text in examples:
    sentiment = analyze_sentiment_vader(text)
    print(f"Phrase: {text} -> Sentiment: {sentiment}")
