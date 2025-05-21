import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont

class GraphPanel(ttk.Frame):
    def __init__(self, parent, tag,width,height):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        
        self.width=width
        self.height=height
        self.parent=parent

             
       