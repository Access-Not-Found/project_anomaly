# IMPORTS
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os
import itertools
import wrangle as w

# DBSCAN import
from sklearn.cluster import DBSCAN

# Scaler import
from sklearn.preprocessing import MinMaxScaler

#FUNCTIONS


def detect_outliers(observed_counts):
    """
    Detect outliers using DBSCAN clustering algorithm on normalized observed counts.
        observed_counts (pandas.DataFrame): DataFrame containing observed counts
            with 'lesson' and 'cohort' as columns.
            Returns:
        outliers (pandas.DataFrame): DataFrame containing outliers identified by DBSCAN.
        non_outliers (pandas.DataFrame): DataFrame containing non-outliers identified by DBSCAN.
    """
    observed_counts=observed_counts.iloc[1:].sort_values(by='lesson',ascending=False)
    

    scaler = MinMaxScaler()
    normalized_counts = scaler.fit_transform(observed_counts)

    dbscan = DBSCAN(eps=0.5, min_samples=5)
    outlier_labels = dbscan.fit_predict(normalized_counts)

    outliers = observed_counts[outlier_labels == -1]
    non_outliers = observed_counts[outlier_labels == 0]

    return outliers, non_outliers