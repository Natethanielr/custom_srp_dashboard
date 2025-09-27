# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def create_dataframe(filepath: str) -> pd.DataFrame:
    """
    Load and clean cost data sets

    ----------
    Steps:
    1. Read the csv into a dataframe
    2. If the last row is a total, drop that row
    3. Convert 'Usage date' to datetime.
    4. Clean the 'Total cost' column and convert to float
    5. Add a new column with weekday names

    Parameters
    ----------
    filepath: str
            Path to the CSV file

    Returns
    ----------
    pd.DataFrame
            The cleaned dataframe
    """
    # import csv
    df = pd.read_csv(filepath)
    # drop any columns where the usage date is Nan
    df = df.dropna(subset=['Usage date'])
    # convert usage date to datetime
    df['Usage date'] = pd.to_datetime(df['Usage date'])
    # convert the total cost to float, remove $
    df['Total cost'] = (
        df['Total cost']
        .replace({'\\$': '', ',': ''}, regex=True)
        .astype(float)
    )
    # create a new column with the day of the week
    df['Day of week'] = df['Usage date'].dt.day_name()
    # create a datetime column to sort hourly costs
    df['Datetime'] = pd.to_datetime(
        df['Usage date'] + " " + df['Interval'], format="%m/%d/%Y %I:%M %p")
    return df


"""
Testing below, file is unfinished
"""
if __name__ == "__main__":
    df = create_dataframe(
        'cost_data/dailyCost7_14_2025_to_9_26_2025.csv'
    )
    print(df.head())
