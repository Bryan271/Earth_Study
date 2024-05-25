# main.py

# This file serves as the entry point for the application. 
# It initializes the main window, sets up the GUI, and starts 
# the event loop. The actual GUI logic and other functionalities 
# will be handled in the respective modules.

import tkinter as tk
from gui_module import AutomaticScreenshotGUI

# Creates the main window
root = tk.Tk()
root.title("Vector Mapping Prototype v1.1")
print("root.title")

# Creates an instance of the GUI class
gui = AutomaticScreenshotGUI(root)
print("gui")

# Start the GUI event loop
root.mainloop()
