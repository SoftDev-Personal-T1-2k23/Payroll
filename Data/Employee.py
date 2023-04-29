"""An employee class and related employee classifications"""
from abc import ABC, abstractmethod

import Data.Payroll as Payroll

DATA_ACCESS_VIEW = {# Which privilege levels have access to view what data
    "public": [
        "FirstName", "LastName", "JobTitle", "ID", "StartDate", "Department"
    ],
    "private": [
        "Address", "City", "State", "Zip", "Route", "Account", "Email", "Phone", "ClassificationId", "Salary", "PayMethod",
        "Commission", "Route", "Account", "Privilege"
    ],
    "admin": [
        "IsArchived"
    ]
}
DATA_ACCESS_MODIFY = {# Which privlege levels have access to edit what data
    "public": [],
    "private": [
        "Address", "City", "State", "Zip", "Route", "Account", "Email", "Phone", "ClassificationId", "Salary", "PayMethod",
        "Commission", "Route", "Account"
    ],
    "admin": [
        "FirstName", "LastName", "ID", "JobTitle", "StartDate", "Department", "Privilege", "IsArchived"
    ]
}
DATA_PRESENTATION = {# Where to display what data
    "public": [
        "FirstName", "LastName", "JobTitle", "ID", "StartDate", "Department"
    ],
    "private": [
        "Address", "City", "State", "Zip", "Route", "Account", "Email", "Phone", "ClassificationId", "Salary", "PayMethod",
        "Commission", "Route", "Account"
    ],
    "admin": [
        "Privilege", "IsArchived"
    ]
}

def format_field_data(data):
    """Format data to match the presentation constant (DATA_PRESENTATION)"""
    data_new = {
        "public": [],
        "private": [],
        "admin": []
    }
    for (_, field_list) in data.items():
        for field_pair in field_list:
            field_title = field_pair[0]
            for priv_group_2 in data_new.keys():
                if field_title in DATA_PRESENTATION[priv_group_2]:
                    data_new[priv_group_2].append(field_pair)
                    break
    return data_new


class Employee:
    #Employee object contain their name, id, payment info, classification info, and adress

    def __init__(self, column_titles, data_values):
        # name_raw = data[1].split(' ')
        # name_join  = ''

        # Setup employee data fields
        self.data = {} # Stores all CSV related data
        column_title_count = len(column_titles)
        for i in range(column_title_count):
            column_title = column_titles[i]
            data_value = data_values[i]

            self.data[column_title] = data_value

        name_components = data_values[column_titles.index("Name")].split(" ")
        self.data["FirstName"] = name_components[0]
        self.data["LastName"] = name_components[-1]

        # Setup employee fields
        self.classification = None
        self.set_classification(self, self.data["ClassificationId"])

        # self.id = data[0]
        # self.last_name = name_raw.pop()
        # self.first_name = name_join.join(name_raw)
        # self.address = data[2]
        # self.city = data[3]
        # self.state = data[4]
        # self.zip = data[5]
        # self.classification = None
        # self.paymethod = data[6]
        # self.salary = data[8]
        # self.commission = data[9]
        # self.hourly = data[10]
        # self.route = data[11]
        # self.account = data[12]
        # self.password = data[13]
        # self.start_date = data[14]
        # self.privilege = data[15]
        # self.department = data[16]
        # self.email = data[17]
        # self.phone = data[18]
        # self.title = data[19]
        
        # self.quick_attribute = {
        # #use as a reference for which attribute corrosponds to which number
        #     'ID': self.data["ID"],
        #     'First name': self.data["FirstName"],
        #     'Last name': self.data["LastName"],
        #     'Address': self.data["Address"],
        #     'City': self.data["City"],
        #     'State': self.data["State"],
        #     'Zip': self.data["Zip"],
        #     'Classification': str(self.classification),
        #     'PayMethod': self.data["PayMethod"],
        #     'Route': self.data["Route"],
        #     'Account': self.data["Account"],
        #     'Start Date': self.data["StartDate"],
        #     'Privilege': self.data["Privilege"],
        #     'Department': self.data["Department"],
        #     'Email': self.data["Email"],
        #     'Phone': self.data["Phone"],
        #     'JobTitle': self.data["JobTitle"],

        # }
        self.pay_type_dict = {
            "Salary": self.data["Salary"],
            "Hourly": self.data["Hourly"],
            "Commission": self.data["Commission"]
        }
        # self.editable_by_user = {
        # #use as a reference for which attribute corrosponds to which number
        #     'First name': self.data["FirstName"],
        #     'Last name': self.data["LastName"],
        #     'Address': self.data["Address"],
        #     'City': self.data["City"],
        #     'State': self.data["State"],
        #     'Zip': self.data["Zip"],
        #     'Route': self.data["Route"],
        #     'Account': self.data["Account"],
        #     'Email': self.data["Email"],
        #     'Phone': self.data["Phone"],
        #     'JobTitle': self.data["JobTitle"]
        # }
        
        # self.general = ["ID", "First name", "Last name", 'Title', 'Start Date', 'Email', 'Phone', 'Department']
        # self.personal = ["Address", "City", "State", "Zip", "Classification", "PayMethod", "Salary", "Hourly", "Commission", 'Privilege']
        # self.sensitive = ["Route", "Account"]

        #put any information you want to be public in the employee dictionary
        # self.privilege_access = {
        #     "administrator": self.quick_attribute,
        #     "employee": {'First name': self.data["FirstName"], 'Last name': self.data["LastName"], 'Email': self.data["Email"], 'Phone': self.data["Phone"], 'JobTitle': self.data["JobTitle"]}
        # }
    @staticmethod
    def get_fake_data_keys():
        """Get additional data created that isn't stored in employees.csv"""
        return ["FirstName", "LastName"]

    @staticmethod
    def set_classification(self, classification, salary = -1, commission = -1, hourly = -1):
        #sets the classification of the employee to the given classification class
        if salary == -1:
            salary = self.data["Salary"]
        if commission == -1:
            commission = self.data["Commission"]
        if hourly == -1:
            hourly = self.data["Hourly"]
        if classification == '1':
            self.classification = Salaried(salary)
        elif classification == '2':
            self.classification = Commissioned(salary, commission)
        elif classification == '3':
            self.classification = Hourly(hourly)
        # self.quick_attribute['Classification'] = str(self.classification)
    
    def archive(self):
        """Archive this employee
        
            Returns:
                archival_success: Whether archival was successful
        """
        self.data["IsArchived"] = "1"
        return True

    def unarchive(self):
        """Unarchive this employee
        
            Returns:
                unarchival_success: Whether unarchival was successful
        """
        self.data["IsArchived"] = "0"
        return True

    def get_viewable_field_data(self):
        """Return fields the current user has privilege to edit"""
        # Get accessible fields
        curr_user = Payroll.USER
        is_user = curr_user.data["ID"] == self.data["ID"]
        user_privilege = curr_user.data["Privilege"]
        is_admin = user_privilege == "administrator"

        public_accessible_fields = DATA_ACCESS_VIEW["public"]
        private_accessible_fields = DATA_ACCESS_VIEW["private"] if is_user or is_admin else None
        admin_accessible_fields = DATA_ACCESS_VIEW["admin"] if is_user or is_admin else None

        # Gather and return field data
        field_data = {
            "public": [(key, self.data[key]) for key in public_accessible_fields] if public_accessible_fields else [],
            "private": [(key, self.data[key]) for key in private_accessible_fields] if private_accessible_fields else [],
            "admin": [(key, self.data[key]) for key in admin_accessible_fields] if admin_accessible_fields else []
        }
        return format_field_data(field_data)
    
    def get_editable_field_data(self):
        """Return fields the current user has privilege to edit"""
        # Get accessible fields
        curr_user = Payroll.USER
        is_user = curr_user.data["ID"] == self.data["ID"]
        user_privilege = curr_user.data["Privilege"]
        is_admin = user_privilege == "administrator"
        
        public_accessible_fields = DATA_ACCESS_MODIFY["public"] if is_user or is_admin else None
        private_accessible_fields = DATA_ACCESS_MODIFY["private"] if is_user or is_admin else None
        admin_accessible_fields = DATA_ACCESS_MODIFY["admin"] if is_admin else None

        # Gather and return field data
        field_data = {
            "public": [(key, self.data[key]) for key in public_accessible_fields] if public_accessible_fields else [],
            "private": [(key, self.data[key]) for key in private_accessible_fields] if private_accessible_fields else [],
            "admin": [(key, self.data[key]) for key in admin_accessible_fields] if admin_accessible_fields else []
        }
        return format_field_data(field_data)

    def issue_payment(self):
        payment = self.classification.compute_payment()
        return f'Mailing {payment} to {self.data["FirstName"]} {self.data["LastName"]} at {self.data["Address"]} {self.data["City"]} {self.data["State"]} {self.data["Zip"]}\n'

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
        pass
        # Commented - I see no places this method is used and pandas is being removed
        # self.data["ID"] = self.quick_attribute['ID']
        # self.data["LastName"] = self.quick_attribute['last_name']
        # self.data["FirstName"] = self.quick_attribute['first_name']
        # self.data["Address"] = self.quick_attribute['Address']
        # self.data["City"] = self.quick_attribute['City']
        # self.data["State"] = self.quick_attribute['State']
        # self.data["Zip"] = self.quick_attribute['Zip']
        # if str(self.classification) != self.quick_attribute['Classification']:
        #     self.set_classification(self.quick_attribute['Classification'])
        #     if str(self.classification) == '2':
        #         Payroll.process_receipts()
        #     elif str(self.classification) == '3':
        #         Payroll.process_timecards()
        # self.data["PayMethod"] = self.quick_attribute['PayMethod']
        # self.data["Salary"] = self.quick_attribute['Salary']
        # self.data["Commission"] = self.quick_attribute['Commission']
        # self.data["Hourly"] = self.quick_attribute['Hourly']
        # self.data["Route"] = self.quick_attribute['Route']
        # self.data["Account"] = self.quick_attribute['Account']

        # line_num = 0
        # for i in Payroll.EMPLOYEES.employees:
        #     if i == self.data["ID"]:
        #         break
        #     line_num += 1
        
        # file = pd.read_csv(DIR_ROOT + "\\" + File)
        # for i in self.quick_attribute:
        #     if i != 'last_name' and i != 'first_name':
        #         file.loc[line_num, i] = self.quick_attribute[i]
        #     elif i == 'last_name':
        #         file.loc[line_num, 'Name'] = self.data["FirstName"] + ' ' + self.data["LastName"]
        # file.to_csv(DIR_ROOT + "\\employees.csv", index=False)



    def __str__(self):
        printer = ''
        printer += str(self.data["ID"]) + ' : '
        printer += self.data["LastName"] + ' ' + self.data["FirstName"] + ', '
        printer += self.data["Address"] + ', ' + self.data["City"] + ' ' + self.data["State"] + ' ' + self.data["Zip"]
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