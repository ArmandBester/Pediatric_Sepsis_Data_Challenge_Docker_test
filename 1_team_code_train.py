#!/usr/bin/env python

from helper_code import *
import numpy as np, os, sys
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
import joblib



# Train your model.
def train_challenge_model(path_to_training_data, model_folder):
    # Generate dummies and store the column names for consistency
    patient_ids, data, label, features = load_challenge_data(path_to_training_data)
    data = pd.get_dummies(data)
    columns = data.columns

    # Save the column names for later use during inference
    with open(os.path.join(model_folder, 'columns.txt'), 'w') as f:
        f.write("\n".join(columns))
        
    # Define parameters for random forest classifier and regressor.
    n_estimators   = 123  # Number of trees in the forest.
    max_leaf_nodes = 456  # Maximum number of leaf nodes in each tree.
    random_state   = 789  # Random state; set for reproducibility.

    # Impute any missing features; use the mean value by default.
    imputer = SimpleImputer().fit(data)

    # Train the models.
    data_imputed = imputer.transform(data)
    prediction_model = RandomForestClassifier(
        n_estimators=n_estimators, max_leaf_nodes=max_leaf_nodes, random_state=random_state
        ).fit(data_imputed, label)

    # Save the models.
    save_challenge_model(model_folder, imputer, prediction_model)

    print('Done! training model')
        

# Save your trained model.
def save_challenge_model(model_folder, imputer, prediction_model):
    d = {'imputer': imputer, 'prediction_model': prediction_model}
    filename = os.path.join(model_folder, 'model.sav')
    joblib.dump(d, filename, protocol=0)


## If required run all the functions
train_challenge_model(path_to_training_data="training_data/SyntheticData_Training.csv", model_folder="model")

