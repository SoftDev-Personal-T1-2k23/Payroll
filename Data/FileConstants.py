import os
import sys

#DIR_ROOT = os.path.abspath(os.path.join(__file__, "..\\.."))
DIR_ROOT = os.path.abspath(os.path.join(os.path.abspath(sys.executable), "..\\"))
# in some cases the above code goes to the wrong spot. This happens when its not compiled as an executable. For testing purposes we need this code 
# If the csv file isn't there this will use the current working directory instead
file_path = DIR_ROOT + "\\" + "employees.csv"
if not(os.path.isfile(file_path)):
    # print("using cwd")
    DIR_ROOT = os.getcwd()

PATH_PAYLOG = os.path.join(DIR_ROOT, "paylog.txt")
PATH_EMPLOYEE_DATA = os.path.join(DIR_ROOT, "employees.csv")