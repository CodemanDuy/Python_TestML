import unittest
import sys, os
import urllib
import urllib.parse
import datetime


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from core_utils.util_common import Core_UtilityCommon
from core_utils.util_data import Core_UtilityData
from core_utils.util_logic import Core_UtilityLogic
from config import Configuration

from service.banking.exchangerate_service import ExchangeRateService

class UtilityTestCase(unittest.TestCase):

    UtilCommon = Core_UtilityCommon()
    UtilData = Core_UtilityData()
    UtilLogic = Core_UtilityLogic()
    Config = Configuration()

    # ###########################################################################################################
    # def test_common__validateDateFormat(self):
                       
    #     self.assertTrue(UtilityTestCase.UtilCommon.validateDateFormat('2016-01-15'), '###Error Message: Not valid')

    #     self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2016-01-32'), '###Error Message: Not valid')

    #     self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2016-13-01'), '###Error Message: Not valid')

    #     self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2019-02-30'), '###Error Message: Not valid')


    # def test_common__parseStringToDate(self):

    #     data = UtilityTestCase.UtilCommon.parseStringToDate('2016-01-15')
    #     self.assertIsNotNone(data, '###Error Message: No data')

    #     data = UtilityTestCase.UtilCommon.parseStringToDate(datetime.date(2019,1,15))
    #     self.assertIsNotNone(data, '###Error Message: No data')

    # ###########################################################################################################

    # def test_data__readJsonFromUrl(self):

    #     data = UtilityTestCase.UtilData.readJsonFromUrl("https://openexchangerates.org/api/historical/2001-02-16.json?app_id=e1e21981345b4bbe959f49186802ce97")

    #     self.assertIsNotNone(data, '###Error Message: No data')

    ###########################################################################################################

    def test_logic__calLinearRegressionOfY(self):
        
        lstX = [60, 61, 62, 63, 65]
        lstY = [3.1, 3.6, 3.8, 4, 4.1]
        x = 64

        data = UtilityTestCase.UtilLogic.calLinearRegressionOfY(lstX, lstY, x)
        print(data)

        self.assertIsNotNone(data, '###Error Message: No data')

    def test_logic__calLinearRegressionOfListY(self):
        
        lstX = [60, 61, 62, 63, 65]
        lstY = [3.1, 3.6, 3.8, 4, 4.1]
        x = [64, 66, 67, 68]

        data = UtilityTestCase.UtilLogic.calLinearRegressionOfListY(lstX, lstY, x)
        print(data)

        self.assertIsNotNone(data, '###Error Message: No data')

       

###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()
