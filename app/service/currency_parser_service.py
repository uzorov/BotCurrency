import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse


def getCurrency(currency1):
    if currency1 in ["USD", "CNY"]:
        currency2 = "Russian Ruble"
        price_datetime, exchange_rates = get_exchange_list_xrates(currency1, 1)
        return exchange_rates[currency2]
    else:
        return get_exchange_list_metal(currency1)
    # if currency2 == "RUB":
    #    currency2 = "Russian Ruble"
    # elif currency2 == "USD":
    #    currency2 = "Russian Ruble"



def get_exchange_list_xrates(currency, amount=1):
    content = requests.get(f"https://www.x-rates.com/table/?from={currency}&amount={amount}").content
    soup = bs(content, "html.parser")
    price_datetime = parse(soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text)
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
    return price_datetime, exchange_rates


def get_exchange_list_metal(metal):
    if metal == "CGN":
        content = requests.get(f"https://www.metaltorg.ru/metal_catalog/metallurgicheskoye_syrye_i_polufabrikaty/chugun/chugun_peredelnyi/").content
        soup = bs(content, "html.parser")
        exchange_tables = soup.find_all("table")[17].find_all("tr")[-1].find_all("td")[-4].text.replace(",", ".")
        return exchange_tables
    if metal == "STL":
        content = requests.get(f"https://www.metaltorg.ru/metal_catalog/listovoi_prokat/list_rulon_bez_pokrytiya/goryachekatanaya_rulonnaya_stal/").content
        soup = bs(content, "html.parser")
        exchange_tables = soup.find_all("table")[17].find_all("tr")[2].find_all("td")[2].text.replace(",", ".")
        return exchange_tables

#def updateTodayValue():
 #   if adapter.isExistForToday("CNY"):
  #      adapter.updateValue("CNY", getCurrency("CNY"))
   # if adapter.isExistForToday("USD"):
#        adapter.updateValue("USD", getCurrency("USD"))
 #   if adapter.isExistForToday("CGN"):
  #      adapter.updateValue("CGN", getCurrency("CGN"))
   # if adapter.isExistForToday("STL"):
    #    adapter.updateValue("STL", getCurrency("STL"))



