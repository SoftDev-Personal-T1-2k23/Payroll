from UI.Page import Page
import os
import sys
# import Modules.ModuleLoader as ModuleLoader
import UI.PageConstructors as PageConstructors
import payroll

# PAGE_CONSTRUCTOR_DIR = "UI\PageConstructors"
def LoadPageConstructor(page_id:str):
    return PageConstructors.__dict__[f"PageConstructor_{page_id}"].constructor
#     module_path = os.path.join(PAGE_CONSTRUCTOR_DIR, f"PageConstructor_{page_id}.py")
#     module = ModuleLoader.LoadModule(module_path)
#     return module.constructor if module else None

class PageController:
    """A class that controls and manages page changes"""

    def __init__(self, ui_core):
        """Perform required preparation for page management and display
         
          Params:
              ui_core: The application UICore
        """
        # Set ui_core reference
        self.ui_core = ui_core

        # Setup a global page cache (to store images and other persistent data)
        self.cache = {
            "images": {}
        }
        # Setup a page-local caches
        self.page_cache = {}

        # Declare future fields
        self.page = None
        self.page_data = None
        self.prev_page = None
        self.prev_page_data = None

    def store_current_page(self) ->None:
        """Store the current page's data"""
        # Store the current page fields in the previous page fields
        self.prev_page = self.page
        self.prev_page_data = self.page_data
        # Clear the current page fields
        self.page = None
        self.page_data = None
    
    def open_prev_page(self) ->None:
        #"""Open the previously opened page (ease of use)
        #
        #   Returns:
        #       success: Whether a previous page was successfully loaded
        #"""
        # If there was no previous page then return.
        if not self.prev_page: return

        # Setup and load the previous page's cached data
        self.prev_page, self.page = self.page, self.prev_page
        self.prev_page_data, self.page_data = self.page_data, self.prev_page_data

        # Load the desired page
        self.clear_page()
        self.page.load(self.ui_core, self.ui_core.tooltip_controller, self.cache, self.page_data)

    def open_page(self, page_id:str, employee = None) ->None:

        """Clear the current page and open the desired page
        
          Params:
              page_id: The page's associated page_id to load from

        """
        #if there was an employee provided that set the target
        if employee is not None:
            # print("EMPLOYEE PROVIDED")
            payroll.TARGET_USER = employee

        # Check if a page exists and clear and store it if it does
        if self.page is not None:
            self.clear_page()

        page = None
        if not page_id in self.page_cache:
            # Load the page from the specified python page module, otherwise (and cache it as a page)
            page_constructor = LoadPageConstructor(page_id)
            if not page_constructor:
                print(f"Failed to load page [{page_id}]")
                return
            
            page = Page(page_id, page_constructor)
        else:
            # Load the page from the page_cache, if it has already been loaded
            page = self.page_cache[page_id]
        
        # Update class page fields
        self.store_current_page()
        self.page = page
        self.page_data = {}
        
        # Load the desired page
        self.page.load(self.ui_core, self.ui_core.tooltip_controller, self.cache, self.page_data)
    
    def clear_page(self) ->None:
        """Clear the currently displayed page"""
        # Clear the tkinter root child widgets
        for ui_element in self.ui_core.root.winfo_children():
            if ui_element.winfo_class() == "TFrame":
                if ui_element.winfo_id() != self.ui_core.tooltip_controller.tooltip.tooltip_id:
                    ui_element.destroy()
    
    def get_current_page(self) -> Page:
        """Get the current page
        
        Returns:
            current_page: The currently shown page
        """
        # Return the current page instance
        return self.page
    
    def get_current_page_data(self) -> dict:
        """Return the current page data
        
          Returns:
              page_data: The currently shown page's data
        """
        # Return the current page's data
        return self.page_data
    
    def get_prev_page_data(self) -> dict:
        """Return the previous page's data
        
          Returns:
              page_data: The previously shown page's data
        """
        # Return the previous page's data
        return self.get_prev_page_data


