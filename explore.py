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

def plot_one(df):
    '''This function plots question one findings'''
    data_series = df[(df['program'] == 'data science') & (df['cohort'] != 'Staff')&(df['lesson']!='')].lesson.value_counts().head(5)
    web_dev_series = df[(df['program'] == 'web dev') & (df['cohort'] != 'Staff')&(df['lesson']!='')].lesson.value_counts().head(5)    
    front_series = df[(df['program'] == 'frontend') & (df['cohort'] != 'Staff')&(df['lesson']!='')].lesson.value_counts().head(7)[2:6]
    
    plt.subplot(221)
    data_series.plot(kind='bar')
    plt.title('Most Visited Lessons for Data Science Program')
    plt.xticks(rotation=45)
    plt.show()

    plt.subplot(222)
    web_dev_series.plot(kind='bar')
    plt.title('Most Visited Lessons for Web Dev Program')
    plt.xticks(rotation=45)
    plt.show()

    plt.subplot(223)
    front_series.plot(kind='bar')
    plt.title('Most Visited Lessons for Frontend Program')
    plt.xticks(rotation=45)
    plt.show()
    
def plot_one_pings(df):
    '''This functions plots the findings to question one per cohort'''
    # creates the variables
    data_fundies_cohort = df[(df['lesson'] == 'classification') & (df['program'] == 'data science') & (df['cohort'] != 'Staff')].cohort.value_counts().head(5)
    web_java_cohort = df[(df['lesson'] == 'javascript-i') & (df['program'] == 'web dev')  & (df['cohort'] != 'Staff')].cohort.value_counts().head(5)
    front_images_cohort = df[(df['lesson'] == 'html-css') & (df['program'] == 'frontend') & (df['cohort'] != 'Staff')].cohort.value_counts()

    # plots
    plt.subplot(311)
    data_fundies_cohort.plot(kind='bar')
    plt.title('Classification Pings per Data Science Cohort')
    plt.xticks(rotation=45)
    
    plt.subplot(312)
    web_java_cohort.plot(kind='bar')
    plt.title('Javascript-i Pings per Web Dev Cohort')
    plt.xticks(rotation=45)
    
    plt.subplot(313)
    front_images_cohort.plot(kind='bar')
    plt.title('HTML-CSS Pings per Frontend Cohort')
    plt.xticks(rotation=45)
    plt.subplots_adjust(left=0.1,
                bottom=0,
                right=0.9,
                top=1.5,
                wspace=0.6,
                hspace=0.6)
    plt.show()
    
def web_2018(df):
    """This function prints the sites accessed from web dev students in 2018"""
    # create the variables
    df_date = df.set_index('start_date')
    df_date = df_date.sort_index()
    df_date_2018 = df_date[df_date.index.year == 2018]   
    wd_2018 = df_date_2018[(df_date_2018.program == 'web dev')&(df_date_2018['cohort'] != 'Staff')&(df_date_2018['lesson'] != '')].endpoint.value_counts().tail(10)
    print(wd_2018)
    
def web_2019(df):
    """This function prints the sites accessed from web dev students in 2019"""
    # create the variables
    df_date = df.set_index('start_date')
    df_date = df_date.sort_index()
    df_date_2019 = df_date[df_date.index.year == 2019]   
    wd_2019 = df_date_2019[(df_date_2019.program == 'web dev')&(df_date_2019['cohort'] != 'Staff')&(df_date_2019['lesson'] != '')].endpoint.value_counts().tail(10)
    print(wd_2019)
    
def web_2020(df):
    """This function prints the sites accessed from web dev students in 2020"""
    # create the variables
    df_date = df.set_index('start_date')
    df_date = df_date.sort_index()
    df_date_2020 = df_date[df_date.index.year == 2018]   
    wd_2020 = df_date_2020[(df_date_2020.program == 'web dev')&(df_date_2020['cohort'] != 'Staff')&(df_date_2020['lesson'] != '')].endpoint.value_counts().tail(10)
    print(wd_2020)