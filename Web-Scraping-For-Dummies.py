#1: Import the libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#2: URL of the website to scrape
url = "https://books.toscrape.com/"

#3: Import the HTML code of the page
response = requests.get(url)
response.encoding = "utf-8"
html = response.text

#4: Analyze the HTML code
soup = BeautifulSoup(html, "html.parser")


#5: Data block extraction
books = soup.find_all("article", class_="product_pod") #?!!

#6: Store the data in a list
data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    data.append({"Titre": title, "Prix": price})
    
 #7 : Display as a table
df = pd.DataFrame(data)
print(df.head(10))