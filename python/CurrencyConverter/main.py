from locale import currency
from logging import exception
from urllib import response
import requests

class Currency():
    # create empty dictionary to store rates
    rates = {}
    def __init__(self, url) -> None:
        data = requests.get(url).json()
        self.rates = data["rates"]
    def convertMexPesos(self, fromCurrency, toCurrency, amount):
        initialAmount = amount
        if fromCurrency != 'EUR':
            amount = amount / self.rates[fromCurrency]
        # round to two decimal places 
        amount = round(amount * self.rates[toCurrency], 2)
        print('{} {} = {} {}'.format(initialAmount, fromCurrency, amount, toCurrency))

def main() -> None:
    print("...Converting Currencies....")
    accessKey = ''
    url = str.__add__('http://data.fixer.io/api/latest?acess_key=', accessKey)
    # initialize class
    c = Currency(url)
    fromCountry = input("From Country: ")
    toCountry = input("To Country: ")
    amount = int(input("Amount: "))

    # call conversion class
    c.convertMexPesos(fromCountry, toCountry, amount)

    

if __name__ == "__main__":
    main()