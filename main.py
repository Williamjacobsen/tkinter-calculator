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

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="black")
    gui.title("Calculator")

    l = Label(gui, text=str(stack), width=40, height=2)

    l.grid(columnspan=4)

    Button(gui, text='1', fg='white', bg='gray', command=lambda: set_stack(1), height=2, width=10).grid(row=1, column=0)
    Button(gui, text='2', fg='white', bg='gray', command=lambda: set_stack(2), height=2, width=10).grid(row=1, column=1)
    Button(gui, text='3', fg='white', bg='gray', command=lambda: set_stack(3), height=2, width=10).grid(row=1, column=2)
    Button(gui, text='4', fg='white', bg='gray', command=lambda: set_stack(4), height=2, width=10).grid(row=2, column=0)
    Button(gui, text='5', fg='white', bg='gray', command=lambda: set_stack(5), height=2, width=10).grid(row=2, column=1)
    Button(gui, text='6', fg='white', bg='gray', command=lambda: set_stack(6), height=2, width=10).grid(row=2, column=2)
    Button(gui, text='7', fg='white', bg='gray', command=lambda: set_stack(7), height=2, width=10).grid(row=3, column=0)
    Button(gui, text='8', fg='white', bg='gray', command=lambda: set_stack(8), height=2, width=10).grid(row=3, column=1)
    Button(gui, text='9', fg='white', bg='gray', command=lambda: set_stack(9), height=2, width=10).grid(row=3, column=2)
    Button(gui, text='0', fg='white', bg='gray', command=lambda: set_stack(0), height=2, width=10).grid(row=4, column=0)
    
    Button(gui, text='+', fg='white', bg='gray', command=lambda: set_stack('+'), height=2, width=10).grid(row=1, column=4)
    Button(gui, text='-', fg='white', bg='gray', command=lambda: set_stack('-'), height=2, width=10).grid(row=2, column=4)
    Button(gui, text='*', fg='white', bg='gray', command=lambda: set_stack('*'), height=2, width=10).grid(row=3, column=4)
    Button(gui, text='/', fg='white', bg='gray', command=lambda: set_stack('/'), height=2, width=10).grid(row=4, column=4)

    Button(gui, text='Calculate', fg='white', bg='gray', command=lambda: evaluate_stack(), height=2, width=10).grid(row=4, column=1)

    gui.mainloop()

