import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")

features = ["Ad_Spend (€)", "Impressions", "Clicks", "Conversions", "Revenue (€)"]
X = df[features]
y = df["ROI"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de régression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print(f"Modèle entraîné avec MAE: {mae:.2f}")

# 📝 Tester une nouvelle publicité
new_ad = pd.DataFrame([{
    "Ad_Spend (€)": 500000,
    "Impressions": 10000000,
    "Clicks": 700000,
    "Conversions": 50000,
    "Revenue (€)": 8000000
}])

predicted_roi = model.predict(new_ad)[0]
print(f"💡 ROI estimé pour cette pub : {predicted_roi:.2f}")

