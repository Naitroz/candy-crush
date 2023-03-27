import tkinter as tk
import random
import re
import pprint

window = tk.Tk()
g = [[3, 1, 2, 4, 3, 4, 2, 4, 1],[1, 2, 2, 1, 3, 3, 3, 3, 2],[1, 3, 2, 3, 4, 1, 1, 3, 4],[2, 3, 1, 2, 3, 4, 1, 1, 4],[1, 3, 3, 2, 3, 3, 4, 1, 1],[1, 2, 4, 4, 4, 3, 1, 4, 3],[4, 4, 4, 4, 2, 2, 3, 4, 2],[4, 2, 4, 3, 2, 1, 3, 4, 2],[1, 3, 4, 2, 2, 2, 2, 2, 2]]
color = ["green", "blue", "yellow", "red"]

class DragManager():
    start_x, start_y = 0,0
    dragged = None

    def __init__(self,widget):
        self.widget = widget
        self.add_dragable(self.widget)
    
    def add_dragable(self, widget):
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.on_start)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_drop)
        self.widget["cursor"] = "hand1"
    
    def on_start(self, event):
        DragManager.start_x, DragManager.start_y = event.widget.winfo_pointerxy() 
        dragged_item = event.widget.find_withtag("current")
        DragManager.dragged = event.widget.itemcget(dragged_item, "fill")
        DragManager.dragged = (event.widget, dragged_item)
        pprint.pprint(g)

    def on_drag(self, event):
        dx = event.widget.winfo_pointerx() - DragManager.start_x
        dy = event.widget.winfo_pointery() - DragManager.start_y
        if dx < -50 or dx < 50 or dy < -50 or dy > 50 :
            print("here")
            window.event_generate('<Motion>', warp=True, x=event.widget.winfo_pointerx(), y=event.widget.winfo_pointery())

    def on_drop(self, event):
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        candy = widget.find_withtag("candy")
        dropped_color = widget.itemcget(candy[0], 'fill')
        dragged_color = DragManager.dragged[0].itemcget(DragManager.dragged[1], "fill")
        widget.itemconfig(candy[0], fill=dragged_color)
        DragManager.dragged[0].itemconfig(DragManager.dragged[1], fill=dropped_color)
        g[(int(re.findall(r'\d+', str(widget))[0])-1 )//9][(int(re.findall(r'\d+', str(widget))[0])-1 )%9] = color.index(dragged_color) + 1
        g[(int(re.findall(r'\d+', str(DragManager.dragged[0]))[0])-1 )//9][(int(re.findall(r'\d+', str(DragManager.dragged[0]))[0])-1 )%9] = color.index(dropped_color) + 1
        pprint.pprint(g)
 
class Gui:
    def __init__(self, window, size, grid):
        # Intensive grid generation here
        for i in range(size):
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=75)

            for j in range(size):
                frame = tk.Canvas(master=window,relief=tk.RAISED,borderwidth=0,width=110,height=110)
                a = DragManager(frame)
                frame.grid(row=i, column=j, padx=5, pady=5)
                c = frame.create_oval(0,0,55,55, fill=color[grid[i][j]-1], tags="candy")

gui = Gui(window, 9, g)
window.mainloop()
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()

