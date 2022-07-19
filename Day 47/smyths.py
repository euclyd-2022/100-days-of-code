import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

link = "https://content.syndigo.com/page/3c32d61a-b4a0-4a8c-a678-239fdc2a246f/210427.json"

params = {
"u": "37DC0B40-6B85-4599-A713-488DFDFEE640",
"siteid": "3c32d61a-b4a0-4a8c-a678-239fdc2a246f",
"pageid": "210427",
"s": "1657707252711",
"v": "v1.0.311",
"visitid": "41C79059-D8DD-4513-A365-AEBE536FFEC8",
"ref": "https://www.smythstoys.com/",
"r": "0.42450111577197425",
"pageurl": "https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pet-simulator/pet-simulator-x-series-1-collector-clips/p/210427"
}




r = requests.get(link,params=params,headers={
        'content-type': 'application/json; charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
soup = BeautifulSoup(r.text,"html.parser")
print(soup)
    # if not soup.select_one("a.trackProduct[href]"):break
    # for item in soup.select("a.trackProduct[href]"):
    #     product_name = item.select_one("h2.prodName").get_text(strip=True)
    #     product_price = item.select_one("[itemprop='price']").get("content")
    #     print(product_name,product_price)
    #
    # p+=1
