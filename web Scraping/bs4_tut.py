from bs4 import BeautifulSoup


with open("web Scraping/basics_bs4.html","r") as f:
    html_doc = f.read() 
soup = BeautifulSoup(html_doc,"html.parser")
print(soup.prettify())