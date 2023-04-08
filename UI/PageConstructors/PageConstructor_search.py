"""A page for searching the employee database"""

from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController

BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    search_entry_var = StringVar()
    filter0_var = StringVar()
    filter1_var = StringVar()
    # Split the page into necessary panels

    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee Search", style="Bold.TLabel")

    # Add a search entry and search button
    search_frame = ttk.Frame(top_frame, height=30)
    search_btn = ttk.Button(search_frame, text="Search")
    search_entry = ttk.Entry(search_frame, width=50, textvariable=search_entry_var)

    # Add search filter options
    #       (employee last name, employee id, employee department id, etc.)
    # Add necessary tooltips
    filter_frame = ttk.Frame(top_frame, height=30)

    FILTER0_OPTIONS = ["These", "are", "all", "valid", "options"]
    filter0_frame = ttk.Frame(filter_frame, width=20)
    filter0_label = ttk.Label(filter0_frame, text="Filter0:")
    filter0_menu = ttk.OptionMenu(filter0_frame, filter0_var, FILTER0_OPTIONS[0], *FILTER0_OPTIONS)

    FILTER1_OPTIONS = ["Some", "helpful", "search", "filters"]
    filter1_frame = ttk.Frame(filter_frame, width=20)
    filter1_label = ttk.Label(filter1_frame, text="Filter1:")
    filter1_menu = ttk.OptionMenu(filter1_frame, filter1_var, FILTER1_OPTIONS[0], *FILTER1_OPTIONS)

    middle_frame = ttk.Frame(base_frame)
    results_frame = ttk.Frame(middle_frame, width=400, height=300, style="Indent.TFrame")

    # Add a "to home" button (-> home page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)



    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    search_frame.pack(side=TOP, fill=X, padx=(0,50), pady=(5,5))
    search_btn.pack(side=LEFT, expand=TRUE)
    search_entry.pack(side=LEFT, expand=TRUE)

    filter_frame.pack(side=TOP, fill=X)

    filter0_frame.pack(side=LEFT, padx=(0,5))
    filter0_label.pack(side=LEFT, expand=TRUE)
    filter0_menu.pack(side=LEFT, expand=TRUE)

    filter1_frame.pack(side=LEFT)
    filter1_label.pack(side=LEFT, expand=TRUE)
    filter1_menu.pack(side=LEFT, expand=TRUE)

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
    results_frame.pack(side=TOP, expand=TRUE, pady=(10,0))

    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)