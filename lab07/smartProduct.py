# Author: Erik Bobinski
# Date: 11/2/2024
# Description: Improved product ordering system that appends an id to each product 
# and constructor allows programmer to define several attributes for each product

class SmartProduct:
    def __init__(self, name, qty, unitPrice, id):
        self.__name = name
        self.__qty = qty
        self.__unitPrice = unitPrice
        self.__totalCost = unitPrice * qty
        self.__id = id

    def getName(self):
        return self.__name
    def getQty(self):
        return self.__qty
    def getUnitPrice(self):
        return self.__unitPrice
    def getTotalCost(self):
        return self.__totalCost
    def getId(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name
    def setQty(self, qty):
        self.__qty = qty
    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice
    def setTotalCost(self, totalCost):
        self.__totalCost = totalCost
    def setId(self, id):
        self.__id = id
