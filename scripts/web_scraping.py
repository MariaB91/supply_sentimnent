import requests 
from bs4 import BeautifulSoup

def scrapper_avis(url):
    """ fonction qui permet de scrapper une page web
    parametres:
    url : url de la page
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


avis = scrapper_avis('https://fr.trustpilot.com/categories/home_garden')