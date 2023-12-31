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
def get_logs(filename):
    """
    Retrieves logs data from the specified database table and saves it as a CSV file.
"""
    directory = os.getcwd() + "/"  # Use the current working directory as the directory path

    if os.path.exists(directory + filename):
        df = pd.read_csv(directory + filename, index_col=0)
        return df
    else:
        url = env.get_db_url('curriculum_logs')
        conn = create_engine(url).connect()
        query = text("""SELECT * FROM curriculum_logs.logs as l
                        JOIN curriculum_logs.cohorts as c ON c.id=l.cohort_id;""")
        df = pd.read_sql(query, conn)
        df.to_csv(directory + filename, index_col=0)
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
    # checks if the file exists, else creates the csv
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
    """
    # basic column dropping and renaming
    df['access_date'] = df.apply(lambda row: str(row['date']) + ' ' + str(row['time']), axis=1)
    df = df.drop(columns={ 'id', 'slack', 'deleted_at', 'date', 'time'})
    df = df.rename(columns={'name': 'cohort', 'created_at': 'created', 'updated_at': 'updated'})
    
    # changed datatypes
    df['start_date'] = df['start_date'].astype('datetime64')
    df['end_date'] = df['end_date'].astype('datetime64')
    df['created'] = df['created'].astype('datetime64')
    df['updated'] = df['updated'].astype('datetime64')
    df['access_date'] = df['access_date'].astype('datetime64')
    
    # mapped null cohort_ids with selected numbers (no ranking)
    df['program'] = df['program_id'].map({1: 'web dev', 2: 'web dev', 3: 'data science', 4: 'frontend'})
    df['cohort_id'] = df['cohort_id'].astype(int)
    
    # grabs the lesson from path
    df['lesson'] = df['path'].str.split('/').str[-2]
    
    # grabs the endpoint from the lesson
    df['endpoint'] = df['path'].str.split('/').str[-1]
    
    return df