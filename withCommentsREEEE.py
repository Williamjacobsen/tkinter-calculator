# Dette er vores lommeregner lavet i python med tkinter liberary'et.
# Jeg har ikke fulgt tutorialen, det er pga. da jeg startede min programmerings "karriere",
# sad jeg fast i termet 'tutorial hell', derfor vil jeg aldrig blindt følge en tutorial igen,
# lige meget om du føler at du lærer noget, så snart du selv skal lave noget eller løse et problem,
# har du ingen ide hvad du skal og hvordan du løser problemet.
# 
# 1. https://www.tutorialspoint.com/python/python_gui_programming.htm
# tkinter documentation, her har jeg eksempler på brug af f.eks. Label()
#
# 2. https://stackoverflow.com/questions/40331904/showing-square-root-symbol-in-tkinter-label-python 
# brugt til at få et unicode symbol ind i koden, (så det er visulet i stedet for bogstaver)
#
# 3. https://www.compart.com/en/unicode/U+00B2
# unicode til x i anden
# 

# tkinter, til at lave gui
# from tkinter import *, så jeg tilgør ting dirkete, det betyder dog ikke meget,
# det gør bare så at jeg ikke skal sige tkinter.Tk() men bare Tk()
from tkinter import *
# math, ikke rigtigt nødvædnigt, men hvis der skulle tilføjes mere avanceret ting, vil den være nødvændig,
# dog bruger jeg det til math.sqrt() men man kunne godt bare gøre **0.5, men det er ikke ligeså sexy.
import math

# her er lidt kode til at ryde terminalen både på windows og mac/linux
import os # adgang til systemet
if os.name == 'nt': # hvis den hedder 'new technologies' aka windows
    os.system('cls') # command for at ryde terminalen på windows
else: # hvis det er mac eller linux
    os.system('clear') # command til at tyde terminalen på mac og linux

# stack, det er der vores udregning og formel er
stack = ""
# her er historikken af vores udregninger
stack_history = []

def set_stack(n): # en function der tilføjer 'n' til 'stack'
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)
    stack = str(stack) # lav det til en string
    # gruden til vi laver 'stack' til en string er at hvis vi vil pluse eller tilføje noget til den,
    # er det en nem måde at undgå errors, f.eks. man kan til tilføje en type 'int' til en type 'str'
    stack += str(n) # lav den til type 'str' så begge er type 'str'

    equestion.config(text = stack) # updatere vores text label til 'stack'

def stack_clear(): # ryd hele 'stack'en
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)
    stack = "" # lav den til ingen ting eller ""
    equestion.config(text = stack) # updatere vores text label til 'stack' hvilket nu er ingen ting eller ""

def stack_clear_latest(): # ryd den sidste i 'stack'
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)
    stack = stack[:-1] # tag alt undtagen den sidste index, og sæt det til 'stack'
    equestion.config(text = stack) # updatere vores text label til 'stack'

def _round(): # rund 'stack' til det nærmeste 2 cifre
    # gruden til der er et _ (underscore) foran teksten er fordi der allerede eksistere en 'round' funktion,
    # så få at lave min egen uden at køre en allerede eksisrerende funktion er der et _ (underscore) foran
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)

    evaluate_stack() # kør funktion der udregner/evaluater 'stack'
    stack = str(round(float(stack), 2)) # sæt 'stack' til det nærmeste 2 cifre, og lav den til type 'str'

    equestion.config(text = stack) # updatere vores text label til 'stack'

def squared(): # sæt 'stack' i anden
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)

    stack = str(eval(f"({stack})**2")) # sæt 'stack' til udregnet 'stack' i anden, i type 'str' (** er i anden)
    equestion.config(text = stack) # updatere vores text label til 'stack'

def update_stack_history(): # hver gang 'stack' bliver udregnet, tilføjer vi den til 'stack_history' array'et
    global stack_history # få adgang til global scope (så vi kan tilgå vores 'stack_history' variabel inde i en funktion)
    if len(stack_history) >= 5: # så der kun er fem
        stack_history.pop(0) # hvis der er fem eller flere, fjerner/pop'er den, den første i array'et
    history.config(text = str('\n'.join(stack_history))) # updatere vores 'stack_history' array label til,
    # en str der laver en ny linje (\n) hver gang der er et nyt element i array'et

def evaluate_stack(): # evaluate / udregn 'stack'
    global stack # få adgang til global scope (så vi kan tilgå vores 'stack' variabel inde i en funktion)
    global stack_history # få adgang til global scope (så vi kan tilgå vores 'stack_history' variabel inde i en funktion)

    # \u221A er kvadratrod symbelet, se kilde 2.
    if '\u221A' in stack: # hvis '\u221A' er i 'stack'
        stack = stack.split('\u221A') # opdel, i array for hver hvadratrod symbol

        # eksempel,
        # stack = "\u221A50"
        # stack.split('\u221A')
        # ['', '50']

        for i in range(1, len(stack), 2): # start på index 1 (2, lmao), sprig en over hver gang
            stack[i] = math.sqrt(float(eval(stack[i]))) # såt det nuværende index i array'et, 
            # til den den udregnet index i array'et,
            # og tag kvadratroden af den

        for i in range(len(stack)): # gå igennem alle elementer/indexer
            stack[i] = str(stack[i]) # lav dem til type 'str'
        stack = ''.join(stack) # sæt dem sammen i en 'str' mellem hver '', 
        # hvilket sætter det sammen i en lang køre f.eks. 323+2313-32/3232*23

    stack = str(eval(str(stack))) # udregn 'stack' og lav det til type 'str'

    stack_history.append(stack) # tilføj det til historikken
    update_stack_history() # udater historikken (funktion)
    
    equestion.config(text = stack) # updatere vores text label til 'stack'

def create_btn(op: str, row: int, column: int): # lav en knap, op er teksten knapen viser / operator'en
    # se kilde 1. for brug af Button()
    Button(gui, text=op, fg='white', bg='gray', command=lambda: set_stack(op), height=2, width=10).grid(row=row, column=column)

if __name__ == '__main__': # se under
    # hvis __name__ er det samme som __main__, har du kørt filen direkte,
    # eller vil __name__ være det samme som den fil du har importeret den fra,
    # og dermed ikke køre

    # basic setup af tkinter, se kilde 1.
    gui = Tk()
    gui.configure(background="gray")
    gui.title("Calculator")

    # brug af Label(), se kilde 1.
    equestion = Label(gui, text=str(stack), width=20, height=2, font=40) # teksten der viser udregnigen
    equestion.grid(column=0, columnspan=3) # den er placeret i column 0, og fylder 3 column
    history = Label(gui, text="", width=10, height=12, font=40) # teksten for historikken
    history.grid(column=7, row=0, rowspan=5) # same princip omfggggg

    # kør funktion der laver en knap, '7' er teksten, 1 er row, 0 er column
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

    # samme princip omfg
    Button(gui, text='x\u00B2', fg='white', bg='gray', command=squared, height=2, width=10).grid(row=4, column=2) # squared
    Button(gui, text='C', fg='white', bg='gray', command=stack_clear, height=2, width=10).grid(row=0, column=6)
    Button(gui, text='\u293A', fg='white', bg='gray', command=stack_clear_latest, height=2, width=10).grid(row=0, column=5) # arrow back
    Button(gui, text='Round', fg='white', bg='gray', command=_round, height=2, width=10).grid(row=3, column=6)
    Button(gui, text='Calculate', fg='white', bg='gray', command=evaluate_stack, height=2, width=10).grid(row=4, column=6)

    # få den til at køre alt den oversåtende kode, se kilde 1.
    gui.mainloop()