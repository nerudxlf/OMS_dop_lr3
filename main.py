import pandas as pd
import numpy as np


def main():
    data = pd.read_csv('time_series_covid19_recovered_global.csv')
    russia_data = data.values[195][4:]
    ukr_data = data.values[231][4:]

    mean_rus = np.mean(russia_data)
    median_rus = np.median(russia_data) 
    min_rus = min(russia_data)
    max_rus = max(russia_data)

    mean_ukr = np.mean(ukr_data)
    median_ukr = np.median(ukr_data)
    min_ukr = min(ukr_data)
    max_ukr = max(ukr_data)
    



if __name__ == '__main__':
    main()