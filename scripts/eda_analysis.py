import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = os.path.join("data", "Clean_Brand_Sales_AdSpend_Data.csv")
data = pd.read_csv(DATA_PATH)

print("Aperçu du dataset :")
print(data.head())

print("\nValeurs manquantes :")
print(data.isnull().sum())


data.columns = data.columns.str.strip()
print("\nColonnes après nettoyage :")
print(data.columns)


print("\nStatistiques descriptives :")
print(data.describe())


data['Date'] = pd.to_datetime(data['Date'])


plt.figure(figsize=(12, 6))
sns.histplot(data['Gross Sales'], bins=30, kde=True, color="blue", label="Gross Sales")
sns.histplot(data['Total Ad Spend'], bins=30, kde=True, color="red", label="Ad Spend")
plt.legend()
plt.title("Distribution des ventes et dépenses publicitaires")
plt.show()


numeric_data = data.select_dtypes(include=['number'])  # Exclure les colonnes non numériques
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matrice de Corrélation")
plt.show()


time_series = data.groupby('Date')[['Gross Sales', 'Total Ad Spend']].sum()
plt.figure(figsize=(12, 6))
sns.lineplot(data=time_series, markers=True)
plt.title("Évolution des Ventes et Dépenses Publicitaires")
plt.xlabel("Date")
plt.ylabel("Montant en dollars ($)")
plt.xticks(rotation=45)
plt.legend(["Ventes Brutes", "Dépenses Publicitaires"])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


country_sales_spend = data.groupby('Country')[['Gross Sales', 'Total Ad Spend']].sum()
print("\nVérification des valeurs par pays :")
print(country_sales_spend)

plt.figure(figsize=(12, 6))
country_sales_spend.plot(kind='bar', figsize=(12, 6), log=True, color=['blue', 'red'])
plt.title('Ventes Brutes et Dépenses Publicitaires par Pays (Échelle Logarithmique)')
plt.ylabel('Montant en dollars (log)')
plt.xlabel('Pays')
plt.xticks(rotation=45)
plt.legend(["Ventes Brutes", "Dépenses Publicitaires"])
plt.show()


data['ROI'] = (data['Gross Sales'] - data['Total Ad Spend']) / data['Total Ad Spend']
data['ROI'] = data['ROI'].replace([float('inf'), -float('inf')], 0)  # Remplacer les valeurs infinies
roi_by_country = data.groupby('Country')['ROI'].mean()

plt.figure(figsize=(12, 6))
roi_by_country.sort_values().plot(kind='bar', color='green')
plt.title("ROI moyen par pays")
plt.xlabel("Pays")
plt.ylabel("ROI (Taux de rentabilité)")
plt.xticks(rotation=45)
plt.axhline(0, color='black', linestyle='--')
plt.show()


sales_by_brand = data.groupby('Brand Name')['Gross Sales'].sum()
plt.figure(figsize=(8, 8))
sales_by_brand.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='coolwarm')
plt.title("Répartition des Ventes par Marque")
plt.ylabel("")  # Supprimer le label y
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['Total Ad Spend'], y=data['Gross Sales'], alpha=0.5)
sns.regplot(x=data['Total Ad Spend'], y=data['Gross Sales'], scatter=False, color="red")
plt.title("Corrélation entre Dépenses et Ventes")
plt.xlabel("Dépenses Publicitaires ($)")
plt.ylabel("Ventes Brutes ($)")
plt.show()
