# importing tkinter as tk so we can use the library throughout the code
import tkinter as tk

# function to use when button is clicked
def button_click():
    print("Button Clicked!")

# create root window and give it a title
root = tk.Tk()
root.title("Button Example :)")

# add the button to the root window, with the text "Click Me!", which will execute the button_click() function
button = tk.Button(root, text="Click Me!", command=button_click)
# then pack it!
button.pack()

# start the mainloop of the root, which is needed to keep the UI visible
root.mainloop()

