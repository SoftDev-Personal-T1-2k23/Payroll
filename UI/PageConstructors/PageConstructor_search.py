"""A page for searching the employee database"""

from tkinter import *
from tkinter import ttk
from UI.tooltip_controller import TooltipController
#make it so we can use the view page

from .PageConstructor_view import constructor as construct_view
BUTTON_WIDTH = 20
FILTER_COND_LOOKUP = { # Conditions
    ">0K": lambda x: float(x)>=0,
    ">25K": lambda x: float(x)>=25E3,
    ">50K": lambda x: float(x)>=50E3,
    ">75K": lambda x: float(x)>=75E3,
    ">100K": lambda x: float(x)>=100E3,
}

FILTER_TRANS_LOOKUP = { # Translations
    "Employee": "employee",
    "Admin": "administrator",
    "True": "1",
    "False": "0"
}
FILTER_OPTIONS = {
    "Privilege": ["N/A", "Employee", "Admin"],
    "Salary": ["N/A", ">0K", ">25K", ">50K", ">75K", ">100K"], # Actual use >= and <=, but > and < are simple
    "IsArchived": ["N/A", "True", "False"]
}

last_search_text = None # last search text; used for backward page navigation
current_search_results = None # Current search results
current_search_by = None # Current search by
current_filters = {} # Current filters

#make a list to keep track of what employees need to be displayed
display_list = []

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    udi = ui_core.ui_data_interface
    user_is_admin = udi.get_access_level() == "administrator"

    search_by_var = StringVar()
    search_entry_var = StringVar()
    filter_vars = {} # Populated with filter option keys and StringVar values
    # Split the page into necessary panels

    base_frame = ttk.Frame(ui_core.root, padding=15)

    # Add the page title
    top_frame = ttk.Frame(base_frame)
    title = ttk.Label(top_frame, text="Employee Search", style="Bold.TLabel")

    SEARCH_BY_OPTIONS = [
        "LastName", "ID", "Email"
    ]
    def search_by_changed(*args):
        global current_search_by
        current_search_by = search_by_var.get()
    # Add a search entry and search button
    def perform_basic_search(*args, search_text=None):
        s_text = search_entry_var.get() if search_text is None else search_text
        search(s_text, results_frame, results_scroll, ui_core)
    search_frame = ttk.Frame(top_frame, height=30)
    global current_search_by
    selected_search_by_option = current_search_by or SEARCH_BY_OPTIONS[0]
    current_search_by = selected_search_by_option # Prevents an error for None search_by option
    search_by = ttk.OptionMenu(search_frame, search_by_var, selected_search_by_option, *SEARCH_BY_OPTIONS)
    search_by.config(width=10)
    search_by_var.trace("w", search_by_changed)
    search_btn = ttk.Button(search_frame, text="Search", command=perform_basic_search)
    search_entry = ttk.Entry(search_frame, width=50, textvariable=search_entry_var)
    search_entry_var.trace("w", perform_basic_search)

    # Add search filter options

    base_filter_frame = ttk.Frame(top_frame, height=30)
    
    def get_longest_filter_option(filter_options):
        #calculate what the longest item in the menu is so the width can be consistent
        longest_option = max(filter_options, key=len)
        longest_option_width = len(longest_option)
        return longest_option_width+1
    results_frame = None
    def filter_var_updated(filter_option_title, filter_var):
        global current_filters
        current_filters[filter_option_title] = filter_var
        if results_frame is None: return
        perform_basic_search(search_text=last_search_text)

    global current_filters
    for (filter_option_title, filter_options) in FILTER_OPTIONS.items():
        if filter_option_title == "IsArchived" and not user_is_admin: continue

        filter_var = StringVar()
        filter_vars[filter_option_title] = filter_var
        filter_var.trace("w", lambda a,b,c,fv=filter_var: filter_var_updated(filter_option_title, fv))

        filter_frame = ttk.Frame(base_filter_frame, width=20)
        filter_label = ttk.Label(filter_frame, text=f"{filter_option_title}:")
        current_filter_choice = filter_options[0]
        if filter_option_title in current_filters:
            current_filter_choice = current_filters[filter_option_title].get()
        filter_menu = ttk.OptionMenu(filter_frame, filter_var, current_filter_choice, *filter_options)
        #set fixed width to options menu
        filter_menu.config(width=get_longest_filter_option(filter_options))

        filter_frame.pack(side=LEFT, padx=(0,5))
        filter_label.pack(side=LEFT, expand=TRUE)
        filter_menu.pack(side=LEFT, expand=TRUE)


    middle_frame = ttk.Frame(base_frame)
    results_frame = ttk.Frame(middle_frame, width=400, height=300, style="Indent.TFrame")
    results_frame.pack_propagate(False)
    results_scroll = ttk.Scrollbar(results_frame)
    def export_search_results():
        if current_search_results is None: return
        udi.export_csv("export", current_search_results)
    csv_btn = ttk.Button(middle_frame, text="Export CSV", width=BUTTON_WIDTH, command=export_search_results)
    ttc.add_tooltip(csv_btn, "export_csv_btn", (-175, 0), ("Export CSV", "Export search results"))


    # Add a "to home" button (-> home page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    # back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)
    back_btn = ttk.Button(bottom_frame, text="Back", command=lambda: ui_core.page_controller.open_page("home"))


    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP)
    title.pack(expand=TRUE)

    search_frame.pack(side=TOP, fill=X, padx=(0,50), pady=(5,5))
    search_by.pack(side=LEFT)
    search_btn.pack(side=LEFT, expand=TRUE)
    search_entry.pack(side=LEFT, expand=TRUE)

    base_filter_frame.pack(side=TOP, fill=X)

    middle_frame.pack(side=TOP, expand=TRUE, fill=BOTH)
    results_frame.pack(side=TOP, expand=TRUE, pady=(10,0))
    results_scroll.pack(side=RIGHT, fill=Y)
    csv_btn.pack(side=BOTTOM)

    bottom_frame.pack(side=LEFT)
    back_btn.pack(side=LEFT)


    # Perform setup logic
    global last_search_text
    if last_search_text is not None:
        perform_basic_search(search_text=last_search_text)
        search_entry.insert(0, last_search_text)
        last_search_text = None


def search(search_text, results_frame, results_scroll, ui_core):
    '''
    This function is called when the search button is pressed
    it takes the input from the search entry box as a parameter
    '''
    udi = ui_core.ui_data_interface
    current_user = udi.get_user()
    user_is_admin = udi.get_access_level() == "administrator"
    employees = udi.get_employees()

    #reset the display_list and clear the frame
    emp_list = []
    for child in results_frame.winfo_children():
        child.destroy()

    def add_emp(emp):
        if emp in emp_list: return False
        emp_list.append(emp)
        return True

    #Apply filters, if any
    global current_filters
    applied_search_filters = False
    for id in employees:
        emp = employees[id]
        
        for (filter_title, filter_val) in current_filters.items():
            filter_val = filter_val.get()
            if filter_val == "N/A":
                continue # Ignore N/A filters
            else:
                applied_search_filters = True
            if filter_val in FILTER_TRANS_LOOKUP: # Translate filter_value
                filter_val = FILTER_TRANS_LOOKUP[filter_val]
            emp_val = emp.data[filter_title]

            if filter_val in FILTER_COND_LOOKUP:
                filter_cond_success = False
                try:
                    filter_cond_success = FILTER_COND_LOOKUP[filter_val](emp_val)
                except:
                    pass
                if filter_cond_success:
                    add_emp(emp)
                    continue

            if filter_title == "Privilege" or filter_title == "IsArchived":
                if emp_val == filter_val:
                    add_emp(emp)

    if search_text != "":
        IGNORED_FIELDS = [
            "Password"
        ]
        #loop through the dictionary of employees
        for id in employees:
            #get the individual employee object
            emp = employees[id]
            #filter irrelevant employees by search_by value
            search_by_emp_val = str(emp.data[current_search_by]).lower()[:len(search_text)]
            if not search_text in search_by_emp_val:
                if emp in emp_list:
                    emp_list.remove(emp)
                continue

            if applied_search_filters: continue

            #loop through the persons attributes
            for (field_name, field_value) in emp.data.items():
                if field_name in IGNORED_FIELDS: continue

                #if the users query appears in the field we are looking at add the employee to the list
                if search_text in str(field_value).lower():
                    add_emp(emp)

    #make the entries
    def view_employee_data(emp):
        global last_search_text
        last_search_text = search_text
        udi.set_target_employee(emp)
        ui_core.page_controller.open_page("view")
    
    def archive_employee(emp):
        udi.archive_employee(emp)
        search(search_text, results_frame, results_scroll, ui_core)
    
    def unarchive_employee(emp):
        udi.unarchive_employee(emp)
        search(search_text, results_frame, results_scroll, ui_core)

    RESULT_STYLE_LOOKUP = {
        "archived": {
            "frame": "Admin.TFrame",
            "label": "Admin.TLabel",
        },
    }

    global current_search_results
    current_search_results = []
    row = 0
    for emp in emp_list:
        is_archived = emp.data["IsArchived"] == "1"
        if is_archived and not user_is_admin: continue

        current_search_results.append(emp)

        frame = ttk.Frame(results_frame)
        frame_emp_name = ttk.Frame(frame, width=50)
        label_emp_name = ttk.Label(frame_emp_name, text=emp.data["Name"])
        content_frame = ttk.Frame(frame)
        btn_view = ttk.Button(content_frame, text="View", command=lambda e=emp: view_employee_data(e))
        btn_archive = None
        if user_is_admin and not is_archived:
            btn_archive = ttk.Button(content_frame, text="Archive", command=lambda e=emp: archive_employee(e))
        btn_unarchive = None
        if user_is_admin and is_archived:
            btn_unarchive = ttk.Button(content_frame, text="Unarchive", command=lambda e=emp: unarchive_employee(e))
        
        if is_archived:
            style_info = RESULT_STYLE_LOOKUP["archived"]
            frame_style = style_info["frame"]
            label_style = style_info["label"]

            frame.configure(style=frame_style)
            frame_emp_name.configure(style=frame_style)
            label_emp_name.configure(style=label_style)
            content_frame.configure(style=frame_style)

        frame.pack(side=TOP, fill=X, padx=(2,2), pady=(2,2))
        frame_emp_name.pack(side=LEFT)
        label_emp_name.pack(padx=(0,10))
        content_frame.pack(side=LEFT, expand=TRUE, fill=X)
        btn_view.pack(side=RIGHT)
        if btn_archive is not None:
            btn_archive.pack(side=RIGHT)
        if btn_unarchive is not None:
            btn_unarchive.pack(side=RIGHT)

        row += 1
