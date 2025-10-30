import requests
from bs4 import BeautifulSoup
from typing import List


class Website:
    
    usr: str
    title: str
    body: str
    links: List[str]
    text: str

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        body_tag = soup.find('body')
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = body_tag.get_text(separator="\n", strip=True) if body_tag else "No body tag found"
        else:
            self.text = ""
            links = [link.get('href') for link in soup.find_all('a')]
            self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage title:\n {self.title}\nWebpage Content:\n{self.text}\n\n"
    
    def get_references(self):
        return f"Reference Link:\n{self.links}"
        

if __name__ == "__main__":
    scrapper = Website("https://www.scrapethissite.com/pages/")
    print(scrapper.get_contents())