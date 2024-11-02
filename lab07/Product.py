# Author: Erik Bobinski
# Date: 11/2/2024
# Description: product class that defines a product and its-
# name, amount of itself, its unit-price, and the total cost

class Product:
    def __init__(self):
        self.__name = ""
        self.__qty = 0
        self.__unitPrice = 0
        self.__totalCost = 0

    def getName(self):
        return self.__name
    def getQty(self):
        return self.__qty
    def getUnitPrice(self):
        return self.__unitPrice
    def getTotalCost(self):
        return self.__totalCost
    
    def setName(self, name):
        self.__name = name
    def setQty(self, qty):
        self.__qty = qty
    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice
    def setTotalCost(self, totalCost):
        self.__totalCost = totalCost
    

