import pandas as pd
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,LSTM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
import joblib


import os
import pickle
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf

# Replace with your model's path
model_path = 'models/picklemodel2.pkl'

try:
    # Load the model
    model =pickle.load(open(model_path,'rb'))
    
    # Check if the model is loaded by printing the model summary
    model.summary()
    
    print("Model is loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
