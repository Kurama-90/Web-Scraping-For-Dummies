# Web-Scraping-For-Dummies
------------------------------

Extract information (title and price) from the books listed on the demonstration website `http://books.toscrape.com/`.

### Prerequisites

Ensure you have **Python** and the following libraries installed:

-   `requests`: To make HTTP requests and retrieve web page content.

-   `BeautifulSoup` (`bs4`): To parse the HTML code and extract data.

-   `pandas`: To store and display the extracted data in a tabular format (DataFrame).

You can install them via `pip`:

Bash

```
pip install requests beautifulsoup4 pandas

```

### Code Explanation Step-by-Step

The script is divided into seven logical steps:

* * * * *

#### 1\. Import Libraries

Python

```
import requests
from bs4 import BeautifulSoup
import pandas as pd

```

-   We import the three necessary libraries: **`requests`** for web connection, **`BeautifulSoup`** for HTML parsing, and **`pandas`** for data manipulation.

* * * * *

#### 2\. Define the URL

Python

```
url = "https://books.toscrape.com/"

```

-   The **URL** (Uniform Resource Locator) of the web page we want to scrape is defined in a variable.

* * * * *

#### 3\. Retrieve HTML Code

Python

```
response = requests.get(url)
response.encoding = "utf-8"
html = response.text

```

-   **`requests.get(url)`** sends an HTTP request to the URL to fetch the page.

-   **`response.encoding = "utf-8"`** ensures that special characters are correctly decoded.

-   **`html = response.text`** stores the page's HTML content as a string.

* * * * *

#### 4\. Analyze the HTML Code

Python

```
soup = BeautifulSoup(html, "html.parser")

```

-   The **`BeautifulSoup`** object is created. It takes the HTML code and parses it using Python's standard HTML parser (`"html.parser"`), making it navigable and searchable.

* * * * *

#### 5\. Data Block Extraction

Python

```
books = soup.find_all("article", class_="product_pod")

```

-   This is the key scraping step. We use the **`find_all()`** method to locate **all** HTML elements of type **`<article>`** that have the attribute **`class`** equal to **`"product_pod"`**.

    -   On the website, each book's information block (title, price, image) is contained within this element.

-   The `books` variable now holds a list of all these book blocks.

* * * * *

#### 6\. Extract and Store Specific Data

Python

```
data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    data.append({"Titre": title, "Prix": price})

```

-   An empty list **`data`** is initialized.

-   A **`for`** loop iterates over each book block (`book`):

    -   **Title (`title`)**: The title is found in the **`title`** attribute of the **`<a>`** tag, which is nested inside the **`<h3>`** tag within the `book` block.

    -   **Price (`price`)**: The price is in the **`<p>`** tag with the class **`"price_color"`**. We use **`.text`** to get only the textual content of this element.

    -   A dictionary containing the title and price is appended to the **`data`** list.

* * * * *

#### 7\. Display as a Table

Python

```
df = pd.DataFrame(data)
print(df.head(10))

```

-   The list of dictionaries **`data`** is converted into a **Pandas `DataFrame`** object (`df`), which allows the data to be displayed in a clear, tabular format.

-   **`print(df.head(10))`** displays the first 10 rows of the DataFrame, confirming the successful extraction.

* * * * *

### How to Run the Script

1.  Download `Web-Scraping-For-Dummies.py`.

2.  Open your terminal or command prompt.

3.  Execute the script:

Bash

```
python Web-Scraping-For-Dummies.py

```

The output will display a table of the first 10 scraped books.
