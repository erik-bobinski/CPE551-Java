# Author: Erik Bobinski
# Date: 11/8/2024
# Description: Subclass of Employee, has additional level attribute

from Employee import Employee

class Supervisor(Employee):

    def __init__(self, name, id, payRate, level):
        super().__init__(name, id, payRate)
        self.__level = level

    def calcPay(self, hours):
        return super().calcPay(hours) + (1000 * self.__level)
    
    def getLevel(self):
        return self.__level
    def setLevel(self, level):
        self.__level = level

    def __str__(self):
        return super().__str__() + f", Level: {self.__level}"