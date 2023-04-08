"""A page for importing and exporting database information"""

from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController

BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):


    # Split the page into necessary panels
    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)

    # Add the page title
    login_frame = ttk.Frame(top_frame)
    title = ttk.Label(login_frame, text="Export", style="Bold.TLabel")

    # Add a list of buttons for various export options (csv export, pay report)
    # Add necessary tooltips
    button_frame = ttk.Frame(login_frame)
    pay_report_btn = ttk.Button(button_frame, text="Export Pay Report", width=BUTTON_WIDTH)
    ttc.add_tooltip(pay_report_btn, "export_pay_report_btn", (-170, 0), "Export Pay Report", "Generate a pay report")
    csv_btn = ttk.Button(button_frame, text="Export CSV", width=BUTTON_WIDTH)
    ttc.add_tooltip(csv_btn, "export_csv_btn", (-175, 0), "Export CSV", "Export selected employee info")

    # Add a "to home page" button (-> home page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)



    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)
    #
    login_frame.pack(expand=TRUE)
    title.pack(expand=TRUE)
    #
    button_frame.pack(expand=TRUE)
    pay_report_btn.pack(expand=TRUE)
    csv_btn.pack(expand=TRUE)
    #
    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)
    
    # root.bind("<Return>", calculate)