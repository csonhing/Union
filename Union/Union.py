# tkinter docs: https://docs.python.org/3/library/tkinter.html#module-tkinter  
import tkinter as tk

# root represents the main window of the application
root = tk.Tk()

# Header bar
root.title("Union")
root.iconbitmap('CCoC_Logo1.ico')

# Menu bar
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Settings")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)

root.config(menu = menubar)
root.mainloop()