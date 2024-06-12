# # 8d8b867acc184e19b9230729c6837471

import requests
import os
from os import system

newsapi_key = "8d8b867acc184e19b9230729c6837471"
url = "https://newsapi.org/v2/everything?q=Apple&from=2024-06-11&sortBy=popularity&apiKey=8d8b867acc184e19b9230729c6837471"
response = requests.get(url).json()

article = response["articles"]
head = []
for ar in article:
     head.append(ar["description"])

for i in range(10):
    print(f"{i+1}. {head[i]}\n")

def mytext(text):
    system("say {}".format(text))
    
if __name__ == "__main__":
    for i in range(10):
        mytext(head[i])
