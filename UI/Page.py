
class Page:
    """A representation and container for a page's display"""

    def __init__(self, page_id:str, constructor):
        """Setup the page for loading
        
          Params:
              id: The page id to use
              constructor_func: The function used to construct the page
        """
        # Store the page id and page generation instructions
        self.id = page_id
        self.constructor_func = constructor
    
    def load(self, ui_core, *args) ->None:
        """Load the page
        
          Params:
              ui_core: The program ui_core
              *args: TooltipController, PageController.cache, PageController.page_data
        """
        # Run the page generation instructions (pass *args along)
        self.constructor_func(ui_core, *args)
    
    def get_id(self) ->str:
        """Return the page id
        
          Returns:
              page_id: The page id
        """
        # Return the page id
        return self.id
