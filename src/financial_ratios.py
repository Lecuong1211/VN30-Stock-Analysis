# ======================================
# financial_ratios.py
# Financial Analysis VN30
# ======================================

import os
import pandas as pd
from vnstock import *


VN30 = [
    'ACB', 'BCM', 'BID', 'BVH', 'CTG', 'FPT', 'GAS', 'GVR',
    'HDB', 'HPG', 'MBB', 'MSN', 'MWG', 'PLX', 'SAB', 'SHB',
    'SSB', 'SSI', 'STB', 'TCB', 'TPB', 'VCB', 'VHM', 'VIB',
    'VIC', 'VJC', 'VNM', 'VPB', 'VRE', 'VIX'
]


def calculate_ratios(tickers):

    os.makedirs(
        'outputs',
        exist_ok=True
    )

    results = []

    for ticker in tickers:

        print(
            f'\nProcessing {ticker}'
        )

        try:

            stock = Vnstock().stock(

                symbol=ticker,

                source='VCI'

            )

            income = (

                stock.finance
                .income_statement(
                    period='year'
                )

            )

            balance = (

                stock.finance
                .balance_sheet(
                    period='year'
                )

            )

            # ======================
            # Market Price
            # ======================

            price = pd.read_csv(

                f'data/{ticker}.csv'

            )['close'].iloc[-1]

            # ======================
            # Net Income
            # ======================

            net_income = income.loc[

                income['item_en']

                ==

                'Net profit/(loss) after tax',

                '2024'

            ].iloc[0]

            # ======================
            # Total Assets
            # ======================

            assets = balance.loc[

                balance['item_en']

                ==

                'Total Assets',

                '2024'

            ].iloc[0]

            # ======================
            # Owner Equity
            # ======================

            equity = balance.loc[

                balance['item_en']

                ==

                "Owner's Equity",

                '2024'

            ].iloc[0]

            # ======================
            # EPS
            # ======================

            eps = income.loc[

                income['item_en']

                ==

                'EPS basic (VND)',

                '2024'

            ].iloc[0]

            # ======================
            # Total Liabilities
            # ======================

            liabilities = balance.loc[

                balance['item_en']

                ==

                'Total liabilities',

                '2024'

            ].iloc[0]

            # ======================
            # Current Assets
            # ======================

            current_assets = balance.loc[

                balance['item_en']

                ==

                'Current Assets',

                '2024'

            ].iloc[0]

            # ======================
            # Current Liabilities
            # ======================

            current_liabilities = balance.loc[

                balance['item_en']

                ==

                'Current liabilities',

                '2024'

            ].iloc[0]

            # ======================
            # Shares Outstanding
            # ======================

            shares = (

                equity

                /

                (

                    balance.loc[

                        balance['item_en']

                        ==

                        'Book value per share (VND)',

                        '2024'

                    ].iloc[0]

                )

            )

            # ======================
            # BVPS
            # ======================

            bvps = (

                equity

                /

                shares

            )

            # ======================
            # Ratios
            # ======================

            roe = (

                net_income

                /

                equity

            )

            roa = (

                net_income

                /

                assets

            )

            pe = (

                price

                /

                eps

            )

            pb = (

                price

                /

                bvps

            )

            current_ratio = (

                current_assets

                /

                current_liabilities

            )

            debt_equity = (

                liabilities

                /

                equity

            )

            results.append({

                'Ticker': ticker,

                'Price': price,

                'ROE': roe,

                'ROA': roa,

                'P/E': pe,

                'P/B': pb,

                'Current Ratio':

                    current_ratio,

                'Debt/Equity':

                    debt_equity

            })

        except Exception as e:

            print(
                f'Error {ticker}'
            )

            print(e)

    return pd.DataFrame(
        results
    )


if __name__ == '__main__':

    ratios = calculate_ratios(
        VN30
    )

    ratios.to_csv(

        'outputs/financial_ratios.csv',

        index=False

    )

    print(
        '\nSaved financial_ratios.csv'
    )

    # ==========================
    # Top 5 ROE
    # ==========================

    print(
        '\nTOP 5 ROE'
    )

    print(

        ratios
        .sort_values(

            'ROE',

            ascending=False

        )

        [['Ticker', 'ROE']]

        .head()

    )

    # ==========================
    # Top 5 P/E thấp
    # ==========================

    print(
        '\nTOP 5 LOWEST P/E'
    )

    print(

        ratios
        .sort_values(

            'P/E'

        )

        [['Ticker', 'P/E']]

        .head()

    )

    # ==========================
    # Top 5 P/B thấp
    # ==========================

    print(
        '\nTOP 5 LOWEST P/B'
    )

    print(

        ratios
        .sort_values(

            'P/B'

        )

        [['Ticker', 'P/B']]

        .head()

    )