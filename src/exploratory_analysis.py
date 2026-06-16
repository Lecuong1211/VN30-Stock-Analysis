# ======================================
# exploratory_analysis.py
# EDA cho toàn bộ VN30
# ======================================

import os
import pandas as pd


VN30 = [
    'ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR',
    'HDB', 'HPG', 'MBB', 'MSN', 'MWG', 'PLX', 'SAB', 'SHB',
    'SSB', 'SSI', 'STB', 'TCB', 'TPB', 'VCB', 'VHM', 'VIB',
    'VIC', 'VJC', 'VNM', 'VPB', 'VRE', 'VIX'
]


def analyze_stocks(tickers):

    os.makedirs(
        'outputs',
        exist_ok=True
    )

    summary = []

    for ticker in tickers:

        print(f'\n===== {ticker} =====')

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            # ---------------------
            # Thông tin dataset
            # ---------------------

            print("\nINFO:")

            print(
                df.info()
            )

            # ---------------------
            # Missing Values
            # ---------------------

            print("\nMissing Values:")

            print(
                df.isnull().sum()
            )

            # ---------------------
            # Descriptive Statistics
            # ---------------------

            print("\nDescribe:")

            print(
                df.describe()
            )

            # ---------------------
            # Highest Price
            # ---------------------

            highest_price = (
                df['high'].max()
            )

            print(
                f'Highest Price: {highest_price}'
            )

            # ---------------------
            # Highest Volume Day
            # ---------------------

            highest_volume_day = (

                df.loc[
                    df['volume'].idxmax()
                ]

            )

            print(
                '\nHighest Volume Day:'
            )

            print(
                highest_volume_day
            )

            # ---------------------
            # Daily Return
            # ---------------------

            df['daily_return'] = (

                df['close']
                .pct_change()

            )

            mean_return = (

                df['daily_return']
                .mean()

            )

            volatility = (

                df['daily_return']
                .std()

            )

            min_return = (

                df['daily_return']
                .min()

            )

            max_return = (

                df['daily_return']
                .max()

            )

            # ---------------------
            # Summary Table
            # ---------------------

            summary.append({

                'Ticker': ticker,

                'Average Close':

                    df['close'].mean(),

                'Highest Price':

                    highest_price,

                'Mean Return':

                    mean_return,

                'Volatility':

                    volatility,

                'Min Return':

                    min_return,

                'Max Return':

                    max_return

            })

        except Exception as e:

            print(
                f'Error with {ticker}'
            )

            print(e)

    # ==================================
    # Export Summary
    # ==================================

    summary_df = pd.DataFrame(
        summary
    )

    summary_df.to_csv(

        'outputs/summary_statistics.csv',

        index=False

    )

    print(

        '\nSummary saved to outputs/summary_statistics.csv'

    )

    return summary_df


if __name__ == '__main__':

    result = analyze_stocks(
        VN30
    )

    print('\n===== SUMMARY =====')

    print(result.head())