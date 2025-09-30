import pandas as pd
from src.data_import import load_data
from typing import cast


"""
    moved this logic into the data_import file, testing the output to make sure the new imported function works as expected. 

def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    daily_df = daily_data(
        '~/Documents/python_projects/finance/srp/data/dailyCost7_14_2025_to_9_26_2025.csv')
    hourly_df = hourly_data(
        '~/Documents/python_projects/finance/srp/data/hourlyCost7_14_2025_to_9_26_2025.csv')
    return daily_df, hourly_df
"""


def get_stats(df: pd.DataFrame) -> pd.Series:
    """Creates a pd series that contains the statistics of a datafram

    This function takes the daily cost dataframe, calculates the agg mean, max, min, and std of the total cost column. Returns a pd series with these statistics. 

    Args: 
        df (pd.DataFrame): dataframe containing cost data

    Returns: 
        stats (pd.Series): series with statistics
    """
    stats = df['Total cost'].agg(['mean', 'max', 'min', 'std'])
    return cast(pd.Series, stats)


def above_average_days(
        df: pd.DataFrame,
        stats: pd.Series) -> pd.DataFrame:
    """ Create dataframe containing all days where energy use is above avg

    Uses the statistics of a dataframe to generate a new dataframe that
    contains all days that are obove the average energy use. This will 
    return all days where the the total cost is above the mean. 

    Args: 
        df (pd.DataFrame): daily cost dataframe

    Returns: 
        above_average (pd.DataFrame): above average dataframe
    """

    above_average = df[df['Total cost'].ge(stats['mean'])]
    return cast(pd.DataFrame, above_average)


def grouped_above_days(above_average: pd.DataFrame):
    """ 
    Creates a new dataframe that is catogorized and groupled by days of
        the week based on the days above average
    """
    day_groups = above_average.groupby(
        'Day of week')['Day of week'].value_counts(
    )
    # create new index to sort the days of week chronologically
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday",
                  "Friday", "Saturday", "Sunday"]
    day_groups.index = pd.CategoricalIndex(
        day_groups.index, categories=days_order, ordered=True)
    day_groups = day_groups.sort_index()
    return day_groups


def high_use_days(daily: pd.DataFrame) -> pd.Series:
    """
        Wrapper that requires only the input of a daily
        data frame to generate a series of grouped days
    """
    stats = get_stats(daily)
    above_average = above_average_days(daily, stats)
    day_groups = grouped_above_days(above_average)
    return day_groups


def maximum_usage_date(
        daily_df: pd.DataFrame,
        hourly_df: pd.DataFrame
) -> pd.DataFrame:
    max_date = daily_df.loc[daily_df['Total cost'].idxmax(), 'Usage date']
    max_day = hourly_df.loc[hourly_df['Usage date'] == max_date, :]
    return max_day


def main():
    daily, hourly = load_data()
    stats = get_stats(daily)
    above_avg = above_average_days(daily, stats)
    grouped = grouped_above_days(above_avg)
    max_date = maximum_usage_date(daily, hourly)
    print(stats)
    print(grouped)
    print(max_date)


if __name__ == "__main__":
    main()
