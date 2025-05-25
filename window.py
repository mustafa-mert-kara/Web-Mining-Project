import tkinter as tk

from tkinter import ttk
from datetime import datetime
from controlpanel import ControlPanel
from outputpanel import OutputPanel
from graphpanel import GraphPanel

class Window(tk.Tk):
    def __init__(self,width,height,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{width}x{height}")
        
        self.__window_width=width
        self.__window_height=height
        padding=tk.Frame(self,height=self.__window_height*0.02,width=self.__window_width*0.1)
        padding.grid(row=0,column=0,sticky = tk.W+tk.N)
        self.Control=ControlPanel(self,"ControlFrame",height=self.__window_height*0.2,width=self.__window_width*0.1)
        self.Control.grid(row=0,column=1,sticky = tk.W+tk.E+tk.N+tk.S)
        
        
        self.Graphs=GraphPanel(self,"GraphPanel",height=int(self.__window_height*0.9),width=self.__window_width*0.1)
        self.Graphs.grid(row=2,column=0,sticky = tk.W+tk.N+tk.S)
        
        self.Output=OutputPanel(self,"OutputPanel",height=int(self.__window_height*0.9),width=self.__window_width*0.02)
        self.Output.grid(row=2,column=1,sticky = tk.W+tk.N+tk.S)

        
        

        

    def redraw(self, delay=1000):
        
        self.after(delay, lambda: self.redraw(delay))

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    def close(self):
        self.is_running=False

    def get_selected_dataset(self):
        return self.Control.get_selected_dataset()
    def get_selected_model(self):
        return self.Control.get_selected_dataset()
    
    
    def notify_new_dataset(self):
        self.Output.new_dataset()
    
    def update_custom_input(self,row):
        self.Control.update_custom_input(row)
    




    
        
        



