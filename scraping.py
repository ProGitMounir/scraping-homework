import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_wikipedia():
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    tables = soup.find_all('table', class_='wikitable sortable')
    if not tables:
        st.error("Table not found on the webpage.")
        return None
    
    table = tables[0]  # Select the first matching table
    headers = [header.text.strip() for header in table.find_all('th')]
    
    df = pd.DataFrame(columns=headers)
    rows = table.find_all('tr')[1:]
    
    for row in rows:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        if len(individual_row_data) == len(headers):
            df.loc[len(df)] = individual_row_data
    
    return df

def main():
    st.title("Web Scraping: Largest US Companies by Revenue")
    
    if st.button("Scrape Data"):
        df = scrape_wikipedia()
        if df is not None:
            st.write("### Scraped Data Table")
            st.dataframe(df)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "companies.csv", "text/csv")
            
if __name__ == "__main__":
    main()
