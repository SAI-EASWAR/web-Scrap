from bs4 import BeautifulSoup

with open("web Scraping/basics_bs4.html","r") as f:
    html_doc = f.read() 
soup = BeautifulSoup(html_doc,"html.parser")

# get the html code
# print(soup.prettify())

# to find all the tag with tag div
# for divs in soup.find_all("div"):
#     print(divs)

# we can also use css selectors in this

# xc=soup.select("a")
# print(xc)

#how to change the content in a html tag
# x = soup.find(class_="myclass")
# x.string= "this has been changed"
# print(x)


#to get the parent of the give tag
# x = soup.find(class_="myclass")
# print(x.parent)



