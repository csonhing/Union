#===============================================================================
#   Menubar.py (Python source file)
#
#   This file implements a menubar that commonly seen at the top of most
#     applications that contains drop down menus with headings like File, Edit,
#     View, Help, etc.
#
#   Author(s):
#     Cameron C. Hingson (CCH) <cameron.hingson@gmail.com>
#===============================================================================
import tkinter as tk

class Menubar(tk.Menu):

  def __init__(self, parent):
    self.parent = parent
    self.menubar = tk.Menu(self.parent)

    # File drop-down menu
    filemenu = tk.Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "Settings")
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = self.parent.destroy)
    self.menubar.add_cascade(label = "File", menu = filemenu)

    self.parent.config(menu = self.menubar)