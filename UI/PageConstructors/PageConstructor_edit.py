"""A page for editing an employee's information"""


import tkinter as tk
from tkinter import *
from tkinter import ttk
from UI.tooltip_controller import TooltipController
BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    udi = ui_core.ui_data_interface

    employee = udi.get_target_employee()
    target_employee_data = employee.get_editable_field_data()

    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee View", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)

    emp_title = ttk.Label(header_frame, text=employee.data["FirstName"] + " " + employee.data["LastName"], style="Indent.TLabel")
    pay_report_btn = ttk.Button(header_frame, text="Generate Pay Report")
    csv_btn = ttk.Button(header_frame, text="Export CSV")

    # Add panels the user has access to:
    #       General emp. info, Personal emp. info, and Sensitive emp. info
    # Add necessary tooltips
    middle_frame = ttk.Frame(base_frame)
    public_frame = ttk.Frame(middle_frame, width=400, height=120, style="Public.TFrame")
    public_frame.pack_propagate(False)
    private_frame = ttk.Frame(middle_frame, width=400, height=120, style="Private.TFrame")
    private_frame.pack_propagate(False)
    admin_frame = ttk.Frame(middle_frame, width=400, height=120, style="Admin.TFrame")
    admin_frame.pack_propagate(False)

    # Add a "to prev page" button (-> home page | search page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=lambda: ui_core.page_controller.open_page("home"))

    # Populate the three panels with the relevant stored information (text labels)

    # get the user fields and create entries and store them in a list
    # entry_dict = {}

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
    field_entry_priv_style_lookup = {
        "public": "Public.TEntry",
        "private": "Private.TEntry",
        "admin": "Admin.TEntry",
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
        for _ in range(COLUMN_COUNT):
            parent_frame = field_column_parent_lookup[key]
            style = frame_priv_style_lookup[key]

            column = ttk.Frame(parent_frame, style=style)
            column.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=(2,2), pady=(2,2))

            field_columns[key].append(column)

    # row = 0
    for (priv_group_key, priv_group_data) in target_employee_data.items():
        frame_priv_style = frame_priv_style_lookup[priv_group_key]
        field_title_priv_style = field_title_priv_style_lookup[priv_group_key]
        field_entry_priv_style = field_entry_priv_style_lookup[priv_group_key]

        columns = field_columns[priv_group_key]
        column_index = 0
        for field_data in priv_group_data:
            field_name = field_data[0]
            field_value = field_data[1]

            column_parent = columns[column_index]
            
            frame_field = ttk.Frame(column_parent, style=frame_priv_style)
            label_title = ttk.Label(frame_field, text=field_name, style=field_title_priv_style)
            label_value = ttk.Entry(frame_field, style=field_entry_priv_style)
            label_value.insert(0, str(field_value))

            frame_field.pack(side=TOP, fill=X)
            label_title.pack(side=LEFT, fill=X)
            label_value.pack(side=RIGHT, fill=X)

            column_index += 1
            column_index %= COLUMN_COUNT

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
    #     # if field_name in employee.general:
    #     #     frame = public_frame
    #     # elif field_name in employee.personal:
    #     #     frame = private_frame
    #     # else:
    #     #     frame = admin_frame

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


    #Create change password button
    # change_btn = ttk.Button(admin_frame, text="change password", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("change"))

    # change_btn.grid(column=1, row=target_row, padx=5, pady=5)
    # # Create Save button
    # save_btn = ttk.Button(middle_frame, text="Save", command=lambda: udi.update_employee_info([(pair[0], pair[1].get()) for pair in entry_dict.items()]))
    # # save_button.grid(column=1, row=2, padx=5, pady=5)

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
    # save_btn.pack(side=LEFT)



