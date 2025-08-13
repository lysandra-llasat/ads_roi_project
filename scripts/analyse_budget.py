import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.ensemble import RandomForestRegressor


df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")


features = ["Ad_Spend (€)", "Impressions", "Clicks", "Conversions", "Revenue (€)", "CTR", "CPC (€)", "Conversion_Rate"]
X = df[features]
y = df["ROI"]


plt.figure(figsize=(10, 6))
sns.heatmap(df[features + ["ROI"]].corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("🔍 Corrélation entre les variables et le ROI")
plt.show()

X_const = sm.add_constant(X)  # Ajout de la constante
model = sm.OLS(y, X_const).fit()
print(model.summary())


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)
importance_df = pd.DataFrame({"Variable": X.columns, "Importance": rf_model.feature_importances_})
importance_df = importance_df.sort_values(by="Importance", ascending=False)


plt.figure(figsize=(8, 5))
sns.barplot(x="Importance", y="Variable", data=importance_df, palette="viridis")
plt.title("📊 Importance des variables sur le ROI")
plt.xlabel("Score d'importance")
plt.ylabel("Variable")
plt.show()

