from tkinter import *
from tkinter import ttk
#
from UI.TooltipController import TooltipController

BUTTON_WIDTH = 20

def constructor(ui_core, ttc:TooltipController, cache, page_data):

    def attempt_logout():
        logout_success = True
        if logout_success:
            ui_core.page_controller.open_page("login")

    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)

    login_frame = ttk.Frame(top_frame)
    title = ttk.Label(login_frame, text="Home", style="Bold.TLabel")

    button_frame = ttk.Frame(login_frame)
    search_btn = ttk.Button(button_frame, text="Search", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("search"))
    ttc.add_tooltip(search_btn, "home_search_button", (-170, 0), "Search Page", "Search the employee database")
    edit_btn = ttk.Button(button_frame, text="Edit Information", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("edit"))
    ttc.add_tooltip(edit_btn, "home_edit_button", (-175, 0), "Edit Page", "Edit your employee information")
    view_btn = ttk.Button(button_frame, text="View Information", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("view"))
    ttc.add_tooltip(view_btn, "home_view_button", (-178, 0), "View Page", "View your employee information")
    import_export_btn = ttk.Button(button_frame, text="Export", width=BUTTON_WIDTH, command=lambda: ui_core.page_controller.open_page("export"))
    ttc.add_tooltip(import_export_btn, "home_impexp_button", (-170, 0), "Export Page", "Export employee information")

    bottom_frame = ttk.Frame(base_frame, height=50)
    logout_btn = ttk.Button(bottom_frame, text="Logout", command=attempt_logout)



    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)
    #
    login_frame.pack(expand=TRUE)
    title.pack(expand=TRUE)
    #
    button_frame.pack(expand=TRUE)
    search_btn.pack(expand=TRUE)
    edit_btn.pack(expand=TRUE)
    view_btn.pack(expand=TRUE)
    import_export_btn.pack(expand=TRUE)
    #
    bottom_frame.pack(side=LEFT)
    logout_btn.pack(side=LEFT)
    
    # root.bind("<Return>", calculate)