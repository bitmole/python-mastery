def hello():
    return "Hello from python-mastery!"

def pcost():
    from .pcost import portfolio_cost
    print('Total: ', portfolio_cost('Data/portfolio.dat'))
