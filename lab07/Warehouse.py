# Author: Erik Bobinski
# Date: 11/2/2024
# Description: Warehouse class with stores several unnamed goods
# You can add and remove goods, as well as view the total amount of goods

class Warehouse:
    def __init__(self, initAmount):
        self.__totalAmount = initAmount
        self.__initAmount = initAmount

    def addGoods(self, amount):
        self.__totalAmount += amount

    def removeGoods(self, amount):
        if (amount > self.__totalAmount):
            print("Cannot remove more than you have!")
        else:
            self.__totalAmount -= amount

    def getTotalGoods(self):
        return self.__totalAmount
