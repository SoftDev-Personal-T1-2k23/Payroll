from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController

BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    ttk.Style().configure("Red.TFrame", background="#F00")
    ttk.Style().configure("Green.TFrame", background="#0F0")
    ttk.Style().configure("Blue.TFrame", background="#00F")
    
    filter0_value = StringVar()
    filter1_value = StringVar()

    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee Search", style="Bold.TLabel")

    search_frame = ttk.Frame(top_frame)
    search_btn = ttk.Button(search_frame, text="Search")
    search_entry = ttk.Entry(search_frame)

    filter_frame = ttk.Frame(top_frame)

    FILTER0_OPTIONS = ["These", "are", "all", "valid", "options"]
    filter0_frame = ttk.Frame(filter_frame, width=20)
    filter0_label = ttk.Label(filter0_frame, text="Filter0:")
    filter0_menu = ttk.OptionMenu(filter0_frame, filter0_value, FILTER0_OPTIONS[0], *FILTER0_OPTIONS)

    FILTER1_OPTIONS = ["Some", "helpful", "search", "filters"]
    filter1_frame = ttk.Frame(filter_frame, width=20)
    filter1_label = ttk.Label(filter1_frame, text="Filter1:")
    filter1_menu = ttk.OptionMenu(filter1_frame, filter1_value, FILTER1_OPTIONS[0], *FILTER1_OPTIONS)

    middle_frame = ttk.Frame(base_frame)
    results_frame = ttk.Frame(middle_frame, width=200, height=200, style="Red.TFrame")

    bottom_frame = ttk.Frame(base_frame, height=50)
    back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)



    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)
    title.pack(expand=TRUE)

    search_frame.pack(side=LEFT, expand=TRUE, padx=(0,50))
    search_btn.pack(side=LEFT, expand=TRUE)
    search_entry.pack(side=LEFT, expand=TRUE)

    filter_frame.pack(expand=TRUE)

    filter0_frame.pack(side=LEFT, expand=TRUE, padx=(0,5))
    filter0_label.pack(side=LEFT, expand=TRUE)
    filter0_menu.pack(side=LEFT, expand=TRUE)

    filter1_frame.pack(side=LEFT, expand=TRUE)
    filter1_label.pack(side=LEFT, expand=TRUE)
    filter1_menu.pack(side=LEFT, expand=TRUE)

    middle_frame.pack(expand=TRUE)
    results_frame.pack(expand=TRUE, fill=BOTH)

    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)