import payroll
import hashlib


class UIDataInterface:
    def __init__(self):
        pass

    def is_logged_in(self):
        return True
    
    def attempt_login(self, user:str, password:str):
        employees = payroll.EMPLOYEES.employees
        
        '''
        passwords are stored as hashed values. There is no decoding function. 
        Instead of decoding the stored password we hash the given password and check to see if it matches what was stored

        '''
        password = self.hash_password(password)
        #first check if the employees name exists in the database
        if self.find_employee(employees, user):
            #get the users id
            user_id = self.get_id(employees, user)
            #user the id to get the employees password and check it against the users input
            if password == employees[user_id].password:            
                return True
        return False



    #helper function for checking if an employee exists via the username
    def find_employee(self, employees, user):
        for key in employees:
            if user == employees[key].first_name:
                return key
        return False


    #helper function for getting the id of a user via the username
    def get_id(self, employees, user):
        for key in employees:
            if user == employees[key].first_name:
                return key
        return None

    #function for hashing a password
    def hash_password(self, password):
        # Encode the password string as UTF-8 bytes
        password_bytes = password.encode('utf-8')

        # Generate the SHA-256 hash of the password bytes
        sha256_hash = hashlib.sha256(password_bytes)

        # Convert the hash to a hexadecimal string
        hash_str = sha256_hash.hexdigest()

        return hash_str