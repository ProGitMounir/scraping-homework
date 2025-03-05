import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

@st.cache_data
def scrape_wikipedia(url):
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch the webpage: {e}")
        return None

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
    
    # Clean data (remove footnotes)
    df = df.replace(r'\[\d+\]', '', regex=True)
    return df

def main():
    st.title("Web Scraping: Largest Companies by Revenue")
    
    # Description de l'application
    st.write("""
    ### Description de l'Application
    Cette application permet de scraper (extraire) des données à partir de pages Wikipédia listant les plus grandes entreprises par revenus dans différentes régions du monde. 
    Les données sont affichées dans un tableau interactif et peuvent être téléchargées au format CSV.

    ### Qu'est-ce que le Scraping ?
    Le scraping est une technique utilisée pour extraire automatiquement des données à partir de sites web. 
    Il consiste à analyser le code HTML d'une page web pour en extraire des informations structurées, comme des tableaux ou des listes.
    Dans cette application, nous utilisons la bibliothèque `BeautifulSoup` pour parser le HTML et `pandas` pour organiser les données dans un tableau.
    """)
    
    # Region selection
    region = st.radio("Sélectionnez une région", ("Europe", "États-Unis", "Afrique"))
    if region == "Europe":
        url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Europe_by_revenue'
    elif region == "États-Unis":
        url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    else:
        url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Africa_by_revenue'
    
    if st.button("Scraper les Données"):
        with st.spinner("Scraping des données en cours..."):
            df = scrape_wikipedia(url)
        
        if df is not None:
            st.write(f"### Tableau des Données pour les plus grandes entreprises en {region}")
            st.dataframe(df)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Télécharger en CSV", csv, "companies.csv", "text/csv")

if __name__ == "__main__":
    main()