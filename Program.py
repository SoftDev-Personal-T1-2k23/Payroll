#> Program.py
# Initializes the program and its components
from UI.UICore import UICore
import payroll

# Initialize backend components
payroll.load_employees()

# Initialize UICore
ui_core = UICore(start_page="login")
