import pandas as pd
import numpy as np
import random


random.seed(42)
np.random.seed(42)

#  Liste de 50 marques fictives 
brands = [
    "Nike", "Apple", "McDonald's", "Coca-Cola", "Samsung", "Tesla", "Amazon", "Google", "Facebook", "Microsoft",
    "Pepsi", "Adidas", "Louis Vuitton", "Huawei", "Netflix", "Sony", "Intel", "Nestlé", "Toyota", "BMW",
    "Zara", "Starbucks", "Uber", "Airbnb", "Gucci", "L’Oréal", "Chanel", "Spotify", "Dell", "Visa",
    "Mastercard", "IBM", "Porsche", "Ferrari", "Rolex", "NVIDIA", "TikTok", "PayPal", "Snapchat", "Disney",
    "PlayStation", "Red Bull", "Canon", "Heineken", "Lamborghini", "Hyundai", "Siemens", "Volkswagen", "IKEA", "Twitter"
]

# Liste des pays
countries = ["USA", "France", "Allemagne", "UK", "Canada", "Espagne", "Italie", "Brésil", "Australie", "Japon"]

#  Génération de données sur 12 mois
dates = pd.date_range(start="2023-01-01", periods=12, freq="M")

#  Données sur la cible publicitaire
age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
genders = ["Male", "Female", "Non-binary"]
occupations = ["Student", "Employee", "Self-employed", "Unemployed", "Retired"]
income_levels = ["Low", "Middle", "High"]
ad_channels = ["TV", "Digital", "Print", "Social Media", "Outdoor"]
ad_types = ["Video", "Banner", "Sponsored Post", "Email", "Search Ad"]

#  Liste pour stocker les données
data = []

for date in dates:
    for brand in brands:
        for country in countries:
         
            ad_spend = random.randint(10000, 10000000)  # Budget pub (€)
            impressions = ad_spend * random.uniform(5, 20)
            clicks = impressions * random.uniform(0.005, 0.1)
            conversions = clicks * random.uniform(0.05, 0.3)
            revenue = conversions * random.uniform(10, 500)
            roi = revenue / ad_spend if ad_spend > 0 else 0

            
            ctr = clicks / impressions if impressions > 0 else 0
            cpc = ad_spend / clicks if clicks > 0 else 0
            conversion_rate = conversions / clicks if clicks > 0 else 0
            ad_frequency = impressions / random.randint(50000, 5000000)

            avg_cart_value = revenue / conversions if conversions > 0 else 0
            return_rate = random.uniform(0.02, 0.15)
            customer_satisfaction = round(random.uniform(3, 5), 2)

           
            sentiment_score = round(random.uniform(-1, 1), 2)
            tweet_mentions = random.randint(1000, 100000)
            sentiment_trend = round(sentiment_score + random.uniform(-0.2, 0.2), 2)
            positive_tweets = round(random.uniform(50, 100) * (sentiment_score + 1) / 2, 1)
            negative_tweets = 100 - positive_tweets

           
            target_age = random.choice(age_groups)
            target_gender = random.choice(genders)
            target_occupation = random.choice(occupations)
            target_income = random.choice(income_levels)
            ad_channel = random.choice(ad_channels)
            ad_type = random.choice(ad_types)

          
            data.append([
                date.strftime("%Y-%m-%d"), brand, country, ad_spend, int(impressions),
                int(clicks), int(conversions), round(revenue, 2), round(roi, 2), 
                round(ctr, 4), round(cpc, 2), round(conversion_rate, 4), round(ad_frequency, 2), 
                round(avg_cart_value, 2), round(return_rate, 4), customer_satisfaction, 
                sentiment_score, tweet_mentions, sentiment_trend, positive_tweets, negative_tweets,
                target_age, target_gender, target_occupation, target_income, ad_channel, ad_type
            ])


df = pd.DataFrame(data, columns=[
    "Date", "Brand", "Country", "Ad_Spend (€)", "Impressions", "Clicks", "Conversions", 
    "Revenue (€)", "ROI", "CTR", "CPC (€)", "Conversion_Rate", "Ad_Frequency",
    "Avg_Cart_Value (€)", "Return_Rate", "Customer_Satisfaction",
    "Sentiment_Score", "Tweet_Mentions", "Sentiment_Trend", "% Positive Tweets", "% Negative Tweets",
    "Target_Age", "Target_Gender", "Target_Occupation", "Target_Income", "Ad_Channel", "Ad_Type"
])


df.to_csv("synthetic_ad_data_50_brands_with_targeting.csv", index=False)


