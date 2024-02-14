# pcost.py

import sys

def portfolio_cost(path):
    stockdicts = []
    with open(path) as f:
        for row in f:
            name, shares, price = row.split()
            try:
                shares = int(shares)
                price = float(price)
                d = dict(zip(['name', 'shares', 'price'], (name, shares, price)))
                print(d)
                stockdicts.append(d)
            except ValueError as e:
                print('Could not parse: ', row, end='')
                print('Reason: ', e)

    return sum(s['shares'] * s['price'] for s in stockdicts)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit('Usage: pcost portfile')
    print('Total cost:', portfolio_cost(sys.argv[1]))
