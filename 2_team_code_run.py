#!/usr/bin/env python

from helper_code import *
import numpy as np, os, sys
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_challenge_model(model_folder):
    print('Loading the model...')
    
    # Load the saved column names
    with open(os.path.join(model_folder, 'columns.txt'), 'r') as f:
        columns = f.read().splitlines()

    model = joblib.load(os.path.join(model_folder, 'model.sav'))
    model['columns'] = columns
    return model

def run_challenge_model(model_folder, path_to_test_data):
    model = load_challenge_model(f'{model_folder}')
    imputer = model['imputer']
    prediction_model = model['prediction_model']
    columns = model['columns']

    # Load data.
    patient_ids, data, label, features = load_challenge_data(path_to_test_data)
    
    data = pd.get_dummies(data)

    # Align test data with training columns, filling missing columns with 0
    data = data.reindex(columns=columns, fill_value=0)
    
    # Impute missing data.
    data_imputed = imputer.transform(data)

    # Apply model to data.
    prediction_binary = prediction_model.predict(data_imputed)[:]
    prediction_probability = prediction_model.predict_proba(data_imputed)[:, 1]
    
    results =  {"PatientID": patient_ids, 
                "PredictedProbability": prediction_probability,
                "PredictedBinary": prediction_binary
                }
    resultsDf = pd.DataFrame.from_dict(results)

    print(resultsDf.head())

    resultsDf.to_csv("test_outputs/outputs.txt", sep="|")


run_challenge_model(model_folder="model", path_to_test_data="test_data/test_data.csv")