"""A tooltip shown throughout the program"""
from tkinter import Tk, TOP, LEFT, BOTTOM, TRUE
from tkinter import ttk

class Tooltip:
    """A tooltip that can be shared between pages"""

    def __init__(self, root:Tk, title:str, desc:str):
        """Setup and create the tooltip
        
          Params:
              root: The tkinter root
              title: The tooltip title
              desc: The tooltip description
        """
        # Setup necessary fields (see class diagram)
        self.root = root
        self.tooltip_id = None
        self.frame = None
        self.label_title = None
        self.label_desc = None
        self.title = title
        self.description = desc
        self.x_pos = 0
        self.y_pos = 0
        self.is_hidden = True

        # Create the tooltip widget(s)
        style = ttk.Style()
        style.configure("Tooltip.TFrame", background="#AAA")
        style.configure("Tooltip.TLabel", background="#AAA")
        style.configure("TooltipBold.TLabel", background="#AAA", font=("Sans", 10, "bold"))

        frame = ttk.Frame(self.root, style="Tooltip.TFrame", width=20)

        panel_top = ttk.Frame(frame, style="Tooltip.TFrame")
        label_title = ttk.Label(panel_top, text=title, style="TooltipBold.TLabel")

        panel_bottom = ttk.Frame(frame, style="Tooltip.TFrame")
        label_desc = ttk.Label(panel_bottom, text=desc, style="Tooltip.TLabel")
        panel_top.pack(side=TOP, expand=TRUE)
        label_title.pack(side=LEFT)
        panel_bottom.pack(side=BOTTOM, expand=TRUE)
        label_desc.pack(side=LEFT)
        # Setup field vars
        self.tooltip_id = frame.winfo_id()
        self.frame = frame
        self.label_title = label_title
        self.label_desc = label_desc
        self.hide()

    def show(self, x_pos:int, y_pos:int) ->None:
        """Show the tooltip at the desired position (x, y) (rel. offset)
        
          Params:
              x_pos: X position for the tooltip
              y_pos: Y position for the tooltip
        """
        # Update the stored x and y locations
        self.set_position(x_pos, y_pos)
        self.is_hidden = False

        # Show the tooltip at a specified location
        self.frame.place(x=x_pos, y=y_pos)
        self.frame.lift()
    def hide(self):
        """Hide the tooltip"""
        # Hide the tooltip
        self.is_hidden = True
        self.frame.lower()
    def set_position(self, x_pos:int, y_pos:int):
        """Set the tooltip at the desired position x and y (rel. offset)
        
          Params:
              x_pos: X position for the tooltip
              x_pos: Y position for the tooltip
        """
        # Update the position vars
        self.x_pos = x_pos
        self.y_pos = y_pos
    def get_position(self) -> tuple:
        """Get the tooltip's position
        
        Returns:
            tooltip_pos: A tuple containing the tooltip's x and y offsets
        """
        # Return the tooltip's position as a tuple (x,y)
        return (self.x_pos, self.y_pos)

    def set_title(self, title:str):
        """Set the tooltip's title
        
          Params:
              title: The tooltip title to use
        """
        # Set the tooltip's title
        self.title = title
        self.label_title.configure(text=title)

    def set_description(self, desc:str):
        """Set the tooltip's description
        
          Params:
              desc: The tooltip description to use
        """
        # Set the tooltip's description
        self.description = desc
        self.label_desc.configure(text=desc)
