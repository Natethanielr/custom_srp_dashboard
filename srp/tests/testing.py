from src.data_import import daily_data, hourly_data


def main():
    df = daily_data(
        '~/Documents/python_projects/finance/srp/data/dailyCost7_14_2025_to_9_26_2025.csv')
    print(df.head())
    df1 = hourly_data(
        '~/Documents/python_projects/finance/srp/data/hourlyCost7_14_2025_to_9_26_2025.csv')
    print(df1.head())


if __name__ == '__main__':
    main()
