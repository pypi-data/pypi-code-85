import tkinter as tk
import sys


class MenuItem:

    def __init__(self, label, command=None):
        pass


class MenuBar(tk.Menu):

	def __init__(self, parent):
		tk.Menu.__init__(self, parent)

		fileMenu = tk.Menu(self, tearoff=False)
		self.add_cascade(label="File", underline=0, menu=fileMenu)
		fileMenu.add_command(label="Exit", underline=1, command = self.quit)

	def quit(self):
		sys.exit(0)


