# https://www.tutorialspoint.com/python3/python_gui_programming.htm
# https://python.readthedocs.io/en/stable/library/tkinter.html 

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text="1", command=lambda:self.add_to_stack(1)).pack(side="right")
        tk.Button(self, text="2", command=lambda:self.add_to_stack(2)).pack(side="right")
        tk.Button(self, text="3", command=lambda:self.add_to_stack(3)).pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def add_to_stack(self, item):
        print(item)

root = tk.Tk()
app = Application(master=root)
app.mainloop()

