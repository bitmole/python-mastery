# pcost.py

import sys

def total_cost(path):
    stockdicts = []
    with open(path) as f:
        for row in f:
            stockdicts.append(
                    dict(zip(['name', 'shares', 'price'], row.split())))
    return sum(int(s['shares'])*float(s['price']) for s in stockdicts)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit('Usage: pcost portfile')
    print('Total cost:', total_cost(sys.argv[1]))
