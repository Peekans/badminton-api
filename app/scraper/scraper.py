from bs4 import BeautifulSoup
import requests

class BadmintonScraper:
    def __init__(self):
        self.base_url = "https://badmintonbay.com"

    def scrape_racket(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response, 'html.parser')
        # work in progress data scraping here
        racket_data = {
            "brand": "",
            "name": "",
            "frame": "",
            "shaft": "",
            "flex": "",
            "weight": "",
            "max_tension": "",
            "length": "",
            "balance": "",
            "grommets": "",
            "shaft_diameters": "",
            "special_features": ""
        }


        # add a delay here later after i implement that
        return racket_data