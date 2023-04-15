"""A page for viewing an employee's information"""

from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController
BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    udi = ui_core.ui_data_interface

    user_id = udi.get_user_id()
    user_access_level = udi.get_access_level()

    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee View", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)

    #get the user object saved in the payroll file 
    employee = udi.get_target_employee()

    emp_title = ttk.Label(header_frame, text= employee.data["FirstName"] + " " + employee.data["LastName"] , style="Indent.TLabel")
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
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)

    # Populate the three panels with the relevant stored information (text labels)

    #decide what dictionary of information the user should have access to
    target_dictionary = {}
    #check if the user is viewing themself
    if user_id == employee.data["ID"]:
        target_dictionary = employee.quick_attribute
    #Decide what to display based on the privilege level
    else:
        #set the target_dictionary to whatever dictionary is associated with the users privilege level via the privilege_access dictionary
        target_dictionary = employee.privilege_access[user_access_level]
    # print(target_dictionary)

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

        #handle classification and pay
        if field_name == "Classification":
            classification = employee.classification.type()
            # print(classification)

            #create the label for classification 
            temp_label = ttk.Label(frame, text="Classification")
            #position the label using the grid
            temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #make the labels that hold the information
            value_label = ttk.Label(frame, text=classification)
            #position the label using the grid
            value_label.grid(column=1, row=target_row, padx=5, pady=5)
            target_row += 1

            #create the label for amount
            #create the descriptive labels
            temp_label = ttk.Label(frame, text="Amount")
            #position the label using the grid
            temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #make the labels that hold the information
            value_label = ttk.Label(frame, text=employee.pay_type_dict[classification])
            #position the label using the grid
            value_label.grid(column=1, row=target_row, padx=5, pady=5)

        #handle all other general info
        else:
            #create the descriptive labels
            temp_label = ttk.Label(frame, text=field_name)
            #position the label using the grid
            temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #make the labels that hold the information
            value_label = ttk.Label(frame, text=field_value)
            #position the label using the grid
            value_label.grid(column=1, row=target_row, padx=5, pady=5)

        target_row += 1


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
    #make an edit button if the user is viewing their own page or if they have administrator privileges
    if employee.data["ID"] == user_id or user_access_level == "administrator":
        edit_btn = ttk.Button(bottom_frame, text="edit", command=lambda i=employee: ui_core.page_controller.open_page("edit", i))
        edit_btn.pack(side = LEFT)
    # else:
    #     print("edit access denied " + str(employee.id == payroll.USER.id) + " " + str(employee.privilege == "administrator"))
    #     print(employee.privilege)
    #     print("target employee " + employee.first_name)
    #     print("user " + payroll.USER.first_name)