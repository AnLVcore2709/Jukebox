# Import the font module from tkinter for font configuration
import tkinter.font as tkfont


# This function configures the default fonts used throughout the Tkinter GUI
def configure():
    # Set the preferred font family (you can change it to any available system font)
    family = "Helvetica"

    # Get the default font used by most Tkinter widgets (like buttons, labels, etc.)
    default_font = tkfont.nametofont("TkDefaultFont")
    # Change the font size and family for these general widgets
    default_font.configure(size=15, family=family)

    # Get the font used by text-based widgets (like Text, Entry, etc.)
    text_font = tkfont.nametofont("TkTextFont")
    # Set the font size and family for better readability
    text_font.configure(size=12, family=family)

    # Get the fixed-width font, usually used for code-like or terminal-style text
    fixed_font = tkfont.nametofont("TkFixedFont")
    # Configure its size and family to maintain consistency across all fonts
    fixed_font.configure(size=12, family=family)
