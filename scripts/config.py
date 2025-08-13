import os
from dotenv import load_dotenv

load_dotenv()  

GOOGLE_ADS_API_KEY = os.getenv('GOOGLE_ADS_API_KEY')
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN')

print("Clés API chargées avec succès !")
