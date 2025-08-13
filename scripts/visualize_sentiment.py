import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ANALYZED_TWEETS_PATH = os.path.join("data", "analyzed_tweets.json")

def visualize_sentiments():
    try:
        # Charger les tweets analysés
        with open(ANALYZED_TWEETS_PATH, "r", encoding="utf-8") as file:
            tweets_data = json.load(file)

        # Convertir en DataFrame
        df = pd.DataFrame(tweets_data)

        # Graphe en camembert
        sentiment_counts = df['sentiment'].value_counts()
        plt.figure(figsize=(6, 6))
        sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'gray', 'red'])
        plt.title("Répartition des Sentiments des Tweets")
        plt.ylabel("")
        plt.show()

        # Graphe de l'évolution des sentiments
        df['Date'] = pd.to_datetime(df['id'].astype(int), errors='coerce')
        df['Date'] = df['Date'].dt.date  # Garder seulement la date
        sentiment_over_time = df.groupby(['Date', 'sentiment']).size().unstack().fillna(0)

        plt.figure(figsize=(10, 5))
        sentiment_over_time.plot(kind='bar', stacked=True, colormap='coolwarm')
        plt.title("Évolution des Sentiments des Tweets")
        plt.xlabel("Date")
        plt.ylabel("Nombre de Tweets")
        plt.xticks(rotation=45)
        plt.legend(title="Sentiment")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

        print(" Visualisation des sentiments terminée !")

    except Exception as e:
        print(f" Erreur lors de la visualisation : {e}")

# Exécuter le script
if __name__ == "__main__":
    visualize_sentiments()
