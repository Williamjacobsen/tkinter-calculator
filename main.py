# https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
import os
os.system('clear')

stack = ""
def set_stack(n):
    global stack
    stack += str(n)
    l.config(text = stack)
    print(stack)

def evaluate_stack():
    l.config(text = eval(stack))

def create_btn(op: str, row: int, column: int):
    Button(gui, text=op, fg='white', bg='gray', command=lambda: set_stack(op), height=2, width=10).grid(row=row, column=column)

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="black")
    gui.title("Calculator")

    l = Label(gui, text=str(stack), width=40, height=2)

    l.grid(columnspan=4)

    create_btn('1', 1, 0)
    create_btn('2', 1, 1)
    create_btn('3', 1, 2)
    create_btn('4', 2, 0)
    create_btn('5', 2, 1)
    create_btn('6', 2, 2)
    create_btn('7', 3, 0)
    create_btn('8', 3, 1)
    create_btn('9', 3, 2)
    create_btn('0', 4, 0)

    create_btn('+', 1, 4)
    create_btn('-', 2, 4)
    create_btn('*', 3, 4)
    create_btn('/', 4, 4)
    Button(gui, text='Calculate', fg='white', bg='gray', command=evaluate_stack, height=2, width=10).grid(row=4, column=1)

    gui.mainloop()

