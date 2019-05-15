import unittest
import sys, os
import urllib
import urllib.parse


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from core_utils.util_common import Core_UtilityCommon
from core_utils.util_data import Core_UtilityData

class UtilityTestCase(unittest.TestCase):

    UtilCommon = Core_UtilityCommon()
    UtilData = Core_UtilityData()

    def test_common__validateDateFormat(self):
                       
        self.assertTrue(UtilityTestCase.UtilCommon.validateDateFormat('2016-01-15'), '###Error Message: Not valid')

        self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2016-01-32'), '###Error Message: Not valid')

        self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2016-13-01'), '###Error Message: Not valid')

        self.assertFalse(UtilityTestCase.UtilCommon.validateDateFormat('2019-2-30'), '###Error Message: Not valid')

    def test_data_readJsonFromUrl(self):
        args = '2016-01-15'
        baseCurrency = 'USD'
        url = "https://openexchangerates.org/api/historical/{0}.json?app_id=e1e21981345b4bbe959f49186802ce97&base={1}".format(args, baseCurrency)# urllib.parse.urlencode()
        
        content = UtilityTestCase.UtilData.readJsonFromUrl(url)
        print(content)
        # for item in content:
        #     print(item['title'] + ' - ' + item['woeid'])

###########################################################################################################
"""
doc: Code will begin from here
"""
if __name__ == '__main__':

    unittest.main()
