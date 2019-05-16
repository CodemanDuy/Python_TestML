# Facade Pattern
"""
doc: Model class with the decorator
"""
class ExchangeRateModel(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass


    @property
    def BaseCurrency(self):
        return self.__BaseCurrency
    @BaseCurrency.setter
    def BaseCurrency(self, val):
        self.__BaseCurrency = val

    @property
    def ConvertedCurrency(self):
        return self.__ConvertedCurrency
    @ConvertedCurrency.setter
    def ConvertedCurrency(self, val):
        self.__ConvertedCurrency = val

    @property
    def OnDate(self):
        return self.__OnDate
    @OnDate.setter
    def OnDate(self, val):
        self.__OnDate = val


    @property
    def RateValue(self):
        return self.__RateValue
    @RateValue.setter
    def RateValue(self, val):
        self.__RateValue = val


