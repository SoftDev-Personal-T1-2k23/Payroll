import os

import Data.Payroll as Payroll
from Data.Database import EMPLOYEES
from Data.FileWriter import FileWriter
from Data.FileConstants import DIR_ROOT
from Data.csv_data import CSVData
from Data.Employee import Employee

class UIDataInterface:
    """An interface for communication with non-UI parts of the program"""

    def is_logged_in(self) -> bool:
        """Return whether the current user is logged in
         
          Returns:
              is_logged_in: Whether the current user is logged in or not
        """
        # Request the current login status from the backend
        is_logged_in = True
        # Return the login status
        return is_logged_in

    def get_user_id(self) -> str:
        """Gets the current users's employee ID
        
            Returns:
                user_id: The current user's employee ID
        """
        # Return the login user's ID
        return Payroll.USER.data["ID"]
    
    def get_access_level(self) -> str:
        """Return the current user's access level
        
        Returns:
            access_level: The user's access level
        """
        # Request the current user's access level from the backend
        access_level = Payroll.USER.data["Privilege"]
        # Return access level
        return access_level

    def attempt_logout(self):
        """Attempt to logout of the program
        
            Returns:
                is_logged_out: Whether the current user is logged out or not
        """
        # Perform logout
        return True


    def attempt_login(self, user:str, password:str):
        """Attempt to login with a provided username/id and password
         
          Params:
              username: The user's username
              password: The user's password
          Returns:
              is_logged_in: Whether the current user is logged in or not
        """

        '''
        passwords are stored as hashed values. There is no decoding function. 
        Instead of decoding the stored password we hash the given password and check to see if it matches what was stored

        '''
        employees = Payroll.EMPLOYEES.employees

        # Attempt login with a username/id and password (via backend)
        password = Payroll.hash_password(password)

        #first check if the employees name exists in the database
        if Payroll.find_employee(employees, user):
            # print("FOUND EMPLOYEE")
            #get the users id
            user_id = Payroll.get_id(employees, user)

            #user the id to get the employees password and check it against the users input
            if password == employees[user_id].data["Password"]:
                print("PASSWORD MATCH")
                Payroll.USER = employees[user_id] 
                #if all the information matches return True  
                return True
            else:
                print("PASSWORD MISMATCH")
        # else:
        #     print("FAILED TO FIND EMPLOYEE")
        #return false if the information wasn't validated
        return False

    
    def find_employees(self, search_filters:dict) -> dict:
        """Find and return a collection of employees from the database
         
          Params:
              search_filters: A collection of search filters
          Returns:
              matching_employees: A collection of employees that match the search filters
        """
        # Request a collection of employees that match specified search filters (via backend)
        # Return the resulting collection
    
    def get_employees(self):
        """Get a collection of employees from the database
        
            Returns:
                employees: A collection of all(?) employees
        """
        # Return a collection of employees
        return Payroll.EMPLOYEES.employees

    def get_user(self):
        """Get the current program user (logged in employee)
        
            Returns:
                current_user: The current employee logged in
        """
        return Payroll.USER

    def get_target_employee(self):
        """Return the current target employee

            Returns:
                target_employee: The current target employee's information
        """
        # Return the target employee
        return Payroll.USER if Payroll.TARGET_EMPLOYEE is None else Payroll.TARGET_EMPLOYEE
    def make_new_employee(self, emp_info:dict):
        """Creates space for a new employee

            
        """
        Payroll.make_new_employee(emp_info)

    def validate_entries(self, emp_info:dict):
        #make a dictionary matching labels to validation 
        print(emp_info)

    def set_target_employee(self, employee=None) -> bool:
        """Sets the payroll's target employee
            Params:
                the function has to know what employee should be targeted. 
                the target employee will change based on which employee the user is trying to view. 
                If the user clicks the view button for Teagan then a page for Teagan should pop up
            Returns:
                success: Whether the operation was successful
        """
        #if there was an employee provided that set the target
        if employee == None:
            employee = Payroll.USER
        if employee is not None:
            # print("EMPLOYEE PROVIDED")
            Payroll.TARGET_EMPLOYEE = employee
            return True
        return False
        
    def add_employee(self, emp_id:str, emp_info:dict) -> bool:
        """Add an employee with the specified information to the database
        
        Params:
            emp_id: The employee id to use
            emp_info: The new employee's information
        Returns:
            success: Whether the new employee was successfully added or not
        """
        # Pass the employee id and employee info to the databae (via backend)
        # Return whether the addition was successful

    def update_employee(self, emp_id:str, emp_info:dict) -> bool:
        """Update an existing employee's information
        
        Params:
            emp_id: The employee id to use
            emp_info: The employee information to update
        Returns:
            success: Whether the new employee information was applied successfully or not
        """
        # Request a change to an employee via employee id and the changes desired (via backend)
        # Return whether the update was successful
    
    def update_employee_info(self, emp_info:dict) -> bool:
        """Update an existing employee's information
        
        Params:
            emp_id: The employee id to use
            emp_info: The employee information to update
        Returns:
            success: Whether the new employee information was applied successfully or not
        """
        Payroll.save_info(emp_info)
        return True

    def archive_employee(self, emp) -> bool:
        """Set an existing employee as archived
         
          Params:
              emp: The employee
          Returns:
              success: Whether the employee was archived successfully or not
        """
        # Check that we aren't archiving ourself
        if emp == self.get_user():
            return False
        # Archive the employee
        result = emp.archive()
        # Update the database & CSV
        Payroll.EMPLOYEES.update_employee(emp)
        # Return whether the archival was successful
        return result

    def unarchive_employee(self, emp) -> bool:
        """Set an existing employee as unarchived
         
          Params:
              emp: The employee
          Returns:
              success: Whether the employee was archived successfully or not
        """
        # Check that we aren't unarchiving ourself
        if emp == self.get_user():
            return False
        # Unarchive the employee
        result = emp.unarchive()
        # Update the database & CSV
        Payroll.EMPLOYEES.update_employee(emp)
        # Return whether the archival was successful
        return result

    def generate_pay_report(self, emp_id:str) -> bool:
        """Generate a pay report for a particular employee
         
          Params:
              emp_id: The employee id to use
          Returns:
              success: Whether the pay report was generated and exported successfully or not
        """
        # Request for a pay report to be generated and exported (via backend)
        # Return whether the process was successful

    def export_csv(self, file_name:str, emp_list:list) -> bool:
        """Generate and export a csv file containing employees' information
        
        Params:
            file_name: The file name to export with
            emp_list: The list employee ids to use
        Returns:
            success: Whether the pay csv data was generated and exported successfully or not
        """
        # Request for a csv file containing a collection of employee information be generated and exported (via backend)
        export_path = os.path.join(DIR_ROOT, f"{file_name}.csv")

        # Assemble CSV data
        fake_data_keys = Employee.get_fake_data_keys()
        csv_column_count = -1
        csv_columns = []
        csv_rows = []
        for col_title in emp_list[0].data.keys(): # Unsafe key ordering; may not match employees.csv
            if not col_title in fake_data_keys:
                csv_columns.append(col_title)
        csv_column_count = len(csv_columns)

        for emp in emp_list:
            emp_row = []
            for (i, emp_val) in enumerate(emp.data.values()):
                if i >= csv_column_count: break
                emp_row.append(emp_val)
            csv_rows.append(emp_row)
        
        csv_data = CSVData(csv_columns, csv_rows)
        # Write to new file
        FileWriter.write_csv(export_path, csv_data)
        # Return whether the process was successful
        return True

    def set_new_password(self, employee, password:str) -> bool:
        """Set a user's new password
            Params:
                password: New password to use
            Returns:
                success: Whether the change was successful
        """
        return Payroll.set_password(employee, password)
