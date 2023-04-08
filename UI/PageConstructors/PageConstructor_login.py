from tkinter import *
from tkinter import ttk
from os import path
#
from UI.TooltipController import TooltipController

def constructor(ui_core, ttc:TooltipController, cache, page_data):
    username_var = StringVar()
    password_var = StringVar()
    
    def attempt_login():
        login_success = ui_core.ui_data_interface.attempt_login(username_var.get(), password_var.get())
        if login_success:
            ui_core.page_controller.open_page("home")
        else:
            message_label.configure(text="Invalid login. Please try again.")

    base_frame = ttk.Frame(ui_core.root, padding=15)

    top_frame = ttk.Frame(base_frame)
    #
    login_frame = ttk.Frame(top_frame)
    title = ttk.Label(login_frame, text="Employee Login", style="Bold.TLabel")
    #
    entry_frame = ttk.Frame(login_frame)
    user_entry = ttk.Entry(entry_frame, textvariable=username_var)
    # user_entry.insert(0, "Username")
    # user_entry.bind("<FocusIn>", lambda ev: user_entry.delete(0, "end"))
    ttc.add_tooltip(user_entry, "login_user_entry", (-145, 0), "Username", "Your company username")

    pass_entry = ttk.Entry(entry_frame, show="●", textvariable=password_var)
    # pass_entry.insert(0, "Password")
    # pass_entry.bind("<FocusIn>", lambda ev: pass_entry.delete(0, "end"))
    ttc.add_tooltip(pass_entry, "login_pass_entry", (-145, 0), "Password", "Your company password")
    
    login_btn = ttk.Button(entry_frame, text="Login", command=attempt_login)

    message_label = ttk.Label(entry_frame, text = "", foreground="red", font=("Arial", 12))

    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    login_frame.pack(expand=TRUE)
    title.pack(expand=TRUE, pady=(0,5))

    entry_frame.pack(expand=TRUE)
    user_entry.pack(expand=TRUE, pady=(0,5))
    pass_entry.pack(expand=TRUE, pady=(0,5))
    login_btn.pack(expand=TRUE)
    message_label.pack(expand=TRUE)

    #user_entry.focus()