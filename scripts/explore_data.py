import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")

# Vérifier les premières lignes
print(df.head())


print(df.info())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

#Visualisation : Distribution du ROI par marque
plt.figure(figsize=(12, 6))
sns.boxplot(x="Brand", y="ROI", data=df)
plt.xticks(rotation=90)
plt.title("Distribution du ROI par marque")
plt.show()
