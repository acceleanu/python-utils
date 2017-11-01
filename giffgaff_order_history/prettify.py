from bs4 import BeautifulSoup

f = open("ugly.htm", "r")
html=f.read()

soup = BeautifulSoup(html.decode("utf-8", "ignore"), "html.parser")

pretty=soup.prettify().encode("utf-8")
print(pretty)

