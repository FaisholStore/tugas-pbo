import tkinter as tk

def on_button_click():
    label.configure(text="Hello, Tkinter!")

root = tk.Tk()
root.title("My Tkinter App")

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

root.mainloop()
