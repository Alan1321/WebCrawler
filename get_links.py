import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class get_links:

    def __init__(self, main_url) -> None:
        self.main_url = main_url

    def gather_links(self, init_link):
        try:
            html_text = requests.get(init_link).text
            soup = BeautifulSoup(html_text, 'lxml')
            all_links = soup.find_all('a')
            list = []

            for link in all_links:
                l = link.get('href')
                l = urljoin(self.main_url, l)
                if self.is_home_link(l):
                    list.append(l)
            return list
        except:
            print("Error Opening Link. Try again")
    
    def is_home_link(self, link):
        length = len(self.main_url)
        if(self.main_url == link[0:length]):
            return True
        return False

