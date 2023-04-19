"""A file containing program state and utility functions"""
import os
import hashlib
from Data.FileConstants import DIR_ROOT, PATH_EMPLOYEE_DATA
from Data.FileReader import FileReader
from Data.FileWriter import FileWriter
from Data.Database import Database

USER = None
TARGET_EMPLOYEE = None #this is to keep track of what the view and edit pages should display

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
    print(PATH_EMPLOYEE_DATA)
    csv_data = FileReader.read_csv(PATH_EMPLOYEE_DATA)
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
    FileWriter.write_csv(PATH_EMPLOYEE_DATA, csv_data)

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
        if user == employees[key].data["FirstName"]:
            return key
    return False

# make a dictionary mapping field names to column locations in the csv file
# EMPLOYEE_ENTRY_LOOKUP = {
#     'ID': 0,
#     'LastName': 1,
#     'FirstName': 1,
#     'Address': 2,
#     'City': 3,
#     'State': 4,
#     'Zip': 5,
#     'Classification': 6,
#     'PayMethod': 7,
#     'Salary': 8,
#     'Hourly': 9,
#     'Commission': 10,
#     'Route': 11,
#     'Account': 12,
#     'Password': 13,
#     'Start Date': 14,
#     'Privilege': 15,
#     'Department': 16,
#     'Email': 17,
#     'Phone': 18,
#     'JobTitle': 19
# }
def save_info(field_data):
    '''
    takes a dictionary of entry objects as a parameter
    the dictionary contains field names and the associated entry for that field. 
    '''
    # Get CSV data & Locate the target employee
    csv_data = FileReader.read_csv(PATH_EMPLOYEE_DATA)
    csv_row = None
    col_index = csv_data.get_column_index("ID") # It's zero, but this is prob safer
    for row in csv_data.rows:
        if row[col_index] == TARGET_EMPLOYEE.data["ID"]:
            csv_row = row
    # Return if the target employee does not exist
    if not csv_row:
        print("Error: Failed to save employee info; employee not found")
        return

    # Update the target_employee & CSV data
    for pair in field_data:
        field_key = pair[0]
        field_val = pair[1]
        
        # Exceptions
        if field_key == "FirstName":
            row[1] = field_val
            TARGET_EMPLOYEE.data["FirstName"] = field_val
            continue
        elif field_key == "LastName":
            row[1] += f" {field_val}"
            TARGET_EMPLOYEE.data["LastName"] = field_val
            continue
        
        # Update values
        col_index = csv_data.get_column_index(field_key)
        row[col_index] = field_val
        TARGET_EMPLOYEE.data[field_key] = field_val

    
    # Set values in CSV file
    FileWriter.write_csv(PATH_EMPLOYEE_DATA, csv_data)

    # # Get the information from the fields and save it to a file or database
    # df = pd.read_csv('employees.csv')
    # for field_name in entry_dict:
    #     #skip the last name since that is combined with the first
    #     if field_name == 'Last name':
    #         continue
    #     entry = entry_dict[field_name]
    #     row = get_row(EMPLOYEES.employees, TARGET_EMPLOYEE.data["FirstName"])
    #     col = EMPLOYEE_ENTRY_LOOKUP[field_name]
    #     #handle for unique case of first and last name bieng combined in one spot
    #     if field_name == "First name":
    #         df.iloc[row, col] = entry_dict['First name'].get() + " " + entry_dict['Last name'].get()
    #     else:
    #         df.iloc[row, col] = entry.get()

    # # first_name = entry_list[0].get()
    # # last_name = entry_list[1].get()
    # # address = entry_list[2].get()
    # # city = entry_list[3].get()
    # # state = entry_list[4].get()
    # # zip_code = entry_list[5].get()
    # # route = entry_list[6].get()
    # # account = entry_list[7].get()

    # # row = get_row(EMPLOYEES.employees, TARGET_EMPLOYEE.first_name)
    # # # Do something with the information (e.g. save to a file or database)
    # # df = pd.read_csv('employees.csv')
    # # df.iloc[row, 1] = first_name + " " + last_name
    # # df.iloc[row, 2] = address
    # # df.iloc[row, 3] = city
    # # df.iloc[row, 4] = state
    # # df.iloc[row, 5] = zip_code
    # # df.iloc[row, 11] = route
    # # df.iloc[row, 12] = account
    # df.to_csv('employees.csv', index=False)



#helper function for getting the id of a user via the first name
def get_id(employees, user):
    for key in employees:
        if user == employees[key].data["FirstName"]:
            return key
    return None

#returns the row in the csv file where a users info is stored via the first name
def get_row(employees, user):
    #created to help when saving the password and other data to the csv
    target_row = 0
    for key in employees:
        if user == employees[key].data["FirstName"]:
            return target_row
        target_row += 1
    return None

# not used anywhere in the code
# def set_data(row, col, data):
#     df = pd.read_csv('employees.csv')
#     df.iloc[row, col] = data
#     df.to_csv('employees.csv', index=False)


def load_database():
    """Initialize the database"""
    #Startup the database and store a hoisted reference
    global EMPLOYEES
    EMPLOYEES = Database()

def load_employees(data = PATH_EMPLOYEE_DATA):
    #reads all employees in from the indicated csv file. Defaults employees.csv
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