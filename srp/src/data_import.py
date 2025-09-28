# Import libraries
import pandas as pd


def create_dataframe(filepath: str) -> pd.DataFrame:
    """
    Load and clean cost data sets

    ----------
    Steps:
    1. Read the csv into a dataframe
    2. If the last row is a total, drop that row
    3. Clean the 'Total cost' column and convert to float

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
    # convert the total cost to float, remove $
    df['Total cost'] = (
        df['Total cost']
        .replace({'\\$': '', ',': ''}, regex=True)
        .astype(float)
    )
    return df


def daily_data(filepath: str) -> pd.DataFrame:
    df = create_dataframe(filepath)
    # convert usage date to datetime
    df['Usage date'] = pd.to_datetime(df['Usage date'])
    # create a new column with the day of the week
    df['Day of week'] = df['Usage date'].dt.day_name()
    return df


def hourly_data(filepath: str) -> pd.DataFrame:
    """
    create wraper for hourly cost dataset
    The hourly cost dataset has an additional interval column.
    This creates a new colulmn Datetime that converst the interval to a datetime object 
    so it can be graphed
    """
    df = create_dataframe(filepath)
    df["Datetime"] = (pd.to_datetime(df["Usage date"] + " " + df["Interval"],
                                     format="%m/%d/%Y %I:%M %p"))
    # convert usage date to datetime
    df['Usage date'] = pd.to_datetime(df['Usage date'])
    # create a new column with the day of the week
    df['Day of week'] = df['Usage date'].dt.day_name()
    return df


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
        Specifies the file path for the csv file and loads them into the dataframes.
        Call this function to load the data into a file.
    """
    daily_df = daily_data(
        '~/Documents/python_projects/finance/srp/data/dailyCost7_14_2025_to_9_26_2025.csv')
    hourly_df = hourly_data(
        '~/Documents/python_projects/finance/srp/data/hourlyCost7_14_2025_to_9_26_2025.csv')
    return daily_df, hourly_df
