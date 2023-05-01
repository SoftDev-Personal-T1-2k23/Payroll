"""A data management class"""

from Data.FileConstants import PATH_EMPLOYEE_DATA
from Data.file_reader import FileReader
from Data.FileWriter import FileWriter
from Data.Employee import Employee

EMPLOYEES = None

class Database:
    #contains a dictionary of all employees with their id as a key, as well as expedient methods
    def __init__(self):
        emp_csv_data = FileReader.read_csv(PATH_EMPLOYEE_DATA)

        self.employee_csv_data = emp_csv_data
        self.employees = {}

        # Create employees
        for row in emp_csv_data.rows:
            employee = Employee(emp_csv_data.columns, row)
            self.add_employee(employee)

    def update_employee(self, employee):
        """Update an employees info stored within the database"""
        assert(employee is not None)
        # Load the CSV
        csv_data = FileReader.read_csv(PATH_EMPLOYEE_DATA)
        csv_id_column_index = csv_data.columns.index("ID")
        # Find the employee row
        emp_csv_row = None
        for row in csv_data.rows:
            row_emp_id = row[csv_id_column_index]
            if row_emp_id == employee.data["ID"]:
                emp_csv_row = row
                break
        # Update all information
        for (i, v) in enumerate(emp_csv_row):
            row_val_title = csv_data.columns[i]
            emp_csv_row[i] = employee.data[row_val_title]
        # Save the CSV
        FileWriter.write_csv(PATH_EMPLOYEE_DATA, csv_data)

    def add_employee(self, employee):
        assert(employee is not None)
        #takes an employee object and adds it to the employees dictionary
        self.employees[employee.data["ID"]] = employee

    def change_employee(self, id, change_list, file = "employees.csv"):
        assert(id is not None)
        assert(change_list is not None)
        assert(file is not None)
        #takes an id and attributes to change, stored in a list of tuples, then changes the values of said atributes for the target employee
        #tuples are comprised of the quick_atribute reference to the target attribute, then the value it will be changed to
        #this will change the csv document as well
        employee = self.find_employee(id)
        for i in change_list:
            employee.change(i[0], i[1])
        employee.update(file)

    def find_employee(self, value, attribute = 'ID'):
        assert(value is not None)
        assert(attribute is not None)
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