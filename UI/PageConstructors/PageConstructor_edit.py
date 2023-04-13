"""A page for editing an employee's information"""


import tkinter as tk
from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController
import payroll
BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):

    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee View", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)

    employee = payroll.TARGET_EMPLOYEE
    print(employee.first_name)
    emp_title = ttk.Label(header_frame, text=employee.first_name + " " + employee.last_name, style="Indent.TLabel")
    pay_report_btn = ttk.Button(header_frame, text="Generate Pay Report")
    csv_btn = ttk.Button(header_frame, text="Export CSV")

    # Add panels the user has access to:
    #       General emp. info, Personal emp. info, and Sensitive emp. info
    # Add necessary tooltips
    middle_frame = ttk.Frame(base_frame)
    public_frame = ttk.Frame(middle_frame, width=400, height=120, style="Public.TFrame")
    private_frame = ttk.Frame(middle_frame, width=400, height=120, style="Private.TFrame")
    admin_frame = ttk.Frame(middle_frame, width=400, height=120, style="Admin.TFrame")

    # Add a "to prev page" button (-> home page | search page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=lambda: ui_core.page_controller.open_page("home"))

    # Populate the three panels with the relevant stored information (text labels)
    
    #decide what dictionary of information the user should have access to
    target_dictionary = {}
    #check if the user is viewing themself
    if payroll.USER.id == employee.id:
        target_dictionary = employee.editable_by_user
    #Decide what to display based on the privilege level
    else:
        #set the target_dictionary to whatever dictionary is associated with the users privilege level via the privilege_access dictionary
        target_dictionary = employee.privilege_access[payroll.USER.privilege]

    # get the user fields and create entries and store them in a list
    entry_dict = {}

    target_row = 0
    for field_name in target_dictionary:
        field_value = target_dictionary[field_name]
        frame = None
        #decide which frame the information belongs in based on the categorized lists
        if field_name in employee.general:
            frame = public_frame
        elif field_name in employee.personal:
            frame = private_frame
        else:
            frame = admin_frame

        temp_label = ttk.Label(frame, text=field_name)
        temp_label.grid(column=0, row=target_row, padx=5, pady=5)
        
        temp_entry = ttk.Entry(frame)
        temp_entry.insert(0, field_value)
        temp_entry.grid(column=1, row=target_row, padx=5, pady=5)
        
        entry_dict[field_name] = temp_entry
        target_row += 1


    #Create change password button
    change_btn = ttk.Button(admin_frame, text="change password", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("change"))

    change_btn.grid(column=1, row=target_row, padx=5, pady=5)
    # Create Save button
    save_btn = ttk.Button(middle_frame, text="Save", command=lambda: payroll.save_info(entry_dict))
    # save_button.grid(column=1, row=2, padx=5, pady=5)

    # Validate shown fields, if changed
    #TODO: Validate fields


    #position everything
    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    header_frame.pack(side=TOP, fill=X, expand=TRUE, padx=(0,50), pady=(5,5))
    emp_title.pack(side=LEFT, padx=(0,50))
    pay_report_btn.pack(side=LEFT, padx=(50, 0))
    csv_btn.pack(side=LEFT)

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
    public_frame.pack(side=TOP)

    private_frame.pack(side=TOP)
    admin_frame.pack(side=TOP)

    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)
    save_btn.pack(side=LEFT)



