import pandas as pd
import numpy as np


class DataHandler():
    @staticmethod
    def import_data(path:str,nrows=None):
        file_type=path.split(".")[1]
        match file_type:
            case "csv":
                return pd.read_csv(path,nrows=nrows)
            case "xlsx":
                return pd.read_excel(path,nrows=nrows)
            case "xls":
                return pd.read_excel(path,nrows=nrows)
            case "json":
                return pd.read_json(path,nrows=nrows)
            
    @staticmethod
    def return_columns(path):
        dataset=DataHandler.import_data(path,1)
        return dataset.columns