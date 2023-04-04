from tkinter.ttk import Style
from tkinter import Tk
from UI.Theme import Theme

class ThemeController:
    def __init__(self, root:Tk):
        self.root = root
        self.themes = {}
        self.add_theme(Theme("default", "#111", "#555", "#FFF"))
        
        self.theme = self.themes["default"]
        self.apply_theme(self.theme)

        print(Style().layout("TEntry"))
    def add_theme(self, theme:Theme):
        self.themes[theme.id] = theme
    
    def set_theme(self, theme_id:str):
        if theme_id in self.themes:
            self.theme = self.themes[theme_id]
            self.apply_theme(self.theme)
        
    def apply_theme(self, theme:Theme):
        s = Style()
        self.root.configure(background=theme.bg_color)

        #B=Base
        s.configure("B.TFrame", background=theme.bg_color)

        #T=Theme
        s.configure("T.TFrame", background=theme.bg_color)
        s.configure("T.TLabel", background=theme.bg_color, foreground=theme.text_color)
        s.map("T.TButton",
            background=[("pressed", theme.bg_color), ("active", theme.bg_color), ("disabled", theme.fg_color)],
            foreground=[("pressed", theme.bg_color), ("active", theme.text_color), ("disabled", theme.text_color)]
        )
        s.configure("TEntry", fieldbackground=theme.bg_color, background=theme.bg_color, foreground=theme.bg_color)

        #TT=ToolTip
        s.configure("TT.TFrame", background=theme.bg_color)
        s.configure("TT.TLabel", background=theme.bg_color, foreground=theme.text_color)

