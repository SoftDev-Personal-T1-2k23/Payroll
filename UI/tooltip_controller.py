"""A file housing tooltip controller related things"""
from tkinter import Tk
from UI.Tooltip import Tooltip

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
    def on_enter(self, parent:Tk, elem_id:str)->None:
        """Perform necessary tooltip logic and show tooltip information reactively
        
          Params:
              parent: The tooltip's parent object to follow
              elem_id: The tooltip information id
        """
        root = self.ui_core.root

        # Retrieve tooltip information
        t_info = self.tooltip_info[elem_id]
        tooltip_offset = t_info[0]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        r_x, r_y = root.winfo_rootx(), root.winfo_rooty()
        p_x, p_y = parent.winfo_rootx(), parent.winfo_rooty()

        # Update tooltip information (title and desc)
        self.set_tooltip_info(tooltip_title, tooltip_desc)
        # Show tooltip
        self.show_tooltip(elem_id, p_x-r_x +tooltip_offset[0], p_y-r_y +tooltip_offset[1])
    def on_exit(self) ->None:
        """Perform necessary tooltip logic and hide tooltip reactively
        """
        # Hide the tooltip, if it exists
        self.hide_tooltip()

    def add_tooltip(self, parent:Tk, elem_id:str, offset:tuple, tt_info_pair) ->None:
        """'Add' a tooltip to the specified widget, and store the info for later
        
          Params:
              parent: The tooltip's parent object to follow
              elem_id: The tooltip information id
              tt_info_pair: The displayed tooltip title and desc (tuple)
        """
        title = tt_info_pair[0]
        desc = tt_info_pair[1]
        # Store tooltip information (title, desc) associated with a provided id
        if not elem_id in self.tooltip_info:
            offset = (offset[0], -offset[1]) #Invert y
            self.tooltip_info[elem_id] = (offset, title, desc)
        # Bind the mouse entering and leaving the widget to "on enter" and "on exit"
        parent.bind("<Enter>", lambda e: self.on_enter(parent, elem_id))
        parent.bind("<Leave>", lambda e: self.on_exit())

    def show_tooltip(self, elem_id:str, x_pos:int, y_pos:int) ->None:
        """Show the tooltip at the desired position (x, y) (rel. offset)
        
          Params:
            x_pos: X position for the tooltip
            y_pos: Y position for the tooltip
        """
        # Retrieve tooltip info
        t_info = self.tooltip_info[elem_id]
        tooltip_title = t_info[1]
        tooltip_desc = t_info[2]

        # Show the tooltip at the desired relative position (x, y)
        self.tooltip.set_title(tooltip_title)
        self.tooltip.set_description(tooltip_desc)
        self.tooltip.show(x_pos, y_pos)
    def hide_tooltip(self) ->None:
        """Hide the tooltip"""
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
    def set_tooltip_position(self, x_pos:int, y_pos:int):
        """Set the tooltip's position (x, y) (rel. offset)
        
          Params:
              x_pos: X position for the tooltip
              y_pos: Y position for the tooltip
        """
        # Set the tooltip's relative position (x, y)
        self.tooltip.set_position(x_pos, y_pos)
