import fractions
from itertools import tee
from screeninfo import get_monitors
import tkinter as tk
import fracs.loopfracs as loopfracs
import fracs.recfracs as recfracs

WIN_WIDTH = 350
WIN_HEIGHT = 250

root = tk.Tk()
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{(get_monitors()[0].width - WIN_WIDTH)//2}+{(get_monitors()[0].height - WIN_HEIGHT)//2}")

algorithms = {'Recursion': recfracs, 'Loops': loopfracs}
fraction = algorithms['Recursion']


frame1 = tk.Frame(root)
algorithmName = tk.StringVar(value = 'Recursion')
algoritmLabel = tk.Label(frame1, textvariable = algorithmName)

decimal = tk.DoubleVar(value = 1.0)
decimalInput = tk.Entry(frame1, textvariable = decimal)

numeratorInput = tk.Label(frame1)
numerator = tk.IntVar()

denominatorInput = tk.Label(frame1)
denominator = tk.IntVar()

algoritmLabel.pack()
decimalInput.pack()
numeratorInput.pack()
denominatorInput.pack()


def switch_algorithm(type):
  fraction = algorithms[type]
  algorithmName.set(type)

navmenu = tk.Menu(root)
algorithm = tk.Menu(navmenu, tearoff=0)
algorithm.add_command(label = 'Recursive', command = lambda: switch_algorithm('Recursion'))
algorithm.add_command(label = 'Loops', command = lambda: switch_algorithm('Loops'))
navmenu.add_cascade(label = 'Algorithm', menu = algorithm)


frame1.pack()


root.config(menu = navmenu)

root.mainloop()