class Employee:
    "Common base class for all Employee"
    empCount=0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print("Total employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print(self.name)
    