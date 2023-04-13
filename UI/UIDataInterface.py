import payroll

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
        return payroll.USER.id
    
    def get_access_level(self) -> str:
        """Return the current user's access level
        
        Returns:
            access_level: The user's access level
        """
        # Request the current user's access level from the backend
        access_level = payroll.USER.privilege
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
            print(user_id)
            print(user)
            #user the id to get the employees password and check it against the users input
            if password == employees[user_id].password:
                print("PASSWORD MATCH")
                payroll.USER = employees[user_id] 
                #if all the information matches return True  
                return True
            else:
                print("PASSWORD MISMATCH")
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
    
    def get_employees(self):
        """Get a collection of employees from the database
        
            Returns:
                employees: A collection of all(?) employees
        """
        # Return a collection of employees
        return payroll.EMPLOYEES.employees

    def get_target_employee(self):
        """Return the current target employee

            Returns:
                target_employee: The current target employee's information
        """
        # Return the target employee
        return payroll.TARGET_EMPLOYEE

    def get_target_employee_information(self, employee):
        """Return the current target employee's information

            Params:
                employee: The employee to get information about
            Returns:
                target_employee: The current target employee's information
        """
        #check if the user is viewing themself
        target_dictionary = {}
        if payroll.USER.id == employee.id:
            target_dictionary = employee.editable_by_user
            #Decide what to display based on the privilege level
        else:
            #set the target_dictionary to whatever dictionary is associated with the users privilege level via the privilege_access dictionary
            target_dictionary = employee.privilege_access[payroll.USER.privilege]
        return target_dictionary
    
    def set_target_employee(self, employee) -> bool:
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
            employee = payroll.USER
        if employee is not None:
            # print("EMPLOYEE PROVIDED")
            payroll.TARGET_EMPLOYEE = employee
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
        payroll.save_info(emp_info)
        return True

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

    def set_new_password(self, password:str) -> bool:
        """Set a user's new password
            Params:
                password: New password to use
            Returns:
                success: Whether the change was successful
        """
        hashed_pass = payroll.hash_password(password)
        payroll.USER.password = hashed_pass
        row = payroll.get_row(payroll.EMPLOYEES.employees, payroll.USER.first_name)
        print("saving password: " + str(row))
        payroll.set_data(row, 13, hashed_pass)
        return True
