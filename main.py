# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://stackoverflow.com/questions/40331904/showing-square-root-symbol-in-tkinter-label-python 

from tkinter import *
import math
import os

if os.name == 'nt':
    os.system('cls')
else: 
    os.system('clear')

stack = ""

def set_stack(n):
    global stack
    stack = str(stack)
    
    stack += str(n)

    l.config(text = stack)
    print(stack)

def stack_clear():
    stack = ""
    l.config(text = stack)

def stack_clear_latest():
    global stack
    stack = stack[:-1]
    l.config(text = stack)
    print(stack)

def _round():
    global stack

    evaluate_stack()
    stack = str(round(float(stack), 2))

    l.config(text = stack)

def squared():
    global stack

    stack = eval(f"({stack})**2")
    l.config(text = stack)

def evaluate_stack(): 
    global stack   

    if '\u221A' in stack: # sqrt
        stack = stack.split('\u221A')

        for i in range(1, len(stack), 2):
            stack[i] = math.sqrt(float(eval(stack[i])))

        for i in range(len(stack)):
            stack[i] = str(stack[i])
        stack = ''.join(stack)

    stack = str(eval(str(stack)))
    print(stack)
    l.config(text = stack)

def create_btn(op: str, row: int, column: int):
    Button(gui, text=op, fg='white', bg='gray', command=lambda: set_stack(op), height=2, width=10).grid(row=row, column=column)

if __name__ == '__main__':
    gui = Tk()
    gui.configure(background="gray")
    gui.title("Calculator")

    l = Label(gui, text=str(stack), width=20, height=2, font=40)

    l.grid(column=0, columnspan=3)

    create_btn('7', 1, 0)
    create_btn('8', 1, 1)
    create_btn('9', 1, 2)
    create_btn('4', 2, 0)
    create_btn('5', 2, 1)
    create_btn('6', 2, 2)
    create_btn('1', 3, 0)
    create_btn('2', 3, 1)
    create_btn('3', 3, 2)
    create_btn('0', 4, 0)

    create_btn('.', 4, 1)
    create_btn('/', 1, 4)
    create_btn('*', 2, 4)
    create_btn('-', 3, 4)
    create_btn('+', 4, 4)
    create_btn('\u221A', 0, 4) # sqrt
    create_btn('(', 1, 5)
    create_btn(')', 1, 6)
    Button(gui, text='x\u00B2', fg='white', bg='gray', command=squared, height=2, width=10).grid(row=4, column=2) # squared

    Button(gui, text='C', fg='white', bg='gray', command=stack_clear, height=2, width=10).grid(row=0, column=6)
    Button(gui, text='\u293A', fg='white', bg='gray', command=stack_clear_latest, height=2, width=10).grid(row=0, column=5) # arrow back
    Button(gui, text='Round', fg='white', bg='gray', command=_round, height=2, width=10).grid(row=3, column=6)
    Button(gui, text='Calculate', fg='white', bg='gray', command=evaluate_stack, height=2, width=10).grid(row=4, column=6)

    gui.mainloop()