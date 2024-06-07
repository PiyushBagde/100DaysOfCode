import requests
from bs4 import BeautifulSoup


class ScrapeData:
    def __init__(self):
        response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        zillo_site = response.text

        self.soup = BeautifulSoup(zillo_site, 'html.parser')

        self.all_addresses = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        self.all_prices = self.soup.find_all(attrs={"data-test": "property-card-price"})
        self.all_links = self.soup.find_all(class_="property-card-link")

        self.links = []
        self.prices = []
        self.addresses = []
        self.scrape()

    def scrape(self):
        self.links = [tag.get('href') for tag in self.all_links]
        print('Got links')
        self.prices = [tag.getText().replace("/mo", "").replace("+", "") for tag in self.all_prices]
        print('Got prices')
        self.addresses = [tag.getText().strip().replace("|", ",") for tag in self.all_addresses]
        print('Got addresses')
        print('Data Scrapped Successfully')
