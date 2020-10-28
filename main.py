import pandas as pd


def main():
    data = pd.read_csv('time_series_covid19_recovered_global.csv')
    print(data)


if __name__ == '__main__':
    main()