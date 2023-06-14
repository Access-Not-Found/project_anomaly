#IMPORTS
import pandas as pd
import env
from sqlalchemy import text, create_engine

import os
import pandas as pd
from sqlalchemy import create_engine, text

print(f'Imports Successful')

# FUNCTIONS

# -------------------------------------------------------------------- ACQUIRE --------------------------------------------------------------------
def get_logs(directory, filename):
    """
    Retrieves logs data from the specified database table and saves it as a CSV file.

    Args:
        directory (str): The directory path where the CSV file will be saved.
        filename (str): The name of the CSV file.

    Returns:
        pandas.DataFrame: The logs data as a pandas DataFrame.

    """

    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename,index_col=0)
        return df
    else:
        url = env.get_db_url('curriculum_logs')
        conn = create_engine(url).connect()
        query = text("""SELECT * FROM curriculum_logs.cohorts as c
                        JOIN curriculum_logs.logs as l ON c.id=l.user_id;""")
        df = pd.read_sql(query, conn)
        df.to_csv(directory + filename,index_col=0)
        return df

def get_connection(db):
    """This function creates the url used to check if file exists in the local directory
    ---
    Format: url = function()
    """
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def check_file_exists(fn, query, url):
    """
    check if file exists in my local directory, if not, pull from sql db, save as csv and
    return dataframe
    """
    if os.path.isfile(fn):
        print('csv file found and loaded')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df
    
# -------------------------------------------------------------------- PREPARE --------------------------------------------------------------------
def prep_logs(df):
    """
    Preprocesses the given DataFrame by combining 'date' and 'time' columns into 'access_date',
    dropping unnecessary columns, renaming columns, converting date and time columns to datetime,
    mapping program IDs to program names, and filling null cohort IDs based on cohort names.
    """
    df['access_date'] = df.apply(lambda row: str(row['date']) + ' ' + str(row['time']), axis=1)
    df = df.drop(columns={ 'id', 'slack', 'deleted_at', 'date', 'time'})
    df = df.rename(columns={'name': 'cohort', 'created_at': 'created', 'updated_at': 'updated'})
    df['start_date'] = df['start_date'].astype('datetime64')
    df['end_date'] = df['end_date'].astype('datetime64')
    df['created'] = df['created'].astype('datetime64')
    df['updated'] = df['updated'].astype('datetime64')
    df['access_date'] = df['access_date'].astype('datetime64')
    df['program'] = df['program_id'].map({1: 'data science', 2: 'web dev', 3: 'web dev', 4: 'web dev'})
    cohort_id_mapping = {'Bash': 2, 'Darden': 3, 'Florence': 4, 'Hyperion': 5, 'Jupiter': 6}
    df['cohort_id'].fillna(df['cohort'].map(cohort_id_mapping), inplace=True)
    
    return df

