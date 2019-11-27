#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:38:33 2017

@author: josef
"""
import random, sys
if sys.version_info.major < 3:
    import Tkinter as tk
else:
    import tkinter as tk

COLORS = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'WHITE']


def get_random_colors(count):
    return [random.choice(COLORS) for _ in range(count)]


class ColoredCircles(tk.Canvas):
    """Zeichnet die Kreise in den 4 Ecken"""

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, width=400, height=400)
        self.color_changer_id = None
        self.verwendete_farben = list()
        self.kreis_ids = [
            self.zeichne_kreis(x, y, 70)
            for x, y in [(10, 10), (320, 10), (10, 320), (320, 320)]
        ]
        self.aendere_farben()
        self.winfo_toplevel().bind('<Key>', self.on_key)

    def zeichne_kreis(self, x, y, size):
        return self.create_oval(x, y, x + size, y + size, width=0)

    def aendere_farben(self):
        if self.color_changer_id is not None:
            print('Farbwechsel wegen Zeitueberschreitung.')
            if 'RED' in self.verwendete_farben:
                print('Richtige Farbe aber kein Tastendruck.')
        self.verwendete_farben = get_random_colors(len(self.kreis_ids))
        for kreis_id, farbe in zip(self.kreis_ids, self.verwendete_farben):
            self.itemconfig(kreis_id, fill=farbe)
        self.color_changer_id = self.after(5000, self.aendere_farben)

    def on_key(self, event):
        if 'RED' in self.verwendete_farben:
            if event.keysym in ['Return', 's', 'a']:
                print('Richtige Farbe und Taste.')
                self.after_cancel(self.color_changer_id)
                self.color_changer_id = None
                self.aendere_farben()
        else:
            print('Falsche Farbe')


def main():
    root = tk.Tk()
    root.title('Test Farbige Kreise')
    colored_circles = ColoredCircles(root)
    colored_circles.pack(side=tk.TOP)
    root.mainloop()


if __name__ == '__main__':
    main()