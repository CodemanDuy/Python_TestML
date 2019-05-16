# Facade Pattern
"""
doc: Model class with the decorator
"""
class ApiOpenExcRateModel(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass

    @property
    def Currency(self):
        return self.__Currency
    @Currency.setter
    def Currency(self, val):
        self.__Currency = val


    @property
    def RateValue(self):
        return self.__RateValue
    @RateValue.setter
    def RateValue(self, val):
        self.__RateValue = val
        