import datetime

import matplotlib.pyplot as plt
import numpy

from DBAdapter import DBAdapter
from currency_parser import getCurrency

adapter = DBAdapter()


def getExchangeValue(currency):
    if currency in ["USD", "CNY"]:
        data = adapter.getCurrencyDataFromDb(currency)
    else:
        data = adapter.getMetalDataFomDb(currency)
    if len(data) != 0 and data[-1][2] == datetime.datetime.now().strftime("%H:%M:%S") and \
            data[-1][2] == datetime.date.today().strftime("%D-%M-%Y"):
        return data[-1][3]
    adapter.updateValue(currency, getCurrency(currency))
    if currency in ["USD", "CNY"]:
        data = adapter.getCurrencyDataFromDb(currency)[-1][3]
    else:
        data = float(adapter.getMetalDataFomDb(currency)[-1][3]) * float(adapter.getCurrencyDataFromDb("USD")[-1][3])

    return data


def saveImg(currency, name):
    if currency in ["USD", "CNY"]:
        data = DBAdapter().getCurrencyDataFromDb(currency)
    else:
        data = DBAdapter().getMetalDataFomDb(currency)
    print(data)
    domashniy = {}
    for x in data:
        if x[1] in domashniy:
            domashniy[x[1]].append(x[3])
        else:
            domashniy[x[1]] = [x[3]]
    data = []
    for i in domashniy:
        data.append(numpy.mean(domashniy[i]))
    print(data)
    plt.close()
    #plt.axis([0, min(data) - 1, len(data), max(data) + 1])
    ax = plt.gca()
    ax.set_ylim([min(data) - 1,  max(data) + 1])
    plt.plot(list(map(lambda x: x.split("-")[0] + '.' + x.split("-")[1], domashniy.keys())), data)
    plt.grid(b=True)
    plt.draw()
    plt.savefig(name)
    plt.close()

if __name__ == '__main__':
    adapter = DBAdapter()
    adapter.clearDb()
    adapter.fillDb()
    saveImg("USD", "foto")

    print("USD =", getExchangeValue("USD"))
    print("CNY =", getExchangeValue("CNY"))
    print("CGN =", getExchangeValue("CGN"))
    print("STL =", getExchangeValue("STL"))
