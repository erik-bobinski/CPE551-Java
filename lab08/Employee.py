# Author: Erik Bobinski
# Date: 11/8/2024
# Description: Class for parent class employee

class Employee:

    def __init__(self, name, id, payRate):
        self._name = name
        self._id = id
        self._payRate = payRate

    def calcPay(self, hours):
        return hours * self._payRate
    
    def getName(self, hours):
        return self._name
    def getId(self, id):
        return self._id
    def getPayRate(self, payRate):
        return self._payRate
    
    def setName(self, name):
        self._name = name
    def setId(self, id):
        self._id = id
    def setPayRate(self, payRate):
        self._payRate = payRate
    
    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}, Pay Rate: {self._payRate}"

    