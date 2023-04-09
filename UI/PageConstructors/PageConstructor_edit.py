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
    back_btn = ttk.Button(bottom_frame, text="Back", command=lambda: ui_core.page_controller.open_page("home"))

    # test = ttk.Frame(middle_frame)
    

    # # Create Name field
    # name_label = ttk.Label(middle_frame, text="Name:")
    # name_label.grid(column=0, row=0, padx=5, pady=5)
    # # initial = tk.StringVar(value="initial")
    # name_entry = ttk.Entry(middle_frame)
    # name_entry.insert(0, "Initial text")
    # name_entry.grid(column=1, row=0, padx=5, pady=5)

    # # Create Email field
    # email_label = ttk.Label(middle_frame, text="Email:")
    # email_label.grid(column=0, row=1, padx=5, pady=5)
    # email_entry = ttk.Entry(middle_frame,)
    # email_entry.grid(column=1, row=1, padx=5, pady=5)

    # get the user fields
    entry_list = []
    user = payroll.USER
    target_row = 0
    for field_name in user.editable:
        field = user.editable[field_name]
        temp_label = ttk.Label(middle_frame, text=field_name)
        temp_label.grid(column=0, row=target_row, padx=5, pady=5)
        
        temp_entry = ttk.Entry(middle_frame)
        temp_entry.insert(0, field)
        temp_entry.grid(column=1, row=target_row, padx=5, pady=5)
        # entry_list.append(temp_label)
        entry_list.append(temp_entry)
        target_row += 1

    #Create change password button
    change_btn = ttk.Button(middle_frame, text="change password", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("change"))
    change_btn.grid(column=1, row=len(user.editable), padx=5, pady=5)
    # Create Save button
    save_button = ttk.Button(middle_frame, text="Save", command=save_info)
    save_button.grid(column=1, row=len(user.editable) + 1, padx=5, pady=5)




    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    header_frame.pack(side=TOP, fill=X, expand=TRUE, padx=(0,50), pady=(5,5))
    

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
   
    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)


def save_info(self):
    # Get the information from the fields and save it to a file or database
    # name = self.name_entry.get()
    email = self.email_entry.get()
    
    # Do something with the information (e.g. save to a file or database)

  