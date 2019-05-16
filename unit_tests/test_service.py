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

    
    # def test_exrate__get_exrate_byDate(self):

    #     datereport = '2016-01-15'
    #     baseCurrency = 'USD'

    #     service = ExchangeRateService()
    #     data = service.get_exrate_byDate(datereport, baseCurrency)

    #     self.assertIsNotNone(data, '###Error Message: No data')
    

    # def test_exrate__get_specific_exrate_byDate(self):

    #     datereport = '2016-01-15'
    #     baseCurrency = 'USD'
    #     toCurrency = 'VND'

    #     service = ExchangeRateService()
    #     data = service.get_specific_exrate_byDate(datereport, baseCurrency, toCurrency)
               
    #     self.assertIsNotNone(data, '###Error Message: No data')

    
    def test_exrate__get_specific_exrate_byDateRange(self):

        fromDate = '2016-01-1'        
        toDate = '2016-12-30'
        checkedDate = [15, 5, 10, 20]
        baseCurrency = 'USD'
        toCurrency = 'VND'

        service = ExchangeRateService()
        data = service.get_specific_exrate_byDateRange(fromDate, toDate, checkedDate, baseCurrency, toCurrency)

        # service.display_graph(data)
        service.training_model(data)

        self.assertIsNotNone(data, '###Error Message: No data')

        
       

###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()
