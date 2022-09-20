#===============================================================================
#   CameraControl.py (Python source file)
#
#   This file implements an individual camera's control panel. These control
#   panels are intended to be used multiple times, one for each camera.
#   Implementing the control panels on an individual basis gives all the
#   functionality that is required to control the camera while allowing the
#   instantiating user interface element to set up its layout however it
#   pleases.
#
#   Author(s):
#     Cameron C. Hingson  (CCH) <cameron.hingson@gmail.com>
#===============================================================================
import tkinter as tk

# Camera control panel... What else could it stand for? (CCH)
class CCP(tk.Frame):

  def __init__(self, parent):
    tk.Frame.__init__(self, parent)
    self.parent = parent

    # Connection status light

    # Camera identifiers

    # Camera control buttons

    # Camera rotation control (in degrees)

    # Preview/Program buttons

    # Presets menu and confirmation button
