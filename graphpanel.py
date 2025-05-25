import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont

class GraphPanel(ttk.Frame):
    def __init__(self, parent, tag,width,height):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        
        self.width=width
        self.height=height
        self.parent=parent

        # frame=ttk.Frame(self,width=width,height=height)
        # frame.grid(row=0,column=0,sticky="NSE")
        # self.predict_all=ttk.Button(frame,text="Predict All",command=self.predict_all)
        # self.predict_all.pack()

    def predict_all(self):
        return
             
       