#===============================================================================
#   Union.py (Python source file)
#
#   This file implements the top level of the Union application. Union uses
#   tkinter to implement its user interfaces and attempts to adhere to a
#   model-view-controller (MVC) architecture. The application is currently
#   intended for a 32-bit architecture.
#
#   References:
#     tkinter
#       https://docs.python.org/3/library/tkinter.html#module-tkinter
#     Model-View-Controller (MVC)
#       https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
#
#   Author(s):
#     Cameron C. Hingson  (CCH) <cameron.hingson@gmail.com>
#===============================================================================
import sys
import os
import tkinter as tk

sys.path.append(os.path.join(
  os.path.dirname(os.path.realpath(__file__)), "View"))

from Menubar import Menubar
from Home import Home

class App(tk.Frame):

  def __init__(self, parent):
    tk.Frame.__init__(self, parent)

    # Attach to the root
    self.parent = parent;

    # Set the window's dimensions
    width = 800
    height = 450
    x = 0
    y = 0
    self.parent.geometry(str(width) +
                         "x" +
                         str(height) +
                         "+" +
                         str(x) +
                         "+" +
                         str(y))

    # Window header bar
    self.parent.title("Union")
    self.parent.iconbitmap(os.path.join(
      os.path.dirname(os.path.realpath(__file__)), "Icons", "Camera.ico"))

    # Menu bar (cannot attach to frames so it is attached directly to the root)
    menubar = Menubar(self.parent)
    self.parent.config(menu = menubar)

    # Home page
    home = Home(self)

def main():
  root = tk.Tk()
  app = App(root)
  root.mainloop()

if __name__ == "__main__":
  main()
