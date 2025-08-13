import pandas as pd


df = pd.read_csv("data/synthetic_ad_data_50_brands_with_targeting.csv")

roi_by_channel = df.groupby("Ad_Channel")["ROI"].mean().sort_values(ascending=False)


print("📊 ROI moyen par canal publicitaire :")
print(roi_by_channel)
