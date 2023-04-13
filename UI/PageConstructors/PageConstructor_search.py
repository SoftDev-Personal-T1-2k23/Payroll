"""A page for searching the employee database"""

from tkinter import *
from tkinter import ttk
from UI.TooltipController import TooltipController
import payroll
#make it so we can use the view page

from .PageConstructor_view import constructor as construct_view
BUTTON_WIDTH = 20


#make a list to keep track of what employees need to be displayed
display_list = []

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
    search_btn = ttk.Button(search_frame, text="Search", command=lambda: search(search_entry_var, results_frame, ui_core))
    search_entry = ttk.Entry(search_frame, width=50, textvariable=search_entry_var)

    # Add search filter options
    #       (employee last name, employee id, employee department id, etc.)
    # Add necessary tooltips
    filter_frame = ttk.Frame(top_frame, height=30)


   


    FILTER0_OPTIONS = ["These", "are", "all", "valid", "options"]

    #calculate what the longest item in the menu is so the width can be consistent
    longest_option = max(FILTER0_OPTIONS, key=len)
    longest_option_width = len(longest_option)

    filter0_frame = ttk.Frame(filter_frame, width=20)
    filter0_label = ttk.Label(filter0_frame, text="Filter0:")
    filter0_menu = ttk.OptionMenu(filter0_frame, filter0_var, FILTER0_OPTIONS[0], *FILTER0_OPTIONS)
    #set fixed width to options menu
    filter0_menu.config(width=longest_option_width)


    FILTER1_OPTIONS = ["Some", "helpful", "search", "filters"]

    #calculate what the longest item in the menu is so the width can be consistent
    longest_option = max(FILTER1_OPTIONS, key=len)
    longest_option_width = len(longest_option)

    filter1_frame = ttk.Frame(filter_frame, width=20)
    filter1_label = ttk.Label(filter1_frame, text="Filter1:")
    filter1_menu = ttk.OptionMenu(filter1_frame, filter1_var, FILTER1_OPTIONS[0], *FILTER1_OPTIONS)
    filter1_menu.config(width=longest_option_width)

    middle_frame = ttk.Frame(base_frame)
    results_frame = ttk.Frame(middle_frame, width=400, height=300, style="Indent.TFrame")

   

    # Add a "to home" button (-> home page) & other "ease of use" buttons
    bottom_frame = ttk.Frame(base_frame, height=50)
    # back_btn = ttk.Button(bottom_frame, text="Back", command=ui_core.page_controller.open_prev_page)
    back_btn = ttk.Button(bottom_frame, text="Back", command=lambda: ui_core.page_controller.open_page("home"))



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


def search(data, results_frame, ui_core):
    '''
    This function is called when the search button is pressed
    it takes the input from the search entry box as a parameter
    '''
    # print(data.get())

    #grab the employee database from the payroll file
    employees = payroll.EMPLOYEES.employees

    #reset the display_list and clear the frame
    display_list = []
    for child in results_frame.winfo_children():
        child.destroy()


    #end the function if there is nothing to search
    if data.get() == "":
        return None

    #loop through the dictionary of employees
    for id in employees:
        #get the individual employee object
        person = employees[id]
        #loop through the persons attributes
        for field_name in person.quick_attribute:
            #get the actual attribute value
            field_value = person.quick_attribute[field_name]

            #if the users query appears in the field we are looking at add the employee to the list
            if data.get() in str(field_value):
                display_list.append(person)


    #make the entries
    target_row = 0
    for person in display_list:
        label = ttk.Label(results_frame, text=person.first_name + " " + person.last_name)
        label.grid(row=target_row, column=1, padx=10, pady=10)
        view_btn = ttk.Button(results_frame, text="view", command=lambda i=person: ui_core.page_controller.open_page("view", i))
        
        

        view_btn.grid(row=target_row, column=2)
        target_row += 1
    results_frame.grid_propagate(False)
