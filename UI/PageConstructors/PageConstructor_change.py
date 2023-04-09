import tkinter as tk
from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController
import payroll
BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    ttk.Style().configure("Indent.TFrame", background="#CCC")
    ttk.Style().configure("Indent.TLabel", background="#CCC")
    ttk.Style().configure("Middle.TFrame", background="#c0c6cf")


    user = payroll.USER

    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee Edit", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)
    

    middle_frame = ttk.Frame(base_frame, style = "Middle.TFrame")
    

    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)

    # test = ttk.Frame(middle_frame)
    

    # Create Name field
    new_label = ttk.Label(middle_frame, text="New Password:")
    new_label.grid(column=0, row=0, padx=5, pady=5)
    # initial = tk.StringVar(value="initial")
    new_entry = ttk.Entry(middle_frame, show="●")
    new_entry.grid(column=1, row=0, padx=5, pady=5)

    # Create Email field
    confirm_label = ttk.Label(middle_frame, text="Confirm Password:")
    confirm_label.grid(column=0, row=1, padx=5, pady=5)
    confirm_entry = ttk.Entry(middle_frame, show="●")
    confirm_entry.grid(column=1, row=1, padx=5, pady=5)
    unmatch_error = ttk.Label(middle_frame, text = "", foreground="red", font=("Arial", 12))
    unmatch_error.grid(column=1, row=2, padx=5, pady=5)
    unmatch_error.configure(background="#c0c6cf")
    # Create Save button
    save_button = ttk.Button(middle_frame, text="Save", command=lambda: save_info(new_entry, confirm_entry, unmatch_error, save_button))
    save_button.grid(column=1, row=2, padx=5, pady=5)




    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    header_frame.pack(side=TOP, fill=X, expand=TRUE, padx=(0,50), pady=(5,5))
    

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
   
    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)


def save_info(new_entry, confirm_entry, unmatch_error, save_button):
    # Get the information from the fields and save it to a file or database
    new_pass = new_entry.get()
    confirm_pass = confirm_entry.get()
    if new_pass == confirm_pass:
        unmatch_error.configure(text="Change succesful!", foreground="blue")
        save_button.grid(row=3)
        hashed_pass = payroll.hash_password(new_pass)
        payroll.USER.password = hashed_pass
        row = payroll.get_row(payroll.EMPLOYEES.employees, payroll.USER.first_name)
        payroll.set_data(row, 13, hashed_pass)
    else:
        unmatch_error.configure(text="Passwords don't match")
        save_button.grid(row=3)
    
    # Do something with the information (e.g. save to a file or database)

