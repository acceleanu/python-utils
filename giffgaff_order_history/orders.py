import csv
from bs4 import BeautifulSoup

f = open("orders.htm", "r")
html=f.read()

soup = BeautifulSoup(html.decode("utf-8", "ignore"), "html.parser")

table = soup.find("table", {"id": "ordersTable"})
rows = table.find_all("tr")

def toAscii(str):
    return str.encode('ascii', errors='ignore')

def elemToString(elem):
    if isinstance(elem.string, basestring):
        return elem.string.strip()
    else:
        return elem.find(class_='total').string.strip()

def rowToMap(rv):
    return {
        'date' : toAscii(elemToString(rv[0])), 
        'amount' : toAscii(elemToString(rv[2]))
    }

rows = [row.find_all("td") for row in rows]
rows = [r for r in rows if len(r) != 0]

orders = [rowToMap(r) for r in rows]

print orders

with open('orders.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['date', 'amount'])
    writer.writeheader()
    for order in orders:
        writer.writerow(order)

