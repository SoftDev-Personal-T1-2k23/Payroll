"""A script with the purpose of initializing all program components"""

#> Program.py
# Initializes the program and its components
from UI.ui_core import UICore
from Data import Payroll

# Initialize backend components
Payroll.initialize_passwords()
Payroll.load_database()

# Initialize UICore
ui_core = UICore(start_page="login")
