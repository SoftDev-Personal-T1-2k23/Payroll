#> Program.py
# Initializes the program and its components
from UI.UICore import UICore
import Data.Payroll as Payroll

# Initialize backend components
Payroll.initialize_passwords()
Payroll.load_database()

# Initialize UICore
ui_core = UICore(start_page="login")
