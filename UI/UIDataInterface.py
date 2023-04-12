import payroll
import hashlib


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
    
    def get_access_level(self) -> int:
        """Return the current user's access level
        
        Returns:
            access_level: The user's access level
        """
        # Request the current user's access level from the backend
        access_level = 0
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
        employees = payroll.EMPLOYEES.employees

        # Attempt login with a username/id and password (via backend)
        password = payroll.hash_password(password)

        #first check if the employees name exists in the database
        if payroll.find_employee(employees, user):
            # print("FOUND EMPLOYEE")
            #get the users id
            user_id = payroll.get_id(employees, user)
            #user the id to get the employees password and check it against the users input
            if password == employees[user_id].password:
                # print("PASSWORD MATCH")
                payroll.USER = employees[user_id] 
                #if all the information matches return True  
                return True
            # else:
                # print("PASSWORD MISMATCH")
        # else:
            # print("FAILED TO FIND EMPLOYEE")
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

    def archive_employee(self, emp_id:str) -> bool:
        """Set an existing employee as archived
         
          Params:
              emp_id: The employee id to use
          Returns:
              success: Whether the employee was archived successfully or not
        """
        # Request that an employee via employee id be archived (via backend)
        # Return whether the archival was successful

    def generate_pay_report(self, emp_id:str) -> bool:
        """Generate a pay report for a particular employee
         
          Params:
              emp_id: The employee id to use
          Returns:
              success: Whether the pay report was generated and exported successfully or not
        """
        # Request for a pay report to be generated and exported (via backend)
        # Return whether the process was successful

    def csv_export(self, emp_id_list:list) -> bool:
        """Generate and export a csv file containing employees' information
        
        Params:
            emp_id_list: The list employee ids to use
        Returns:
            success: Whether the pay csv data was generated and exported successfully or not
        """
        # Request for a csv file containing a collection of employee information be generated and exported (via backend) 
        # Return whether the process was successful


