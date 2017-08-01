import datetime

from stock_option import StockOptions


def num_vested(stock_options: list, date: datetime.date = datetime.date.today()) -> int:
    """Calculate the total numbef of vested stock options."""
    
    count = 0
    
    for options in stock_options:
        count += options.num_vested(date)
    
    return count


def buy_price(stock_options: list, date: datetime.date = datetime.date.today()) -> float:
    """Calculate the total excise price for all vested stock options."""
    
    price = 0.0
    
    for options in stock_options:
        price += options.buy_price(date)
    
    return price


def summary(stock_options: list):
    
    print("Count\tPrice\tStart Date\tAge\tBuy Price\tNum Vested")
    
    for o in stock_options:
        print("{0}\t{1}\t{2}\t{3}\t{4:.2f}\t\t{5:.2f}".format(
            o.num_assigned,
            o.excise_price,
            o.date,
            o.age(),
            o.buy_price(),
            o.num_vested()))
    
    print("\nTotal number vested: {0:.2f}".format(num_vested(stock_options)))


def per_month(stock_options: list):
    
    print("Date\tVested\tOutstanding")
    
    num_outstanding = 0
    for o in stock_options:
        num_outstanding += o.num_assigned
    
    for year in range(2008, 2019):
        for month in range(1, 13):
            
            vested = num_vested(stock_options, datetime.date(year, month, 1))
            print("{0}/{1}\t{2:.2f}\t\t{3:.2f}".format(
                month, year,
                vested, num_outstanding - vested))


def test_num_vested():
    
    count = num_vested([StockOptions(400, 1.0, datetime.date(2014, 10, 1))], datetime.date(2015, 10, 1)) 
    assert count == 100, "expected 100; found {0}".format(count)
    
    count = num_vested([StockOptions(400, 1.0, datetime.date(2014, 10, 1)), StockOptions(400, 1.0, datetime.date(2015, 10, 1))], datetime.date(2016, 10, 1)) 
    assert count == 300, "expected 100; found {0}".format(count)


def test_buy_price():
    
    price = buy_price([StockOptions(400, 1.0, datetime.date(2014, 10, 1))], datetime.date(2015, 10, 1)) 
    assert price == 100.0, "expected 100.0; found {0}".format(price)
    
    price = buy_price([StockOptions(400, 1.0, datetime.date(2014, 10, 1)), StockOptions(400, 1.0, datetime.date(2015, 10, 1))], datetime.date(2016, 10, 1)) 
    assert price == 300.0, "expected 300.0; found {0}".format(price)


if __name__ == "__main__":
    
    test_num_vested()
    test_buy_price()