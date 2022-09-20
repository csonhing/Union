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
    tk.Frame.__init__(self, parent)
    self.parent = parent

    # Instantiate a CCP for each camera (currently 8)
