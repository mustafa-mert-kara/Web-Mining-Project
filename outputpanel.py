import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
from datahandler import DataHandler

from random import choice

class OutputPanel(ttk.Frame):
    def __init__(self, parent, tag,width,height):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        
        self.width=width

        self.height=height
        self.parent=parent
        
        self.create_data_view()


    def create_data_view(self):
        dataset=self.parent.get_selected_dataset()
        _,path=dataset.split("--")
        columns=DataHandler.return_columns(path=path)
        self.table = ttk.Treeview(self, columns = list(columns), show = 'headings')
        for col in columns:
            self.table.heading(col, text = col)
            self.table.column(col, minwidth=0, width=len(str.strip(col))*7, stretch=False)
        
        
        self.verscrlbar = ttk.Scrollbar(self, 
                           orient ="vertical", 
                           command = self.table.yview)
        
        self.table.configure(yscrollcommand= self.verscrlbar.set)

        self.table.pack(side ='left',expand=True, fill='y')

        self.verscrlbar.pack(side ='right', fill ='y',expand=True)
        

        dataset=DataHandler.import_data(path)

        for _,row in dataset.iterrows():
            self.table.insert("","end",values=list(row))

        def item_select(_):
            self.parent.update_custom_input(self.table.item(self.table.selection())['values'])
            
        self.table.bind('<<TreeviewSelect>>', item_select)
        
    def destroy_table(self):
        self.table.delete(*self.table.get_children())
        self.table.update()
        self.table.destroy()
        self.verscrlbar.destroy()

             
    def new_dataset(self):
        self.destroy_table()
        self.create_data_view()
        