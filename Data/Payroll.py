"""
Tyler Anderson
5/2/22
CS1410-004
This function will take a number of text files and be able to issue pay to a number of employees. Each employee will
have their own object that contains all of their relevant information. Their pay will be calculated on whether they are
salaried, commissioned, or hourly and be output to a text file.
"""
import os
import csv
import hashlib
import pandas as pd
from Data.FileConstants import DIR_ROOT
from Data.Employee import Employee
from Data.FileReader import FileReader
from Data.FileWriter import FileWriter

PAY_LOGFILE = 'paylog.txt'
DATABASE = 'employees.csv'

EMPLOYEES = None
USER = None
TARGET_EMPLOYEE = None #this is to keep track of what the view and edit pages should display

class Database:
    #contains a dictionary of all employees with their id as a key, as well as expedient methods
    def __init__(self, data):
        self.employees = {}
        self.data = data
        for i in data:
            employee = Employee(i)
            self.add_employee(employee)

    def add_employee(self, employee):
        #takes an employee object and adds it to the employees dictionary
        self.employees[employee.id] = employee

    def change_employee(self, id, change_list, file = "employees.csv"):
        #takes an id and attributes to change, stored in a list of tuples, then changes the values of said atributes for the target employee
        #tuples are comprised of the quick_atribute reference to the target attribute, then the value it will be changed to
        #this will change the csv document as well
        employee = self.find_employee(id)
        for i in change_list:
            employee.change(i[0], i[1])
        employee.update(file)

    def find_employee(self, value, attribute = 'ID'):
        #takes an attribute to search by, then returns all employees who match the given value
        #defaults to a search by id
        if attribute == 'ID':
            try:
                return self.employees[int(value)]
            except:
                raise ValueError('there is no employee with id number: ' +  str(value))
        matches = []
        for i in self.employees:
            if self.employees[i].match_search(value, attribute):
                matches.append(self.employees[i])
        return matches

    def __str__(self):
        #prints the IDs of every employee in the database
        printer = ""
        for i in self.employees:
            printer += str(self.employees[i])
        return printer


def hash_password(password):
    # Encode the password string as UTF-8 bytes
    password_bytes = password.encode('utf-8')

    # Generate the SHA-256 hash of the password bytes
    sha256_hash = hashlib.sha256(password_bytes)

    # Convert the hash to a hexadecimal string
    hash_str = sha256_hash.hexdigest()

    return hash_str

def initialize_passwords():
    '''
    this function is for creating the hashed passwords based on the user id if the password has not yet been initialized
    '''
    # Read the CSV file
    csv_data = FileReader.read_csv('employees.csv')
    # Check for null passwords & Add new ones if necessary
    for row in csv_data.rows:
        # Check if current pass exists
        curr_pass = csv_data.get_row_value(row, "Password")
        if curr_pass is None:
            # Get new password
            user_id = csv_data.get_row_value(row, "ID")
            new_pass = hash_password(user_id)
            # Set new password
            csv_data.set_row_value(row, "Password", new_pass)
    # Update CSV file contents
    FileWriter.write_csv('employees.csv', csv_data)

    #first figure out how many employees there are
    # with open('employees.csv', mode='r') as file:
    #     # Create a reader object
    #     reader = csv.reader(file)
    #     # Use a generator expression to count the number of non-empty rows
    #     num_rows = sum(1 for row in reader if any(row))
    # num_rows -= 1 #subtract 1 for the header row
    
    # for i in range(num_rows):
    #     if pd.isnull(df.iloc[i, 13]):
    #         #get the id
    #         user_id = df.iloc[i, 0]
    #         password = hash_password(str(user_id))
          
    #         # Edit the cell at row 4, column 13
    #         df.iloc[i, 13] = password

    # Write the updated DataFrame back to the CSV file
    # df.to_csv('employees.csv', index=False)

 #helper function for checking if an employee exists via the username
def find_employee(employees, user):
    for key in employees:
        if user == employees[key].first_name:
            return key
    return False

def save_info(entry_dict):
    '''
    takes a dictionary of entry objects as a parameter
    the dictionary contains field names and the associated entry for that field. 
    '''

    #make a dictionary mapping field names to column locations in the csv file
    csv_location = {
        'ID': 0,
        'Last name': 1,
        'First name': 1,
        'Address': 2,
        'City': 3,
        'State': 4,
        'Zip': 5,
        'Classification': 6,
        'PayMethod': 7,
        'Salary': 8,
        'Hourly': 9,
        'Commission': 10,
        'Route': 11,
        'Account': 12,
        'Password': 13,
        'Start Date': 14,
        'Privilege': 15,
        'Department': 16,
        'Email': 17,
        'Phone': 18,
        'Title': 19

    }


    # Get the information from the fields and save it to a file or database
    df = pd.read_csv('employees.csv')
    for field_name in entry_dict:
        #skip the last name since that is combined with the first
        if field_name == 'Last name':
            continue
        entry = entry_dict[field_name]
        row = get_row(EMPLOYEES.employees, TARGET_EMPLOYEE.first_name)
        col = csv_location[field_name]
        #handle for unique case of first and last name bieng combined in one spot
        if field_name == "First name":
            df.iloc[row, col] = entry_dict['First name'].get() + " " + entry_dict['Last name'].get()
        else:
            df.iloc[row, col] = entry.get()

    # first_name = entry_list[0].get()
    # last_name = entry_list[1].get()
    # address = entry_list[2].get()
    # city = entry_list[3].get()
    # state = entry_list[4].get()
    # zip_code = entry_list[5].get()
    # route = entry_list[6].get()
    # account = entry_list[7].get()

    # row = get_row(EMPLOYEES.employees, TARGET_EMPLOYEE.first_name)
    # # Do something with the information (e.g. save to a file or database)
    # df = pd.read_csv('employees.csv')
    # df.iloc[row, 1] = first_name + " " + last_name
    # df.iloc[row, 2] = address
    # df.iloc[row, 3] = city
    # df.iloc[row, 4] = state
    # df.iloc[row, 5] = zip_code
    # df.iloc[row, 11] = route
    # df.iloc[row, 12] = account
    df.to_csv('employees.csv', index=False)



#helper function for getting the id of a user via the first name
def get_id(employees, user):
    for key in employees:
        if user == employees[key].first_name:
            return key
    return None

#returns the row in the csv file where a users info is stored via the first name
def get_row(employees, user):
    #created to help when saving the password and other data to the csv
    target_row = 0
    for key in employees:
        if user == employees[key].first_name:
            return target_row
        target_row += 1
    return None

def set_data(row, col, data):
    df = pd.read_csv('employees.csv')
    df.iloc[row, col] = data
    df.to_csv('employees.csv', index=False)

    

def load_employees(data = 'employees.csv'):
    #reads all employees in from the indicated csv file. Defaults employees.csv

    #before loading the employees make sure they have passwords
    initialize_passwords()

    raw = []
    global EMPLOYEES
    with open(DIR_ROOT + "\\" + data, 'r') as file:
        for line in file:
            try:
                temp = line.strip().split(',')
                temp[0] = int(temp[0])
                raw.append(temp)
            except:
                pass
        EMPLOYEES = Database(raw)





def process_timecards():
    #reads all timecards from the indicated scv file, and gives them to the nessesary hourly employees.
    #Sallaried and Commissioned employees will not receive timecards
    #defaults timecards.scv
    with open(DIR_ROOT + "\\timecards.csv", 'r') as t:
        for line in t:
            line = line.strip().split(',')
            emp = EMPLOYEES.find_employee(int(line.pop(0)))
            for timecard in line:
                if str(emp.classification) == '3':
                    emp.classification.add_timecard(float(timecard))


def process_receipts():
    #reads all receipts from the indicated scv file, and gives them to the nessesary commissioned employees.
    #Sallaried and hourly employees will not receive receipts
    #defaults receipts.scv
    with open(DIR_ROOT + "\\receipts.csv", 'r') as r:
        for line in r:
            line = line.strip().split(',')
            emp = EMPLOYEES.find_employee(int(line.pop(0)))
            for receipt in line:
                if str(emp.classification) == '2':
                    emp.classification.add_receipt(receipt)


def run_payroll():
    global PAY_LOGFILE
    if os.path.exists(DIR_ROOT + "\\" + PAY_LOGFILE):
        os.remove(DIR_ROOT + "\\" + PAY_LOGFILE)
    issue = []
    for emp in EMPLOYEES.employees:
        issue.append(EMPLOYEES.employees[emp].issue_payment())
    with open(DIR_ROOT + "\\" + PAY_LOGFILE, 'w') as pay:
        for i in issue:
            pay.write(i)


def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

if __name__ == "__main__":
    try:
        main()
    except:
        input("[Data] Error: Enter to exit...")