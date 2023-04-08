from tkinter.ttk import Style
from tkinter import Tk
from UI.Theme import Theme

class ThemeController:
    """A controller for managing UI color themes"""

    def __init__(self, root:Tk):
        """Setup necessary references, storage, and prepare the default theme
        
            Params:
                root: The tkinter root
        """
        # Store reference to root
        self.root = root
        # Setup storage for themes
        self.themes = {}
        # Add and create the default theme
        self.add_theme(Theme("default", "#111", "#555", "#FFF"))
        # Set the current theme as the default theme
        self.theme = self.themes["default"]
        # Apply the current theme
        self.apply_theme(self.theme)

    def add_theme(self, theme:Theme) ->None:
        """Add a new theme to the list of themes
        
          Params:
              theme: The theme to store
        """
        # Add the provided theme to the stored list of themes
        self.themes[theme.id] = theme
    
    def set_theme(self, theme_id:str) ->None:
        """Set the current theme to the desired theme and apply it
        
          Params:
              theme_id: The theme id used to lookup and apply
        """
        # Check if the theme_id exists, return if it does not
        if theme_id in self.themes:
            # Set the current theme to the desired theme
            self.theme = self.themes[theme_id]
            # Apply the desired theme
            self.apply_theme(self.theme)
        
    def apply_theme(self, theme:Theme):
        """Apply the provided theme to the UI elements
        
          Params:
              theme: The theme to apply
        """
        # Apply the provided theme to the UI elements
        # &
        # Configure the tkinter stylings for UI elements used across the various pages
        #       Use notation: "T.XXXX"

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

