#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    File name: model.py
    Author: Satwik Gawand
    Date Created: 18/1/2021
    Date Last Modified: 18/1/2021
    Python Version: 3.8.6
'''

# Imports
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier

# Data
penguins = pd.read_csv('penguins_cleaned.csv')

# Ordinal Feature Encoding
df = penguins.copy()
target = 'species'
encode = ['sex', 'island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

def['species'] = df['species'].apply(target_encode)

# Separate params and target
x = df.drop('species', axis=1)
y = df['species']

# Build the Classifier
classifier = RandomForestClassifier()
classifier.fit(x, y)

# Save the Model
pickle.dump(classifier, open('penguins_classifier.pkl', 'wb'))