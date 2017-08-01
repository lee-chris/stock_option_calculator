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