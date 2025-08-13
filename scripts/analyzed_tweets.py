from textblob import TextBlob
import json
import os

# Définir le chemin du fichier nettoyé
CLEAN_TWEETS_PATH = os.path.join("data", "clean_tweets.json")
ANALYZED_TWEETS_PATH = os.path.join("data", "analyzed_tweets.json")

def analyze_sentiment(tweet):
    """ Analyse le sentiment d'un tweet et retourne une polarité (positif, neutre, négatif) """
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity  # Score de sentiment (-1 négatif, 0 neutre, +1 positif)

    if polarity > 0:
        return "positif"
    elif polarity < 0:
        return "négatif"
    else:
        return "neutre"

def analyze_tweets():
    try:
     
        with open(CLEAN_TWEETS_PATH, "r", encoding="utf-8") as file:
            tweets_data = json.load(file)

        analyzed_tweets = []
        for tweet in tweets_data:
            sentiment = analyze_sentiment(tweet["text"])
            analyzed_tweets.append({
                "id": tweet["id"],
                "text": tweet["text"],
                "sentiment": sentiment
            })


        with open(ANALYZED_TWEETS_PATH, "w", encoding="utf-8") as file:
            json.dump(analyzed_tweets, file, ensure_ascii=False, indent=4)

        print("Analyse des sentiments terminée")

    except Exception as e:
        print(f"Erreur lors de l'analyse des tweets : {e}")

# Exécuter le script
if __name__ == "__main__":
    analyze_tweets()
