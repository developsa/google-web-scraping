import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

search_input = input("Search a word : ").replace(" ", "+")
url = "https://www.google.com/search?q=" + search_input

headerParams = {
    "user-agent": os.getenv("USER_AGENT")}

response = requests.get(url, headers=headerParams)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("div", class_="g")
try:
    for result in results:
        a_tag = result.find("a")
        links = a_tag["href"]  # Links
        text = a_tag.find("h3").string  # Titles
        print(links + "  ==>  " + text)
        print("*************")
except AttributeError:
    pass
