# Author: Erik Bobinski
# Date: 11/8/2024
# Description: Subclass of Employee, has additional day/night-time shift attribute

from Employee import Employee

class Worker(Employee):

    def __init__(self, name, id, payRate, shift):
        super().__init__(name, id, payRate)
        self.__shift = shift
        
    def getShift(self, shift):
        return self.__shift
    def setShift(self, shift):
        self.__shift = shift
    
    def __str__(self):
        return super().__str__() + f", Shift: {'Day' if self.__shift == 1 else 'Night'}"
    
