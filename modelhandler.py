import tensorflow as tf
import pickle as pkl
import numpy as np
import json
class Model:
    @staticmethod
    def load_model(path):
        if "keras" in path:
            model=tf.keras.models.load_model(path)
            
            def predict_keras(input_vec):
                    
                    pred=model.predict(input_vec,batch_size=1024)
                    return list(map(lambda x: int(x[0][0]),(pred>=0.5)))
            
            return predict_keras
        else:
            with open(path,"rb") as fp:
                model=pkl.load(fp)
                def predict_ski(input_vec):
                    vec=np.array(input_vec)
                    return model.predict(vec)
                     
                return predict_ski
     
            

# inp_vect={"age":np.array([0.0]),"language":np.array([1.0]),"network":np.array([2.0]),"bytesperduration":np.array([0.916233]),
#           "bytes":np.array([0.002233]),"returned":np.array([1.0])}

# model=Model.load_model("models/mlp.keras")
# print(model(inp_vect))