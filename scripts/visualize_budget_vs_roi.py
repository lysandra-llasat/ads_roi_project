import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Charger les données
df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")


df["Ad_Spend²"] = df["Ad_Spend (€)"] ** 2


X = sm.add_constant(df[["Ad_Spend (€)", "Ad_Spend²"]])  # Ajoute un biais
y = df["ROI"]

model = sm.OLS(y, X).fit()
print(model.summary())


x_range = np.linspace(df["Ad_Spend (€)"].min(), df["Ad_Spend (€)"].max(), 100)
X_pred = sm.add_constant(pd.DataFrame({"Ad_Spend (€)": x_range, "Ad_Spend²": x_range**2}))
y_pred = model.predict(X_pred)


plt.figure(figsize=(10, 6))


sns.scatterplot(
    data=df, 
    x="Ad_Spend (€)", 
    y="ROI", 
    hue="Ad_Channel", 
    alpha=0.7
)


sns.regplot(
    data=df, 
    x="Ad_Spend (€)", 
    y="ROI", 
    scatter=False, 
    color="black", 
    ci=None,
    label="Régression linéaire"
)


plt.plot(x_range, y_pred, color="red", linestyle="dashed", linewidth=2, label="Régression quadratique")


plt.title("💰 Influence du budget publicitaire sur le ROI")
plt.xlabel("Dépenses publicitaires (€)")
plt.ylabel("ROI")


plt.legend(title="Modèles", loc="upper right")


plt.show()
