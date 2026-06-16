# ======================================
# data_download.py
# Download VN30 stock data from vnstock
# ======================================

import os
from vnstock import *


# ======================================
# 1. Danh sách VN30
# ======================================

VN30 = [
    'ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR',
    'HDB', 'HPG', 'MBB', 'MSN', 'MWG', 'PLX', 'SAB', 'SHB',
    'SSB', 'SSI', 'STB', 'TCB', 'TPB', 'VCB', 'VHM', 'VIB',
    'VIC', 'VJC', 'VNM', 'VPB', 'VRE', 'VIX'
]


# ======================================
# 2. Hàm tải dữ liệu
# ======================================

def download_stock_data(
    tickers,
    start_date='2024-01-01',
    end_date='2025-06-01'
):
    """
    Download historical stock prices.

    Parameters
    ----------
    tickers : list
        List of stock symbols.

    start_date : str
        Start date (YYYY-MM-DD)

    end_date : str
        End date (YYYY-MM-DD)
    """

    os.makedirs(
        'data',
        exist_ok=True
    )

    success = 0
    failed = 0

    print("\nDownloading VN30 data...\n")

    for ticker in tickers:

        try:

            print(
                f'Downloading {ticker}...'
            )

            stock = Vnstock().stock(

                symbol=ticker,

                source='VCI'

            )

            df = stock.quote.history(

                start=start_date,

                end=end_date,

                interval='1D'

            )

            if df.empty:

                print(
                    f'No data for {ticker}'
                )

                failed += 1

                continue

            df.to_csv(

                f'data/{ticker}.csv',

                index=False

            )

            print(
                f'✓ Saved data/{ticker}.csv'
            )

            success += 1

        except Exception as e:

            print(
                f'✗ Error downloading {ticker}'
            )

            print(e)

            failed += 1

    print("\n========== SUMMARY ==========")

    print(
        f'Success: {success}'
    )

    print(
        f'Failed : {failed}'
    )

    print(
        f'Total  : {len(tickers)}'
    )

    print("=============================\n")


# ======================================
# 3. Chạy trực tiếp file
# ======================================

if __name__ == '__main__':

    download_stock_data(

        tickers=VN30,

        start_date='2024-01-01',

        end_date='2025-06-01'

    )