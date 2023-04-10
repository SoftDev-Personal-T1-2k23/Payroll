"""The application login page"""

from tkinter import *
from tkinter import ttk
from os import path
#
from UI.TooltipController import TooltipController

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    root:Tk = ui_core.root
    username_var = StringVar()
    password_var = StringVar()
    login_failed_text:ttk.Label = None

    #TODO: Account for login_failed_text being hidden, after just being shown, when consecutive logins occur
    def show_login_failed():
        # rx, ry = bottom_frame.winfo_x(), bottom_frame.winfo_y()
        login_failed_text.pack(pady=(10, 0))
        login_failed_text.after(2000, hide_login_failed)

    def hide_login_failed():
        if login_failed_text is not None:
            login_failed_text.pack_forget()

    def attempt_login():
        login_success = ui_core.ui_data_interface.attempt_login(username_var.get(), password_var.get())
        if login_success:
            ui_core.page_controller.open_page("home")
        else:
            show_login_failed()

    
    # Split the page into necessary panels




    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)
    
    # Add the page title
    login_frame = ttk.Frame(top_frame)
    title = ttk.Label(login_frame, text="Employee Login", style="Bold.TLabel")
    
    # Add the username and password entries & Their entry validations
    # Add necessary tooltips
    entry_frame = ttk.Frame(login_frame)
    user_entry = ttk.Entry(entry_frame, textvariable=username_var)
        # user_entry.insert(0, "Username")
        # user_entry.bind("<FocusIn>", lambda ev: user_entry.delete(0, "end"))
    
    ttc.add_tooltip(user_entry, "login_user_entry", (-145, 0), "Username", "Your company username")

    pass_entry = ttk.Entry(entry_frame, show="●", textvariable=password_var)
        # pass_entry.insert(0, "Password")
        # pass_entry.bind("<FocusIn>", lambda ev: pass_entry.delete(0, "end"))
    ttc.add_tooltip(pass_entry, "login_pass_entry", (-145, 0), "Password", "Your company password")
    
    # Add the login button & Associated login logic (UIDataInterface)
    login_btn = ttk.Button(entry_frame, text="Login", command=attempt_login)


    
    bottom_frame = ttk.Frame(entry_frame, height=20)
    login_failed_text = ttk.Label(bottom_frame, text="Invalid Login", style="Error.TLabel")
    # Quick fix for moving UI widgets
    login_failed_text.pack(pady=(10, 0))
    login_failed_text.after(10, lambda: login_failed_text.pack_forget())



    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    login_frame.pack(expand=TRUE)
    title.pack(expand=TRUE, pady=(0,5))

    entry_frame.pack(expand=TRUE)
    user_entry.pack(expand=TRUE, pady=(0,5))
    pass_entry.pack(expand=TRUE, pady=(0,5))
    login_btn.pack(expand=TRUE)


    bottom_frame.pack(expand=TRUE)

    #user_entry.focus()