from bs4 import BeautifulSoup
import requests

data = []

# send HTML request for page
url = "https://crypto.com/price"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")

# find table of data
coins = doc.find_all("tr")
# for every row of data, get/store info
for i in range(1, 51):
    coinInfo = coins[i].find_all("td")
    name = coinInfo[2].div.a.span.text
    price = coinInfo[3].div.text
    change_24 = coinInfo[4].p.text
    vol = coinInfo[5].text
    marketCap = coinInfo[6].text

    # append coin info to data list
    data.append([name, price, change_24, vol, marketCap])

print(data)
