from tkinter import *
from tkinter import ttk

class Tooltip:
    def __init__(self, root:Tk, title:str, desc:str):
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
        
        self.tooltip_id = frame.winfo_id()
        self.frame = frame
        self.label_title = label_title
        self.label_desc = label_desc
        self.hide()

    def show(self, x:int, y:int):
        self.set_position(x, y)
        self.is_hidden = False

        self.frame.place(x=x, y=y)
        self.frame.lift()
    
    def hide(self):
        self.is_hidden = True
        self.frame.lower()
    
    def set_position(self, x:int, y:int):
        self.x_pos = x
        self.y_pos = y
    
    def set_title(self, title:str):
        self.title = title
        self.label_title.configure(text=title)

    def set_description(self, desc:str):
        self.description = desc
        self.label_desc.configure(text=desc)
