
class Page:
    def __init__(self, page_id:str, constructor):
        self.id = page_id
        self.constructor_func = constructor
    
    def load(self, ui_core, *args):
        self.constructor_func(ui_core, *args)
    
    def get_id(self):
        return self.id
