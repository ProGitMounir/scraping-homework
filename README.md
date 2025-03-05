# Scraping des Plus Grandes Entreprises par Revenus

## Description
Cette application Streamlit permet de scraper des données sur les plus grandes entreprises par revenus dans différentes régions du monde (Europe, États-Unis, Afrique, Asie) à partir de Wikipédia. Les données sont affichées dans un tableau interactif et peuvent être téléchargées au format CSV.

## Fonctionnalités
- **Choix de la Région** : Sélectionnez une région (Europe, États-Unis, Afrique, Asie) pour scraper les données correspondantes.
- **Affichage des Données** : Les données scrapées sont affichées dans un tableau interactif.
- **Téléchargement en CSV** : Téléchargez les données au format CSV pour une utilisation hors ligne.
- **Gestion des Erreurs** : L'application gère les erreurs de connexion et les pages non trouvées.

## Technologies Utilisées
- **Streamlit** : Pour créer l'interface utilisateur de l'application.
- **Pandas** : Pour manipuler et afficher les données dans un DataFrame.
- **Requests** : Pour envoyer des requêtes HTTP et récupérer le contenu des pages web.
- **BeautifulSoup** : Pour parser le HTML et extraire les données des tableaux.

## Installation
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/scraping-homework.git
   
2. Accédez au répertoire du projet :
   ```bash
    cd scraping-homework

3. Installez les dépendances nécessaires :
   ```bash
    pip install -r requirements.txt
   
4. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py

## Utilisation
1. Sélectionnez une région dans le menu déroulant.

2. Cliquez sur "Scraper les Données" pour extraire les données.

3. Visualisez les données dans le tableau interactif.

4. Téléchargez les données en cliquant sur "Télécharger en CSV".





