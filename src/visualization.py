# ======================================
# visualization.py
# Visualization for VN30 Project
# ======================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

VN30 = [
    'ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR',
    'HDB', 'HPG', 'MBB', 'MSN', 'MWG', 'PLX', 'SAB', 'SHB',
    'SSB', 'SSI', 'STB', 'TCB', 'TPB', 'VCB', 'VHM', 'VIB',
    'VIC', 'VJC', 'VNM', 'VPB', 'VRE', 'VIX'
]


def create_visualizations(tickers):

    os.makedirs(
        'images',
        exist_ok=True
    )

    # ==================================
    # 1. LINE CHART
    # ==================================

    print("\nCreating Line Charts...")

    for ticker in tickers:

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            plt.figure(
                figsize=(12, 6)
            )

            plt.plot(

                pd.to_datetime(
                    df['time']
                ),

                df['close']

            )

            plt.title(

                f'{ticker} Closing Price'

            )

            plt.xlabel(

                'Date'

            )

            plt.ylabel(

                'Price (VND)'

            )

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            plt.savefig(

                f'images/{ticker}_line.png'

            )

            plt.close()

        except Exception as e:

            print(
                f'Line Chart Error {ticker}'
            )

            print(e)

    print("✓ Line Charts Completed")

    # ==================================
    # 2. HISTOGRAM RETURN
    # ==================================

    print("\nCreating Histograms...")

    for ticker in tickers:

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            df['daily_return'] = (

                df['close']
                .pct_change()

            )

            plt.figure(
                figsize=(8, 5)
            )

            plt.hist(

                df['daily_return']
                .dropna(),

                bins=30

            )

            plt.title(

                f'{ticker} Return Distribution'

            )

            plt.xlabel(

                'Daily Return'

            )

            plt.ylabel(

                'Frequency'

            )

            plt.tight_layout()

            plt.savefig(

                f'images/{ticker}_histogram.png'

            )

            plt.close()

        except Exception as e:

            print(
                f'Histogram Error {ticker}'
            )

            print(e)

    print("✓ Histograms Completed")

    # ==================================
    # 3. SCATTER PLOT
    # ==================================

    print("\nCreating Scatter Plots...")

    for ticker in tickers:

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            plt.figure(
                figsize=(8, 5)
            )

            plt.scatter(

                df['volume'],

                df['close']

            )

            plt.title(

                f'{ticker}: Volume vs Close'

            )

            plt.xlabel(

                'Volume'

            )

            plt.ylabel(

                'Close Price'

            )

            plt.tight_layout()

            plt.savefig(

                f'images/{ticker}_scatter.png'

            )

            plt.close()

        except Exception as e:

            print(
                f'Scatter Error {ticker}'
            )

            print(e)

    print("✓ Scatter Plots Completed")

    # ==================================
    # 4. BAR CHART AVG RETURN
    # ==================================

    print("\nCreating Average Return Chart...")

    avg_return = {}

    for ticker in tickers:

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            avg_return[ticker] = (

                df['close']
                .pct_change()
                .mean()

            )

        except:

            continue

    plt.figure(
        figsize=(12, 6)
    )

    plt.bar(

        avg_return.keys(),

        avg_return.values()

    )

    plt.title(

        'Average Daily Return - VN30'

    )

    plt.ylabel(

        'Return'

    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(

        'images/avg_return_vn30.png'

    )

    plt.close()

    print("✓ Average Return Chart Completed")

    # ==================================
    # 5. CORRELATION HEATMAP
    # ==================================

    print("\nCreating Heatmap...")

    returns = pd.DataFrame()

    for ticker in tickers:

        try:

            df = pd.read_csv(
                f'data/{ticker}.csv'
            )

            returns[ticker] = (

                df['close']
                .pct_change()

            )

        except:

            continue

    corr = returns.corr()

    plt.figure(
        figsize=(18, 14)
    )

    sns.heatmap(

        corr,

        cmap='coolwarm',

        annot=False

    )

    plt.title(

        'VN30 Correlation Heatmap'

    )

    plt.tight_layout()

    plt.savefig(

        'images/vn30_heatmap.png'

    )

    plt.close()

    print("✓ Heatmap Completed")


if __name__ == '__main__':

    create_visualizations(
        VN30
    )

    print(
        "\nAll visualizations completed!"
    )