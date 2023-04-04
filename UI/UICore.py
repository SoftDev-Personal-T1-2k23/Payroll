from tkinter import *
from tkinter import ttk
from UI.PageController import PageController
from UI.UIDataInterface import UIDataInterface
from UI.ThemeController import ThemeController
from UI.TooltipController import TooltipController
from os import path

class UICore:
    def __init__(self, start_page="login"):
        root = Tk()
        root.title("CS2450 Project")
        root.geometry("500x500")
        root.eval("tk::PlaceWindow . center")

        self.dir_root = path.abspath(path.join(__file__, "..\\.."))
        self.root = root
        self.ui_data_interface = UIDataInterface()
        #self.theme_controller = ThemeController(self.root)
        self.tooltip_controller = TooltipController(self)
        self.page_controller = PageController(self)

        self.temp_setup_styling()

        self.page_controller.open_page(start_page)
        root.mainloop()

    def temp_setup_styling(self):
        style = ttk.Style()
        style.configure("Bold.TLabel", font=("Sans", 10, "bold"))
