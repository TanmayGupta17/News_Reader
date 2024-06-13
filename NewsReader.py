import requests
import pyttsx3

newsapi_key = "8d8b867acc184e19b9230729c6837471"

# Initialize the speech engine
engine = pyttsx3.init()

# Get the topic from the user
topic = input("Enter the news topic to search: ")

# Use the topic in the URL
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-06-11&sortBy=popularity&apiKey={newsapi_key}"
response = requests.get(url).json()

article = response["articles"]
head = []
for ar in article:
    head.append(ar["description"])

for i in range(10):
    print(f"{i+1}. {head[i]}\n")

def mytext(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    for i in range(10):
        mytext(head[i])