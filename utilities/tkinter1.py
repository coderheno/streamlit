import tkinter as tk
root = tk.Tk()
a = tk.Entry(root)
a.pack()
b = tk.Entry(root)
b.pack()

add = tk.Button(root, text="Add Numbers")
add.pack()

root.mainloop()
