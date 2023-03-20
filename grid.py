import tkinter as tk
import random

window = tk.Tk()
g = [[3, 1, 2, 4, 3, 4, 2, 4, 1],[1, 2, 2, 1, 3, 3, 3, 3, 2],[1, 3, 2, 3, 4, 1, 1, 3, 4],[2, 3, 1, 2, 3, 4, 1, 1, 4],[1, 3, 3, 2, 3, 3, 4, 1, 1],[1, 2, 4, 4, 4, 3, 1, 4, 3],[4, 4, 4, 4, 2, 2, 3, 4, 2],[4, 2, 4, 3, 2, 1, 3, 4, 2],[1, 3, 4, 2, 2, 2, 2, 2, 2]]

class DragManager():
    listeDrop = []
    start_x, start_y = 0,0
    dragged = 0

    def __init__(self,widget,drag=True,drop=True):
        self.widget = widget
        self.drag = drag
        self.drop = drop
        if drag:
            self.add_dragable(self.widget)
        if drop:
            DragManager.listeDrop.append(self.widget)
    
    def add_dragable(self, widget):
        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.on_start)
        self.widget.bind("<B1-Motion>", self.on_drag)
        self.widget.bind("<ButtonRelease-1>", self.on_drop)
        self.widget["cursor"] = "hand1"
    
    def on_start(self, event):
        DragManager.start_x = event.x
        DragManager.start_y = event.y
        DragManager.dragged = event.widget.winfo_containing(event.x, event.y).cget("background")
        print("arrraaa", event, DragManager.start_x, DragManager.start_y)

    def on_drag(self, event):
        dx = DragManager.start_x - event.x
        dy = DragManager.start_y - event.y
        print("ara", event, dx, dy)
    
    def on_drop(self, event):
        # commencons par trouver le widget sous le curseur de la souris
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        if target in DragManager.listeDrop:
            print(target.cget("background"), DragManager.dragged)


class Gui:
    def __init__(self, window, size, grid):
        color = ["green", "blue", "yellow", "red"]
        # Intensive grid generation here

        for i in range(size):
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=75)

            for j in range(size):
                frame = tk.Canvas(master=window,relief=tk.RAISED,borderwidth=0,width=110,height=110)
                a = DragManager(frame, drag=True, drop=True)
                frame.grid(row=i, column=j, padx=5, pady=5)
                c = frame.create_oval(0,0,55,55, fill=color[grid[i][j]-1])

gui = Gui(window, 9, g)
window.mainloop()
