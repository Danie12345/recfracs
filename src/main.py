import fractions
from itertools import tee
from screeninfo import get_monitors
import tkinter as tk
import fracs.loopfracs as loopfracs
import fracs.recfracs as recfracs

# Window initialization
WIN_WIDTH = 350
WIN_HEIGHT = 250
root = tk.Tk()
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{(get_monitors()[0].width - WIN_WIDTH)//2}+{(get_monitors()[0].height - WIN_HEIGHT)//2}")


# Convenient storage of functions
algorithms = {'Recursion': recfracs, 'Loops': loopfracs}
fraction = algorithms['Recursion']


# Main frame with inputs and outputs
frame1 = tk.Frame(root)

algorithmName = tk.StringVar(value = 'Recursion')
algoritmLabel = tk.Label(frame1, textvariable = algorithmName)

decimalVar = tk.DoubleVar(value = 1.0)
decimalInput = tk.Entry(frame1, textvariable = decimalVar)

numeratorVar = tk.IntVar(value = 1)
numeratorInput = tk.Label(frame1, textvariable = numeratorVar)

denominatorVar = tk.IntVar(value = 1)
denominatorInput = tk.Label(frame1, textvariable = denominatorVar)

algoritmLabel.pack()
decimalInput.pack()
numeratorInput.pack()
denominatorInput.pack()


# Algorithm switcher
def switch_algorithm(type):
  fraction = algorithms[type]
  algorithmName.set(type)


# Main navigation
navMenu = tk.Menu(root)
algorithmMenu = tk.Menu(navMenu, tearoff = 0)
algorithmMenu.add_command(label = 'Recursive', command = lambda: switch_algorithm('Recursion'))
algorithmMenu.add_command(label = 'Loops', command = lambda: switch_algorithm('Loops'))
navMenu.add_cascade(label = 'Algorithm', menu = algorithmMenu)


# Pack pertinent widgets to root window
frame1.pack()


# Configure menu into root
root.config(menu = navMenu)


# Initiate mainloop sequence
root.mainloop()