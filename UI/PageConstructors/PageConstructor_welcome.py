from tkinter import *
from tkinter import ttk
from Dependencies.TkGif import Gif
from PIL import ImageTk, Image
from os import path

def constructor(ui_core, ttc, cache, page_data):
    splash_img = None
    if not "splash" in cache["images"]:
        splash_img = ImageTk.PhotoImage(Image.open(path.join(ui_core.dir_root, "Art\\jam.gif")))
        cache["images"]["splash"] = splash_img
    else:
        splash_img = cache["images"]["splash"]

    base_frame = ttk.Frame(ui_core.root, padding=15, style="T.TFrame")

    top_frame = ttk.Frame(base_frame, style="T.TFrame")
    splash_art = ttk.Label(top_frame, text="Testing", image=splash_img, width=256)
    Gif(splash_art, path.join(ui_core.dir_root, "Art\\jam.gif"), width=256, height=256)

    bot_frame = ttk.Frame(base_frame, style="T.TFrame")
    login_btn = ttk.Button(bot_frame, text="To Login", command=lambda: ui_core.page_controller.open_page("login"), style="T.TButton")
    ttc.add_tooltip(login_btn, "login_btn", "Login", "Allows the user to login")
    
    base_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

    top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)
    splash_art.pack(expand=TRUE)

    bot_frame.pack(side=TOP, fill=BOTH)
    login_btn.pack()



