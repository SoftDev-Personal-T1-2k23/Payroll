"""An employee class and related employee classifications"""
from abc import ABC, abstractmethod

import pandas as pd
import Data.Payroll as Payroll
from Data.FileConstants import DIR_ROOT

class Employee:
    #Employee object contain their name, id, payment info, classification info, and adress
    def __init__(self, data):
        name_raw = data[1].split(' ')
        name_join  = ''
        self.id = data[0]
        self.last_name = name_raw.pop()
        self.first_name = name_join.join(name_raw)
        self.address = data[2]
        self.city = data[3]
        self.state = data[4]
        self.zip = data[5]
        self.classification = None
        self.paymethod = data[6]
        self.salary = data[8]
        self.commission = data[9]
        self.hourly = data[10]
        self.route = data[11]
        self.account = data[12]
        self.password = data[13]
        self.start_date = data[14]
        self.privilege = data[15]
        self.department = data[16]
        self.email = data[17]
        self.phone = data[18]
        self.title = data[19]
        
        self.quick_attribute = {
        #use as a reference for which attribute corrosponds to which number
            'ID': self.id,
            'First name': self.first_name,
            'Last name': self.last_name,
            'Address': self.address,
            'City': self.city,
            'State': self.state,
            'Zip': self.zip,
            'Classification': str(self.classification),
            'PayMethod': self.paymethod,
            'Route': self.route,
            'Account': self.account,
            'Start Date': self.start_date,
            'Privilege': self.privilege,
            'Department': self.department,
            'Email': self.email,
            'Phone': self.phone,
            'Title': self.title

        }
        self.pay_type_dict = {
            "Salary": self.salary,
            "Hourly": self.hourly,
            "Commission": self.commission
        }
        self.editable_by_user = {
        #use as a reference for which attribute corrosponds to which number
            'First name': self.first_name,
            'Last name': self.last_name,
            'Address': self.address,
            'City': self.city,
            'State': self.state,
            'Zip': self.zip,
            'Route': self.route,
            'Account': self.account,
            'Email': self.email,
            'Phone': self.phone,
            'Title': self.title
        }
        
        self.general = ["ID", "First name", "Last name", 'Title', 'Start Date', 'Email', 'Phone', 'Department']
        self.personal = ["Address", "City", "State", "Zip", "Classification", "PayMethod", "Salary", "Hourly", "Commission", 'Privilege']
        self.sensitive = ["Route", "Account"]

        #put any information you want to be public in the employee dictionary
        self.privilege_access = {
            "administrator": self.quick_attribute,
            "employee": {'First name': self.first_name, 'Last name': self.last_name, 'Email': self.email, 'Phone': self.phone, 'Title': self.title}
        }
        
        self.set_classification(self, data[7])

    @staticmethod
    def set_classification(self, classification, salary = -1, commission = -1, hourly = -1):
        #sets the classification of the employee to the given classification class
        if salary == -1:
            salary = self.salary
        if commission == -1:
            commission = self.commission
        if hourly == -1:
            hourly = self.hourly
        if classification == '1':
            self.classification = Salaried(salary)
        elif classification == '2':
            self.classification = Commissioned(salary, commission)
        elif classification == '3':
            self.classification = Hourly(hourly)
        self.quick_attribute['Classification'] = str(self.classification)

    def issue_payment(self):
        payment = self.classification.compute_payment()
        return (f"Mailing {payment} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zip}\n")

    def match_search(self, value, attribute):
        #checks to see if the employee has the given value for the given attribute
        #returns true even if the value is just a slice of the given attribute
        if value.lower() in self.quick_attribute[attribute].lower():
            return True
        return False

    def change(self, attribute, value):
        #changes the values of the given attributes in the quick_attribute template
        if type(self.quick_attribute[attribute]) == type(value):
            self.quick_attribute[attribute] = value
        else:
            raise ValueError("The given value is not of the correct type")

    def update(self, File):
        #updates all self values to reflect the quick_attribute template
        #also write the updated values to the employees CSV file
        self.id = self.quick_attribute['ID']
        self.last_name = self.quick_attribute['last_name']
        self.first_name = self.quick_attribute['first_name']
        self.address = self.quick_attribute['Address']
        self.city = self.quick_attribute['City']
        self.state = self.quick_attribute['State']
        self.zip = self.quick_attribute['Zip']
        if str(self.classification) != self.quick_attribute['Classification']:
            self.set_classification(self.quick_attribute['Classification'])
            if str(self.classification) == '2':
                Payroll.process_receipts()
            elif str(self.Classification) == '3':
                Payroll.process_timecards()
        self.paymethod = self.quick_attribute['PayMethod']
        self.salary = self.quick_attribute['Salary']
        self.commission = self.quick_attribute['Commission']
        self.hourly = self.quick_attribute['Hourly']
        self.route = self.quick_attribute['Route']
        self.account = self.quick_attribute['Account']

        line_num = 0
        for i in Payroll.EMPLOYEES.employees:
            if i == self.id:
                break
            line_num += 1
        file = pd.read_csv(DIR_ROOT + "\\" + File)
        for i in self.quick_attribute:
            if i != 'last_name' and i != 'first_name':
                file.loc[line_num, i] = self.quick_attribute[i]
            elif i == 'last_name':
                file.loc[line_num, 'Name'] = self.first_name + ' ' + self.last_name
        file.to_csv(DIR_ROOT + "\\employees.csv", index=False)



    def __str__(self):
        printer = ''
        printer += str(self.id) + ' : '
        printer += self.last_name + ' ' + self.first_name + ', '
        printer += self.address + ', ' + self.city + ' ' + self.state + ' ' + self.zip
        printer += '\n'
        return printer

class Classification(ABC):
    #abstract class for the classifications
    @abstractmethod
    def compute_payment(self):
        pass

class Salaried(Classification):
    #Salaried employees get payed by salery
    def __init__(self, salary):
        self.salary = float(salary)

    def compute_payment(self):
        return round(self.salary / 24, 2)

    def __str__(self):
        return "1"

    def type(self):
        return "Salary"


class Commissioned(Salaried):
    #commissioned employees get payed by salery and by a commission per receipt
    def __init__(self, salary, commission):
        super().__init__(salary)
        self.commission_rate = float(commission)
        self.receipts = []

    def add_receipt(self, receipt):
        self.receipts.append(float(receipt))

    def compute_payment(self):
        pay = (sum(self.receipts) * (self.commission_rate/100)) + (self.salary / 24)
        self.receipts = []
        pay = round(pay, 2)
        return pay

    def __str__(self):
        return "2"

    def type(self):
        return "Salary"


class Hourly(Classification):
    #hourly employees get payed according to timecards
    def __init__(self, hourly):
        self.hourly_rate = float(hourly)
        self.time_cards = []

    def add_timecard(self, timecard):
        self.time_cards.append(float(timecard))

    def compute_payment(self):
        payment = 0
        for timecard in self.time_cards:
            payment += timecard * self.hourly_rate
        payment = round(payment, 2)
        return payment

    def __str__(self):
        return "3"

    def type(self):
        return "Salary"