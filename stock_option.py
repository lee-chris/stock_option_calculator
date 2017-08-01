import datetime

class StockOptions(object):
    """A single assignment of granted stock options.
    
    This class is initialized with the number of stock options awarded,
    the excise price per share, and the date the stock options were assigned.
    """
    
    
    def __init__(self, num_assigned, excise_price, date):
        
        self.num_assigned = num_assigned
        self.excise_price = excise_price
        self.date = date
    
    
    def age(self, date=datetime.date.today()):
        """Calculate the age of the stock options in months."""
        
        years = date.year - self.date.year
        
        if date.month < self.date.month:
            years -= 1
        
        # the max age is 4 years (48 months)
        if years >= 4:
            return 48
        
        months = date.month - self.date.month
        
        if date.day < self.date.day:
            months -= 1
        
        return years * 12 + months
    
    
    def num_vested(self, date=datetime.date.today()):
        """Return the number of vested stock options."""
        
        age = self.age(date)
        
        vested = 0
        
        if age >= 12:
            
            vested = self.num_assigned * 0.25
            age -= 12
        
            vested += age * (self.num_assigned / 4 / 12)
        
        return vested
    
    
    def buy_price(self, date=datetime.date.today()):
        """Calculate the total excise price for all vested stock options."""
        
        return self.num_vested(date) * self.excise_price
    

def test():
    
    options1 = StockOptions(960, 1.0, datetime.date(2008, 10, 21))
    
    assert options1.age(datetime.date(2009, 10, 21)) == 12
    assert options1.age(datetime.date(2009, 11, 1)) == 12
    assert options1.age(datetime.date(2010, 10, 21)) == 24
    assert options1.age(datetime.date(2011, 10, 21)) == 36
    assert options1.age(datetime.date(2012, 10, 21)) == 48
    assert options1.age(datetime.date(2013, 10, 21)) == 48
    
    assert options1.num_vested(datetime.date(2000, 10, 21)) == 0
    assert options1.num_vested(datetime.date(2008, 11, 21)) == 0
    assert options1.num_vested(datetime.date(2009, 10, 21)) == 240
    assert options1.num_vested(datetime.date(2009, 11, 21)) == 260
    
    assert options1.buy_price(datetime.date(2009, 10, 21)) == 240.0
    
    
if __name__ == "__main__":
    test()