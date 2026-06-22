import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Empty lists
quotes = []
authors = []

# Find all quotes
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quotes.append(text)
    authors.append(author)

# Create DataFrame
data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

# Print output
print(data)

# Save as CSV
data.to_csv("quotes.csv", index=False)

print("\nData saved successfully as quotes.csv")