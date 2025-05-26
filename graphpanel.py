import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import ConfusionMatrixDisplay

class GraphPanel(tk.Tk):
    def __init__(self, values,width=1200,height=500,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(f"{width}x{height}")
        self.width=width
        self.height=height        

# setting the title 
        self.title(f"Plotting {values["model"]} Results")

        self.table = ttk.Treeview(self, columns = ["Metric","Score"], show = 'headings')
        for col in ["Metric","Score"]:
            self.table.heading(col, text = col)
            self.table.column(col, minwidth=0, width=90, stretch=False)
               

        self.table.pack(side ='left',expand=False, fill='y')        

        

        
        self.table.insert("","end",values=["Accuracy",values["acc"]])
        self.table.insert("","end",values=["F1-Score",values["f1"]])
        self.table.insert("","end",values=["Roc-Auc Score",values["roc"]])



        self.fig, axes = plt.subplots(1,2)

        plt.subplots_adjust(wspace=0.267)

    # adding the subplot
        
        disp = ConfusionMatrixDisplay(confusion_matrix=values["cm"], display_labels=["No Sale","Sale"])
        disp.plot(ax=axes[0])
        values["roc_curve"].plot(ax=axes[1])
        canvas = FigureCanvasTkAgg(self.fig,
                               master = self)  
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack(fill ='both',expand=True)

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                    self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack(fill ='both',expand=True)

        

    
    def redraw(self, delay=1000):
        
        self.after(delay, lambda: self.redraw(delay))

    def wait_for_close(self):
        self.is_running=True
        while self.is_running:
            self.redraw()
    def close(self):
        self.is_running=False