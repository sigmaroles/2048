import numpy
import tkinter as tk
from tkinter import font


class Renderer:
    def __init__(self, update_delegate, size=4):
        self.update_delegate = update_delegate
        self.click_delegate = []

        # Initialize Tk and Canvas
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas.focus_set()
        self.canvas.update()

        self.size = size
        self.rectangles = numpy.zeros((self.size, self.size))
        self.texts = numpy.zeros((self.size, self.size))
        s = 100
        self.canvas.config(width=s * self.size, height=s * self.size)

        helv36 = font.Font(family='Helvetica', size=int(s / 4), weight='bold')
        for i in range(self.size):
            for j in range(self.size):
                r = self.canvas.create_rectangle(i * s, j * s, (i + 1) * s, (j + 1) * s, outline='', activefill='grey')
                t = self.canvas.create_text((i + 0.5) * s, (j + 0.5) * s, font=helv36)
                self.rectangles[i, j] = r
                self.texts[i, j] = t

        self.mainloop()
        self.window.mainloop()

    def mainloop(self):
        t = self.update_delegate()
        for i in range(self.size):
            for j in range(self.size):
                if t[i, j] == 0:
                    c = 'white'
                elif t[i, j] == 2:
                    c = '#eee4da'
                elif t[i, j] == 4:
                    c = '#ede0c8'
                elif t[i, j] == 8:
                    c = '#f2b179'
                elif t[i, j] == 16:
                    c = '#f59563'
                elif t[i, j] == 32:
                    c = '#f67c5f'
                elif t[i, j] == 64:
                    c = '#f65e3b'
                elif t[i, j] == 128:
                    c = '#edcf72'
                elif t[i, j] == 256:
                    c = '#edcc61'
                elif t[i, j] == 512:
                    c = '#edc850'
                elif t[i, j] == 1024:
                    c = '#edc53f'
                elif t[i, j] == 2048:
                    c = '#edc22e'
                else:
                    c = '#3c3a32'

                self.canvas.itemconfig(int(self.rectangles[i, j]), fill=c)
                self.canvas.itemconfig(int(self.texts[i, j]), text=str(t[i, j]))
        self.canvas.after(1, self.mainloop)
