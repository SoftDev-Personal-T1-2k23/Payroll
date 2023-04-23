"""The core module for intializing UI components and holding global references"""
from os import path
from tkinter import Tk
from tkinter import ttk
from UI.PageController import PageController
from UI.UIDataInterface import UIDataInterface
# from UI.ThemeController import ThemeController
from UI.tooltip_controller import TooltipController


class UICore:
    """Serves as a nexus for various UI classes and their communication"""

    def __init__(self, start_page="login"):
        """Initialize the UI portion of the program
         
          Params:
              start_page: The page the program will launch on startup
        """

        # Setup tkinter root and main window
        # Set the window title & Set the window dimensions & Center the window
        root = Tk()
        root.title("CS2450 Project")
        root.geometry("500x500")
        root.eval("tk::PlaceWindow . center")

        # Determine and store the program's absolute CWD path
        self.dir_root = path.abspath(path.join(__file__, "..\\.."))
        # Store root
        self.root = root

        # Store and create: UIDataInterface, ThemeController, TooltipController, PageController
        self.ui_data_interface = UIDataInterface()
        #self.theme_controller = ThemeController(self.root)
        self.tooltip_controller = TooltipController(self)
        self.page_controller = PageController(self)

        # Setup temporary widget styling
        self.temp_setup_styling()

        # Open the welcome page (via PageController)
        # Run the tkinter UI loop
        self.page_controller.open_page(start_page)
        root.mainloop()

    def temp_setup_styling(self):
        """A temp method for styling UI elements"""
        style = ttk.Style()
        style.configure("Bold.TLabel", font=("Sans", 10, "bold"))
        style.configure("Error.TLabel", background="#E77", foreground="#000")

        style.configure("Indent.TFrame", background="#CCC")
        style.configure("Indent.TLabel", background="#CCC")

        style.configure("Public.TFrame", background="#ACA")
        style.configure("Private.TFrame", background="#FEC")
        style.configure("Admin.TFrame", background="#FAA")
        style.configure("Public.TEntry", background="#ACA")
        style.configure("Private.TEntry", background="#FEC")
        style.configure("Admin.TEntry", background="#FAA")
        style.configure("PublicFieldTitle.TLabel", background="#ACA", font=("Sans", 10, "bold"))
        style.configure("PrivateFieldTitle.TLabel", background="#FEC", font=("Sans", 10, "bold"))
        style.configure("AdminFieldTitle.TLabel", background="#FAA", font=("Sans", 10, "bold"))
        style.configure("PublicField.TLabel", background="#ACA")
        style.configure("PrivateField.TLabel", background="#FEC")
        style.configure("AdminField.TLabel", background="#FAA")
        
        style.configure("Red.TFrame", background="#F00")
        style.configure("Green.TFrame", background="#0F0")
        style.configure("Blue.TFrame", background="#00F")
    def silence_pylint_too_few_public_methods(self):
        """Silences pylint error"""
