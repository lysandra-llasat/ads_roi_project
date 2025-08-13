import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")


features = ["Ad_Spend (€)", "Impressions", "Clicks", "Conversions", "Revenue (€)", "CTR", "CPC (€)", "Conversion_Rate"]

correlation_matrix = df[features + ["ROI"]].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("🔍 Corrélation entre les variables et le ROI")
plt.show()
