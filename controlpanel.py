import tkinter as tk
from tkinter import ttk
import tkinter.font as TkFont
import json
from datahandler import DataHandler

class ControlPanel(ttk.Frame):
    def __init__(self, parent, tag,width,height):
        tk.Frame.__init__(self, parent,width=width, height=height,background="white")
        
        self.width=width
        self.height=height
        self.parent=parent

        self.custom_inputs=[]
        self.input_frames=[]
        # self.columnconfigure(30,minsize=100)
        with open('model_registry.json', 'r') as file:
            self.models_json=json.load(file)
            self.models=self.create_strings_from_json(self.models_json)
        with open("dataset_registry.json", 'r') as file:
            self.datasets_json=json.load(file)
            self.datasets=self.create_strings_from_json(self.datasets_json)

        

        self.create_input_comps()
        ttk.Frame(self).grid(row=1,column=0)
        self.create_input_selection()




    def create_strings_from_json(self,json_dict):
        str_val=[]
        for key in json_dict.keys():
            str_val.append(key+"--"+json_dict[key]["path"])
        return str_val

    
    def create_input_comps(self):
        def combox_event(eventObject):
            self.create_input_selection()
            self.parent.notify_new_dataset()
        parent=ttk.Frame(self)
        parent.grid(row=0,column=0,sticky="W")
        start=0
        input_box_colspan=5
        self.model_options=ttk.Combobox(parent,value=self.models,width=len(max(self.models,key=len)), state='readonly')       
        self.model_options.grid(row=0,column=start,columnspan=input_box_colspan)
        start+=input_box_colspan+1
        model_add=ttk.Button(parent,text="Add Model")
        model_add.grid(row=0,column=start)
        start+=1
        self.data_options=ttk.Combobox(parent,values=self.datasets,width=len(max(self.datasets,key=len)), state='readonly')
        self.data_options.current(0)
        self.data_options.grid(row=0,column=start,columnspan=input_box_colspan)
        self.data_options.bind("<<ComboboxSelected>>", combox_event)
        data_add=ttk.Button(parent,text="Add Dataset")
        start+=input_box_colspan+1
        data_add.grid(row=0,column=start)
    
        

    
    def create_input_selection(self):
        self.custom_inputs=[]
        parent=ttk.Frame(self)
        parent.grid(row=1,column=0)
        for frame in self.input_frames:
            frame.grid_forget()
            frame.destroy()
        self.input_frames=[]    
        name,path=str(self.data_options.get()).split("--")
        columns=DataHandler.return_columns(path)
        i=0
        for val in columns:
            frame=ttk.Frame(parent,width=len(str.strip(val))*7,height="40")
            frame.grid(row=2,column=i)
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)
            frame.grid_propagate(False)
            self.input_frames.append(frame)
            # frame=ttk.Frame(self)
            # frame.grid(row=2,column=i)

            i+=1
            if val !=self.datasets_json[name]["label"]:
                self.create_column_sections(frame,val)
        frame=ttk.Frame(parent,width=len(self.datasets_json[name]["label"])*7,height="40")
        frame.grid(row=2,column=i-1)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.grid_propagate(False)
        self.input_frames.append(frame)   
        self.create_column_sections(frame,self.datasets_json[name]["label"],True) 

        self.predict_custom=ttk.Button(parent,text="Predict")
        self.predict_custom.grid(row=2,column=i) 


    def create_column_sections(self,parent,value,isitLabel=False):
        ttk.Label(parent,text=value).grid(row=0,column=0)
        if isitLabel==False:
            inputbox=ttk.Entry(parent)
            inputbox.grid(row=1,column=0)
            self.custom_inputs.append(inputbox)
        else:
            inputbox=ttk.Entry(parent,state=False)
            inputbox.config(state="disabled")
            inputbox.grid(row=1,column=0)
            self.custom_inputs.append(inputbox)

    def get_selected_dataset(self):
        return self.data_options.get()
    
    def get_selected_model(self):
        return self.model_options.get()
    def update_custom_input(self,row):
        
        for box,val in zip(self.custom_inputs,row):
            box.delete(0, 'end')
            box.insert(0,val)

        self.custom_inputs[-1].configure(state="enabled")
        self.custom_inputs[-1].delete(0, 'end')
        self.custom_inputs[-1].insert(0,val)
        self.custom_inputs[-1].configure(state="disabled")
        
    

        

             
       