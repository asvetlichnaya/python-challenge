import pandas as pd
from datetime import datetime, timedelta

from pandas import DataFrame


def get_filtered_df(emp_df: DataFrame, n: int) -> DataFrame:
    emp_df['Date of employment'] = pd.to_datetime(emp_df['Date of employment'])

    current_date = datetime.now()
    n_years_ago = current_date - timedelta(days=365 * n)

    print('Date of ', n, ' years ago:', n_years_ago)
    # In compensation list calculate duration of employment in years * 1000
    compensation = []
    for i in range(len(emp_df)):
        compensation.append(int((current_date - emp_df.loc[i, 'Date of employment']).days/365)*1000)
    # Add 'Compensation' column to dataframe
    emp_df['Compensation'] = compensation
    # Filter employees who work more than n years
    emp_df = emp_df[emp_df['Date of employment'] <= n_years_ago]

    return emp_df.loc[:, ['Name', 'Compensation']]


df = pd.read_csv('input_files/6_input.csv')
print(get_filtered_df(df, 5))
