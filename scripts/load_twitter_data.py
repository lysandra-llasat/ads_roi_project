import re
import json
import os

# Définir le chemin du fichier contenant les tweets récupérés
RAW_TWEETS_PATH = os.path.join("data", "raw_tweets.json")
CLEAN_TWEETS_PATH = os.path.join("data", "clean_tweets.json")

def clean_tweet(tweet):
    """ Nettoie un tweet en supprimant les mentions, hashtags, liens et caractères spéciaux """
    tweet = tweet.lower()  
    tweet = re.sub(r'@\w+', '', tweet)  
    tweet = re.sub(r'#\w+', '', tweet)  
    tweet = re.sub(r'http\S+', '', tweet)  
    tweet = re.sub(r'[^\w\s]', '', tweet)  
    tweet = re.sub(r'\n', ' ', tweet)  
    tweet = re.sub(r'\s+', ' ', tweet).strip() 
    return tweet

def clean_twitter_data():
    try:
        # Lire les tweets bruts
        with open(RAW_TWEETS_PATH, "r", encoding="utf-8") as file:
            tweets_data = json.load(file)

        cleaned_tweets = []
        
        if isinstance(tweets_data, list):  
            for tweet in tweets_data:
                cleaned_text = clean_tweet(tweet.get("text", ""))
                if cleaned_text:  # Vérifier que le tweet n'est pas vide après nettoyage
                    cleaned_tweets.append({
                        "id": tweet.get("id", ""),
                        "text": cleaned_text
                    })
        else:
            raise ValueError("Format du fichier JSON non reconnu !")

        # Sauvegarder les tweets nettoyés
        with open(CLEAN_TWEETS_PATH, "w", encoding="utf-8") as file:
            json.dump(cleaned_tweets, file, ensure_ascii=False, indent=4)

        print(f" {len(cleaned_tweets)} tweets nettoyés et sauvegardés avec succès !")

    except Exception as e:
        print(f" Une erreur est survenue : {e}")

# Exécuter le script
if __name__ == "__main__":
    clean_twitter_data()