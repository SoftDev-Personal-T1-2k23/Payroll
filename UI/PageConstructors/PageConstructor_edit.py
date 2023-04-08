"""A page for editing an employee's information"""

from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController

BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):

    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee View", style="Bold.TLabel")

    header_frame = ttk.Frame(top_frame, height=30)
    emp_title = ttk.Label(header_frame, text="John Johny", style="Indent.TLabel")
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
    #TODO: Add information

    # Validate shown fields, if changed
    #TODO: Validate fields

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