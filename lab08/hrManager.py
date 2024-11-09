# Author: Erik Bobinski
# Date: 11/8/2024
# Description: Main file to give user interactivity with the 
# object oriented employee system

from Supervisor import Supervisor
from Worker import Worker

def calcTotalPay(employees):
    sumPay = 0.0
    for i in range(len(employees)):
        sumPay += employees[i].calcPay(40)
    return round(sumPay, 2)

def listEmployees(employees):
    for i in range(len(employees)):
        print(employees)

def main():
    emps =[]

    senti = True
    while senti:
        try:
            empCnt = int(input("How many employees would you like to add: "))
            senti = False
        except:
            print("Invalid input, try again")
    
    for i in range(empCnt):
        senti = True
        while senti:
            try:
                print(f"Employee {i+1} of {empCnt}:")
                empType = int(input("Worker (1) or Supervisor (2): "))
                if empType == 1:
                    emps.append(Worker("name", i, 0, 0))
                    emps[i].setName(input("Name: "))
                    emps[i].setId(input("ID: "))
                    emps[i].setPayRate(round(float(input("Pay Rate: ")), 2))
                    emps[i].setShift(int(input("Shift (1 for day, 2 for night): ")))
                else:
                    emps.append(Supervisor("name", i, 0, 0))
                    emps[i].setName(input("Name: "))
                    emps[i].setId(input("ID: "))
                    emps[i].setPayRate(round(float(input("Pay Rate: ")), 2))
                    emps[i].setLevel(int(input("Shift (1 for day, 2 for night): ")))
                senti = False
            except ValueError:
                print("Invalid input, try again")
    
    print("Summary of all employees:")
    for i in range(len(emps)):
        print(emps[i])
    print(f"Total pay across all employees: {calcTotalPay(emps)}")


if __name__ == "__main__":
    main()

