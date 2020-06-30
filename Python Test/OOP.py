#Create a class Employee

#understand the difference between class variables and instant variables
#regular/class/static methods
#inheritance
#setters/getters/deleter

class Employee:
    #Class variable
    #If changed by the class, all objects will be modified, if a certain object modifies it, will be specifically modified for that object
    bonus_rate = 0
    count = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + "." + last + "@company.com"
        Employee.count+=1 #Now it's more like a static variable
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        self.first , self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print("Delete fullname")
        self.first = None
        self.last = None

    def printInfo(self):
        print (self.first,"\n",self.last,"\n",self.pay,"\n",self.email,"\n",self.bonus_rate)


    #This is a class method, if any instance called it, it will change the bonus_rate normally
    @classmethod
    def set_bonus(cls,val):
        cls.bonus_rate = val
    #Class method could be used as alternative constructors as well
    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    #They are more like a regular functions with some logical connection with the class
    #doesn't pass any arguments automatically
    @staticmethod
    def is_workday(day):
        #mon = 0 and sun = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#inherites from Employee
class Developer(Employee):
    def __init__ (self,first,last,pay,prog_lang):
        #NOTE: same as Employee().__init__(self,first,last,pay)
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

#inherites from Employee
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            emp.printInfo()

if __name__ == "__main__":
    import datetime

    Employee.set_bonus(1.04)
    emp1 = Employee("ev","evram",2000)
    emp2 = Employee("ev2","evram2",2000)
    emp3 = Employee.from_string("ev3-evram3-3000")
    # print (Employee.count)
    dev1 = Developer("dev1","develop1",3000,"python")
    dev2 = Developer("dev2","develop2",4000,"python2")
    # print (Employee.count)
    mgr = Manager("evev","evev",200000,[emp1,emp2,emp3,dev1,dev2])
    # mgr.printInfo()
    #mgr.print_emp()
    

    #NOTE: The usage of isinstance and issubclass
    # print (isinstance(dev1,Employee))
    # print (isinstance(dev1,Developer))
    # print (isinstance(dev1,Manager))
    # print (issubclass(Developer,Employee))
    # print (issubclass(Manager,Employee))
    # print (issubclass(Employee,Developer))
    #my_date = datetime.date(2016,7,10)
    #NOTE: print (Employee.is_workday(my_date)) == print (emp3.is_workday(my_date)) == False
    #NOTE: Employee.printInfo(emp1) = emp1.printInfo()