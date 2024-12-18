import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Streamlit app title
st.title("Quotes Scraper")

# Select topic
tag = st.selectbox('Choose a topic', ['love', 'humor', 'quotes', 'books'])

# Button to generate CSV
generate = st.button('Generate CSV')

# Base URL
url = f"https://quotes.toscrape.com/tag/{tag}/"

# Fetch content from the URL
try:
    res = requests.get(url)
    res.raise_for_status()  # Raise an error for HTTP issues
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching quotes: {e}")
    st.stop()

# Parse the content
content = BeautifulSoup(res.content, 'html.parser')

# Find all quote divs
quotes = content.find_all('div', class_='quote')

# Prepare to store quotes
quote_file = []

# Display quotes and collect data
for quote in quotes:
    try:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        link = quote.find('a')['href']
        
        # Display the quote and author
        st.success(text)
        st.markdown(f"[{author}](https://quotes.toscrape.com{link})", unsafe_allow_html=True)
        
        # Append data to the list
        quote_file.append([text, author, f"https://quotes.toscrape.com{link}"])
    except Exception as e:
        st.warning(f"Error processing a quote: {e}")

# Generate CSV if button is clicked
if generate:
    if quote_file:
        try:
            df = pd.DataFrame(quote_file, columns=['Quote', 'Author', 'Link'])
            df.to_csv('quotes.csv', index=False)
            st.success("CSV file 'quotes.csv' has been generated successfully!")
        except Exception as e:
            st.error(f"Error generating CSV: {e}")
    else:
        st.warning("No quotes found to save.")
