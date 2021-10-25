from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

data = []

# send HTML request for page
url = "https://finance.yahoo.com/cryptocurrencies"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")

# find table of data
coins = doc.find_all("tr")

# for every row of data, get/store info
for i in range(1, len(coins)):
    coinInfo = coins[i].find_all("td")
    name = coinInfo[1].text
    price = coinInfo[2].text
    change = coinInfo[3].text
    perChange = coinInfo[4].text
    marketCap = coinInfo[5].text
    vol = coinInfo[7].text
    circSupply = coinInfo[9].text

    # append coin info to data list
    data.append([name, price, change, perChange, marketCap, vol, circSupply])

# print grid structure of data
print(tabulate(data, headers=["Name", "Price", "Chane", "% Change", "Market Cap", "Volume in Currency (24hr)", "Circculating Supply"], tablefmt="grid"))
