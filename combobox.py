# importing tkinter as tk so we can use the library throughout the code
import tkinter as tk
from tkinter import ttk

# function to use when button is clicked
def on_select(event):
    selected_item = event.widget.get()
    print("Selected item: ", selected_item)
    pass

# create root window and give it a title
root = tk.Tk()
root.title("Combobox Example!")

# make items to list in the combo box
items = ["this", "that", "here", "there"]

# add the combo box
combo_box = ttk.Combobox(root, values=items)

# Bind function ties the selected item to the on_select function
combo_box.bind("<<ComboboxSelected>>", on_select)
# pack the object to the screen w/ the geometery manager
combo_box.pack()


# start the mainloop of the root, which is needed to keep the UI visible
root.mainloop()

