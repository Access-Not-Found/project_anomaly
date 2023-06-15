# IMPORTS








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
   
    

    scaler = MinMaxScaler()
    normalized_counts = scaler.fit_transform(observed_counts_sorted)

    dbscan = DBSCAN(eps=0.5, min_samples=5)
    outlier_labels = dbscan.fit_predict(normalized_counts)

    outliers = observed_counts_sorted[outlier_labels == -1]
    non_outliers = observed_counts_sorted[outlier_labels == 0]

    return outliers, non_outliers