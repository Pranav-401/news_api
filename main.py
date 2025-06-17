import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key=os.getenv("API_KEY")

query=input("what News are you interested today ??????? : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-17&sortBy=publishedAt&apiKey={api_key}"
r = requests.get(url)
data=r.json()

articles=data["articles"]

# for index,article in enumerate(articles):

#   print(index+1,article['title'],article["description"],article["url"])
#   print("\n******************************\n")


i=1
for article in articles:
  
  print(f"{i} .",article['title'],article["description"],article["url"])
  i+=1
  print("\n******************************\n")