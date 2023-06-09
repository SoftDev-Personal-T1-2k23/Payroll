"""A page for viewing an employee's information"""

from tkinter import *
from tkinter import ttk
#
from UI.tooltip_controller import TooltipController
BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    udi = ui_core.ui_data_interface
    user_is_admin = udi.get_access_level() == "administrator"

    user_id = udi.get_user_id()
    user_access_level = udi.get_access_level()
    employee = udi.get_target_employee()

    target_employee_data = employee.get_viewable_field_data()

    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee View", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)

    def export_csv():
        if employee is None: return
        udi.export_csv("export", [employee])
    def export_paylog():
        if employee is None: return
        udi.export_pay_report([employee])
    #get the user object saved in the payroll file 
    emp_title = ttk.Label(header_frame, text= employee.data["FirstName"] + " " + employee.data["LastName"] , style="Indent.TLabel")
    if user_is_admin:
        pay_report_btn = ttk.Button(header_frame, text="Generate Pay Report", command=export_paylog)
        csv_btn = ttk.Button(header_frame, text="Export CSV", command=export_csv)

    # Add panels the user has access to:
    #       General emp. info, Personal emp. info, and Sensitive emp. info
    # Add necessary tooltips
    middle_frame = ttk.Frame(base_frame)
    public_frame = ttk.Frame(middle_frame, width=400, height=100, style="Public.TFrame")
    public_frame.pack_propagate(False)
    private_frame = ttk.Frame(middle_frame, width=400, height=160, style="Private.TFrame")
    private_frame.pack_propagate(False)
    admin_frame = ttk.Frame(middle_frame, width=400, height=100, style="Admin.TFrame")
    admin_frame.pack_propagate(False)

    # Add a "to prev page" button (-> home page | search page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)


    # target_row = 0
    # for (priv_group_key, priv_group_data) in emp_field_data.items():
    #     frame = None

    #     #decide which frame the information belongs in based on the categorized lists
    #     if priv_group_key == "public":
    #         frame = public_frame
    #     elif priv_group_key == "private":
    #         frame = private_frame
    #     elif priv_group_key == "admin":
    #         frame = admin_frame

    #     for field_data in priv_group_data:
    #         field_name = field_data[0]
    #         field_value = field_data[1]

    #         temp_label = ttk.Label(frame, text=field_name)
    #         temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            
    #         temp_entry = ttk.Entry(frame)
    #         temp_entry.insert(0, field_value)
    #         temp_entry.grid(column=1, row=target_row, padx=5, pady=5)
            
    #         entry_dict[field_name] = temp_entry
    #         target_row += 1


    # Populate the three panels with the relevant stored information (text labels)
    # Build columns
    COLUMN_COUNT = 2
    # vvv there is probably a better way of storing these vvvv
    frame_priv_style_lookup = {
        "public": "Public.TFrame",
        "private": "Private.TFrame",
        "admin": "Admin.TFrame",
    }
    field_title_priv_style_lookup = {
        "public": "PublicFieldTitle.TLabel",
        "private": "PrivateFieldTitle.TLabel",
        "admin": "AdminFieldTitle.TLabel",
    }
    field_priv_style_lookup = {
        "public": "PublicField.TLabel",
        "private": "PrivateField.TLabel",
        "admin": "AdminField.TLabel",
    }
    field_column_parent_lookup = {
        "public": public_frame,
        "private": private_frame,
        "admin": admin_frame
    }
    field_columns = {
        "public": [],
        "private": [],
        "admin": []
    }
    for key in field_columns.keys():
        for i in range(COLUMN_COUNT):
            parent_frame = field_column_parent_lookup[key]
            style = frame_priv_style_lookup[key]

            column = ttk.Frame(parent_frame, style=style)
            column.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=(2,2), pady=(2,2))

            field_columns[key].append(column)

    # row = 0
    for (priv_group_key, priv_group_data) in target_employee_data.items():
        frame_priv_style = frame_priv_style_lookup[priv_group_key]
        field_title_priv_style = field_title_priv_style_lookup[priv_group_key]
        field_priv_style = field_priv_style_lookup[priv_group_key]

        columns = field_columns[priv_group_key]
        column_index = 0
        for field_data in priv_group_data:
            field_name = field_data[0]
            field_value = field_data[1]

            column_parent = columns[column_index]
            
            frame_field = ttk.Frame(column_parent, style=frame_priv_style)
            label_title = ttk.Label(frame_field, text=field_name, style=field_title_priv_style)
            label_value = ttk.Label(frame_field, text=str(field_value), style=field_priv_style)

            frame_field.pack(side=TOP, fill=X)
            label_title.pack(side=LEFT, fill=X)
            label_value.pack(side=RIGHT, fill=X)

            column_index += 1
            column_index %= COLUMN_COUNT

            # #handle classification and pay
            # if field_name == "Classification":
            #     classification = employee.classification.type()
            #     # print(classification)

            #     #create the label for classification 
            #     temp_label = ttk.Label(frame, text="Classification")
            #     #position the label
            #     temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #     #make the labels that hold the information
            #     value_label = ttk.Label(frame, text=classification)
            #     #position the label
            #     value_label.grid(column=1, row=target_row, padx=5, pady=5)
            #     target_row += 1

            #     #create the label for amount
            #     #create the descriptive labels
            #     temp_label = ttk.Label(frame, text="Amount")
            #     #position the label
            #     temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #     #make the labels that hold the information
            #     value_label = ttk.Label(frame, text=employee.pay_type_dict[classification])
            #     #position the label
            #     value_label.grid(column=1, row=target_row, padx=5, pady=5)

            # #handle all other general info
            # else:

            #     #create the descriptive labels
            #     temp_label = ttk.Label(frame, text=field_name)
            #     #position the label using the grid
            #     temp_label.grid(column=0, row=target_row, padx=5, pady=5)
            #     #make the labels that hold the information
            #     value_label = ttk.Label(frame, text=field_value)
            #     #position the label using the grid
            #     value_label.grid(column=1, row=target_row, padx=5, pady=5)

            # row += 1


    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    header_frame.pack(side=TOP, fill=X, expand=TRUE, padx=(0,50), pady=(5,5))
    emp_title.pack(side=LEFT, padx=(0,50))
    if user_is_admin:
        pay_report_btn.pack(side=LEFT, padx=(50, 0))
        csv_btn.pack(side=LEFT)

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
    public_frame.pack(side=TOP)

    private_frame.pack(side=TOP)
    admin_frame.pack(side=TOP)

    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)
    #make an edit button if the user is viewing their own page or if they have administrator privileges
    def edit_employee():
        udi.set_target_employee(employee)
        print("TEMP:VIEW", udi.get_target_employee())
        ui_core.page_controller.open_page("edit")

    if employee.data["ID"] == user_id or user_access_level == "administrator":
        edit_btn = ttk.Button(bottom_frame, text="edit", command=edit_employee)
        edit_btn.pack(side = LEFT)
    # else:
    #     print("edit access denied " + str(employee.id == payroll.USER.id) + " " + str(employee.privilege == "administrator"))
    #     print(employee.privilege)
    #     print("target employee " + employee.first_name)
    #     print("user " + payroll.USER.first_name)