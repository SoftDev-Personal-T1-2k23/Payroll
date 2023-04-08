from UI.Tooltip import Tooltip
from tkinter import Tk

class TooltipController:
    """A controller for tooltip lifespan and display"""

    def __init__(self, ui_core):
        """Setup necessary references, tooltip info cache, and tooltip
        
          Params:
              ui_core: The program UICore
        """
        # Create and store necessary references
        self.ui_core = ui_core
        # Create and store the tooltip
        self.tooltip = Tooltip(self.ui_core.root, "Title", "Description")
        # Setup the tooltip info cache
        self.tooltip_info = {}
    
    def on_enter(self, parent:Tk, id:str) ->None:
        """Perform necessary tooltip logic and show tooltip information reactively
        
          Params:
              parent: The tooltip's parent object to follow
              id: The tooltip information id
        """
        root = self.ui_core.root

        # Retrieve tooltip information
        t_info = self.tooltip_info[id]
        tooltip_offset = t_info[0]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        rx, ry = root.winfo_rootx(), root.winfo_rooty()
        x, y = parent.winfo_rootx(), parent.winfo_rooty()

        # Update tooltip information (title and desc)
        self.set_tooltip_info(tooltip_title, tooltip_desc)
        # Show tooltip
        self.show_tooltip(id, x-rx +tooltip_offset[0], y-ry +tooltip_offset[1])
            

    def on_exit(self, parent:Tk, id:str) ->None:
        """Perform necessary tooltip logic and hide tooltip reactively
        
          Params:
              parent: The tooltip's parent object to follow
              id: The tooltip information id
        """
        # Hide the tooltip, if it exists
        self.hide_tooltip()

    def add_tooltip(self, parent:Tk, id:str, offset:tuple, title:str, desc:str) ->None:
        """'Add' a tooltip to the specified widget, and store the info for later
        
          Params:
              parent: The tooltip's parent object to follow
              id: The tooltip information id
              title: The displayed tooltip title
              desc: The displayed tooltip description
        """
        # Store tooltip information (title, desc) associated with a provided id
        if not id in self.tooltip_info:
            offset = (offset[0], -offset[1]) #Invert y
            self.tooltip_info[id] = (offset, title, desc)
        # Bind the mouse entering and leaving the widget to "on enter" and "on exit"
        parent.bind("<Enter>", lambda e: self.on_enter(parent, id))
        parent.bind("<Leave>", lambda e: self.on_exit(parent, id))

    def show_tooltip(self, id:str, x:int, y:int) ->None:
        """Show the tooltip at the desired position (x, y) (rel. offset)
        
          Params:
              x: X position for the tooltip
              y: Y position for the tooltip
        """
        # Retrieve tooltip info
        t_info = self.tooltip_info[id]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        # Show the tooltip at the desired relative position (x, y)
        self.tooltip.set_title(tooltip_title)
        self.tooltip.set_description(tooltip_desc)
        self.tooltip.show(x, y)
    
    def hide_tooltip(self) ->None:
        """Hide the tooltip"""
        # Hide the tooltip  
        self.tooltip.hide()
    
    def set_tooltip_info(self, title:str, desc:str):
        """Set the tooltip's title and description
        
        Params:
            title: The new title
            desc: The new description
        """
        # Set tooltip title and description
        self.tooltip.set_title(title)
        self.tooltip.set_description(desc)
    
    def set_tooltip_position(self, x:int, y:int):
        """Set the tooltip's position (x, y) (rel. offset)
        
          Params:
              x: X position for the tooltip
              y: Y position for the tooltip
        """
        # Set the tooltip's relative position (x, y)
        self.tooltip.set_position(x, y)