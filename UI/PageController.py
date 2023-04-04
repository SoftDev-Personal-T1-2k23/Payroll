from UI.Page import Page
import os
import sys
# import Modules.ModuleLoader as ModuleLoader
import UI.PageConstructors as PageConstructors

# PAGE_CONSTRUCTOR_DIR = "UI\PageConstructors"
def LoadPageConstructor(page_id:str):
    return PageConstructors.__dict__[f"PageConstructor_{page_id}"].constructor
#     module_path = os.path.join(PAGE_CONSTRUCTOR_DIR, f"PageConstructor_{page_id}.py")
#     module = ModuleLoader.LoadModule(module_path)
#     return module.constructor if module else None

class PageController:
    def __init__(self, ui_core):
        self.ui_core = ui_core
        self.cache = {
            "images": {}
        }
        self.page_cache = {}
        self.page = None
        self.page_data = None
        self.prev_page = None
        self.prev_page_data = None

    def store_current_page(self) ->None:
        self.prev_page = self.page
        self.prev_page_data = self.page_data
        self.page = None
        self.page_data = None
    
    def open_prev_page(self) ->None:
        if not self.prev_page: return
        self.prev_page, self.page = self.page, self.prev_page
        self.prev_page_data, self.page_data = self.page_data, self.prev_page_data

        self.clear_page()
        self.page.load(self.ui_core, self.ui_core.tooltip_controller, self.cache, self.page_data)

    def open_page(self, page_id:str) ->None:
        if self.page is not None:
            self.clear_page()

        page = None
        if not page_id in self.page_cache:
            page_constructor = LoadPageConstructor(page_id)
            if not page_constructor:
                print(f"Failed to load page [{page_id}]")
                return
            
            page = Page(page_id, page_constructor)
        else:
            page = self.page_cache[page_id]
        
        self.store_current_page()
        self.page = page
        self.page_data = {}

        self.page.load(self.ui_core, self.ui_core.tooltip_controller, self.cache, self.page_data)
    
    def clear_page(self) ->None:
        
        for ui_element in self.ui_core.root.winfo_children():
            if ui_element.winfo_class() == "TFrame":
                if ui_element.winfo_id() != self.ui_core.tooltip_controller.tooltip.tooltip_id:
                    ui_element.destroy()
