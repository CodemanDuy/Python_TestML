import unittest
import sys, os
import urllib
import urllib.parse


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from core_utils.util_common import Core_UtilityCommon
from core_utils.util_data import Core_UtilityData
from config import Configuration

from service.banking.exchangerate_service import ExchangeRateService

class ServiceTestCase(unittest.TestCase):

    UtilCommon = Core_UtilityCommon()
    UtilData = Core_UtilityData()
    Config = Configuration()
    ApiCheckExcRateConfig = Config.getApiConfig("get_exchangerate")
        

    
    def test_exrate__get_exrate_byDate(self):

        datereport = '2017-01-15'
        baseCurrency = 'USD'

        service = ExchangeRateService()
        data = service.get_exrate_byDate(ServiceTestCase.ApiCheckExcRateConfig, datereport, baseCurrency)

        self.assertIsNotNone(data, '###Error Message: No data')
    

    def test_exrate__get_specific_exrate_byDate(self):

        datereport = '2017-01-15'
        baseCurrency = 'USD'
        toCurrency = 'EUR'

        service = ExchangeRateService()
        data = service.get_specific_exrate_byDate(ServiceTestCase.ApiCheckExcRateConfig, datereport, baseCurrency, toCurrency)
               
        self.assertIsNotNone(data, '###Error Message: No data')

    
    def test_exrate__get_specific_exrate_byDateRange(self):

        fromDate = '2017-01-1'        
        toDate = '2016-12-30'
        checkedDate = [15, 1, 5, 10, 20, 25]
        baseCurrency = 'USD'
        toCurrency = 'AUD'

        service = ExchangeRateService()
        data = service.get_specific_exrate_byDateRange(ServiceTestCase.ApiCheckExcRateConfig, fromDate, toDate, checkedDate, baseCurrency, toCurrency)

        # service.display_graph(data)
        service.training_linear_model(data)

        self.assertIsNotNone(data, '###Error Message: No data')


    def test_exrate__predicted_basic_exrate(self):

        datereport = '2017-01-15'
        baseCurrency = 'USD'
        toCurrency = 'EUR'

        service = ExchangeRateService()
        data = service.predicted_basic_exrate(ServiceTestCase.ApiCheckExcRateConfig, datereport, baseCurrency, toCurrency)
               
        self.assertIsNotNone(data, '###Error Message: No data')

        
       

###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()
