#===============================================================================
#   Home.py (Python source file)
#
#   This file implements the home page user interface of the application.
#
#   Author(s):
#     Cameron C. Hingson (CCH) <cameron.hingson@gmail.com>
#===============================================================================
import tkinter as tk

class Home(tk.Frame):

  def __init__(self, parent):
    self.parent = parent
    self.frame = tk.Frame(self.parent)

    # Menu bar
    self.menubar = Menubar(self) # TODO: Fix unresolved imports bug
