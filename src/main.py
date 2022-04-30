from screeninfo import get_monitors
import tkinter as tk
import fracs.loopfracs as loopfracs
import fracs.recfracs as recfracs

WIN_WIDTH = 350
WIN_HEIGHT = 250

root = tk.Tk()
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{(get_monitors()[0].width - WIN_WIDTH)//2}+{(get_monitors()[0].height - WIN_HEIGHT)//2}")

navmenu = tk.Menu(root)
submenu1 = tk.Menu(navmenu, tearoff=0)
submenu1.add_command(label='Recursive')
submenu1.add_command(label='Loops')
navmenu.add_cascade(label='Algorithm', menu=submenu1)

root.config(menu=navmenu)

root.mainloop()