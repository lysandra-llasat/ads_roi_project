import pandas as pd
import os

# Charger le dataset
DATA_PATH = os.path.join("data", "Brand_Sales_AdSpend_Data.csv")

def clean_dataset():
    try:
       
        data = pd.read_csv(DATA_PATH)


        data.dropna(inplace=True)
        
        data.columns = data.columns.str.replace(' ', '', regex=False)


        
        data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

       
        Q1 = data['Gross Sales'].quantile(0.25)
        Q3 = data['Gross Sales'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data = data[(data['Gross Sales'] >= lower_bound) & (data['Gross Sales'] <= upper_bound)]

        
        clean_path = os.path.join("data", "Clean_Brand_Sales_AdSpend_Data.csv")
        data.to_csv(clean_path, index=False)

        print("Dataset nettoyé et sauvegardé ")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exécuter le script
if __name__ == "__main__":
    clean_dataset()
