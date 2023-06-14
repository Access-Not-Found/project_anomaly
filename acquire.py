#IMPORTS
import pandas as pd
import env
from sqlalchemy import text, create_engine

import os
import pandas as pd
from sqlalchemy import create_engine, text


# FUNCTIONS



#acquire data
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
        df = pd.read_csv(directory + filename)
        return df
    else:
        url = env.get_db_url('curriculum_logs')
        conn = create_engine(url).connect()
        query = text("""SELECT * FROM curriculum_logs.cohorts as c
                        JOIN curriculum_logs.logs as l ON c.id=l.user_id;""")
        df = pd.read_sql(query, conn)
        df.to_csv(directory + filename)
        return df
