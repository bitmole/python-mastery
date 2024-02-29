# readport.py

import csv

def read_portfolio(filename):
    """Reads a file into a list of dicts representing stock holdings

    :filename: TODO
    :returns: TODO

    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows) # skip headers
        for row in rows:
            holding = {
                    'name': row[0],
                    'shares': int(row[1]),
                    'price': float(row[2]),
                    }
            portfolio.append(holding)
    return portfolio
