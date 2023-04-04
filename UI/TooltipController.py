from UI.Tooltip import Tooltip
from tkinter import Tk

class TooltipController:
    def __init__(self, ui_core):
        self.ui_core = ui_core
        self.tooltip = Tooltip(self.ui_core.root, "Title", "Description")
        self.tooltip_info = {}
    
    def on_enter(self, parent:Tk, id:str):
        if not self.tooltip.frame:
            self.tooltip.refresh()
        root = self.ui_core.root

        t_info = self.tooltip_info[id]
        tooltip_offset = t_info[0]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        rx, ry = root.winfo_rootx(), root.winfo_rooty()
        x, y = parent.winfo_rootx(), parent.winfo_rooty()

        self.set_tooltip_info(tooltip_title, tooltip_desc)
        self.show_tooltip(id, x-rx +tooltip_offset[0], y-ry +tooltip_offset[1])
            

    def on_exit(self, parent:Tk, id:str):
        self.hide_tooltip()

    def add_tooltip(self, parent:Tk, id:str, offset:tuple, title:str, desc:str):
        if not id in self.tooltip_info:
            offset = (offset[0], -offset[1]) #Invert y
            self.tooltip_info[id] = (offset, title, desc)
        parent.bind("<Enter>", lambda e: self.on_enter(parent, id))
        parent.bind("<Leave>", lambda e: self.on_exit(parent, id))

    def show_tooltip(self, id:str, x:int, y:int):
        t_info = self.tooltip_info[id]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        self.tooltip.set_title(tooltip_title)
        self.tooltip.set_description(tooltip_desc)
        self.tooltip.show(x, y)
    
    def hide_tooltip(self):
        self.tooltip.hide()
    
    def set_tooltip_info(self, title:str, desc:str):
        self.tooltip.set_title(title)
        self.tooltip.set_description(desc)
    
    def set_tooltip_position(self, x:int, y:int):
        self.tooltip.set_position(x, y)