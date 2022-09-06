#===============================================================================
#   Union.py (Python source file)
#
#   This file implements the top level of the Union application. Union uses
#   tkinter to implement its user interfaces and attempts to adhere to a
#   model-view-controller (MVC) architecture.
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
import os
import tkinter as tk

class App(tk.Frame):

  def __init__(self, parent):
    # Attach to the root
    self.parent = parent;
    self.frame = tk.Frame(self.parent)

    # Window header bar
    self.parent.title("Union")
    self.parent.iconbitmap(os.path.join(
      os.path.dirname(os.path.realpath(__file__)),"CCoC_Logo1.ico"))

    # Home page
    home = Home(self) # TODO: Fix unresolved imports bug

def main():
  root = tk.Tk()
  app = App(root)
  root.mainloop()

if __name__ == "__main__":
  main()