import matplotlib.pyplot as plt
import pandas as pd
from src.data_import import load_data
from src.analysis import high_use_days


def useage_and_temp(df: pd.DataFrame) -> plt.Figure:
    """ Graphs daily usage and temp

    This function takes the daily usage dataframe 
    and graphs it over time. Additional axis to 
    show the daily high temperature. Includes add
    itional functionality to assign colors to 
    differentiate weekdays and weekend. 


    Args: 
        df: A data frame (usage specific to the daily 
            usage data)


    Returns: 
        fig: Returns a matplotlib figure 
    """
    # create a list that assignes colors for the weekdays/weekends for Day of Week
    colors = ['red' if day in ['Saturday', 'Sunday']
              else 'blue' for day in df['Day of week']]
    # initate figure and axis for plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df['Usage date'], df['Total cost'],
           edgecolor=colors, color='steelblue', label='Total Cost')
    # create a secondary axis on the same figure for the temperature
    ax1 = ax.twinx()
    ax1.plot(df['Usage date'], df['High temperature (F)'],
             'k', ls='dotted', label='High temperature')
    ax.set_xlabel('Usage date')
    ax.set_ylabel('Cost $')
    # ax.set_ylim(0,8)
    ax1.set_ylabel('Temperature')
    ax1.set_ylim(20, 120)
    ax.legend()
    ax1.legend()
    return fig


def high_use_groups(df: pd.DataFrame) -> plt.Figure:
    """ Graphs count of high use days

    This function imports analysis from the analysis file
    that counts the number of times a day of the week has
    above average energy use. This is intended to show what
    days are generally high usage days. The function will
    take the daily use dataframe as the argumet, pass that
    through a function from analysis to obtain a series 
    with the counts of days, the graph that series. 

    Arg: 
        df: The daily usage data frame. 

    Returns: 
        fig: Bar graph of the counts
    """
    high_use = high_use_days(df)
    fig, ax = plt.subplots()
    high_use.plot(kind='bar', title='Number of times above average usage')
    return fig


def main():
    daily_df, hourly_df = load_data()
    usage_graph = useage_and_temp(daily_df)
    usage_graph.savefig("usage_vs_temp.png", dpi=300)  # save figure
    plt.show()
    graphed_days = high_use_groups(daily_df)
    graphed_days.savefig("graph_of_high_use_days.png")
    plt.show()


if __name__ == "__main__":
    main()
