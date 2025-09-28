import numpy as np
import pandas as pd
from src.data_import import daily_data, hourly_data


def load_data() -> pd.DataFrame:
    daily_df = daily_data(
        '~/Documents/python_projects/finance/srp/data/dailyCost7_14_2025_to_9_26_2025.csv')
    hourly_df = hourly_data(
        '~/Documents/python_projects/finance/srp/data/hourlyCost7_14_2025_to_9_26_2025.csv')
    return daily_df, hourly_df


def get_stats(df: pd.DataFrame) -> pd.Series:
    """
    creates a pd series that contains the statistics of a datafram
    """
    stats = df['Total cost'].agg(['mean', 'max', 'min', 'std'])
    return stats


def above_average_days(
        df: pd.DataFrame,
        stats: pd.Series) -> pd.DataFrame:
    """
    Uses the statistics of a dataframe to generate a new dataframe that
        contains all days that are obove the average energy use
    """

    above_average = df[df['Total cost'].ge(stats['mean'])]
    return above_average


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


def main():
    daily, hourly = load_data()
    stats = get_stats(daily)
    above_avg = above_average_days(daily, stats)
    grouped = grouped_above_days(above_avg)
    print(stats)
    print(grouped)


if __name__ == "__main__":
    main()
