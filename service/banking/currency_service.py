import os, sys
import inspect, types
from datetime import timedelta, date, datetime

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add abase_serviceolute path to current sys.path


from service.base_service import BaseService

"""
doc: Service class to process logic
"""
class CurrencyService():
    


    def __init__(self):
        self.base_service = BaseService()        
        self.domain_factory = self.base_service.DomainFactory()
        self.util_common = self.base_service.UtilCommon()
        self.util_data = self.base_service.UtilData()        
        
        self.ConfigApiModel = self.domain_factory.init_ModelClass('ConfigApiModel')
        self.ConfigApiQueryModel = self.domain_factory.init_ModelClass('ConfigApiQueryModel')
        self.ApiOpenExcRateModel = self.domain_factory.init_ModelClass('ApiOpenExcRateModel')
        self.ExchangeRateModel = self.domain_factory.init_ModelClass('ExchangeRateModel')
        

    # def get_currency_supportbyApi(self, apiConfig, apiPathVariable):
    #     modelBaseCurParam = self.ConfigApiQueryModel()    
    #     modelBaseCurParam.param_name = "base"
    #     modelBaseCurParam.param_curvalue = baseCurrency

    #     lstCustomizeParam = []
    #     lstCustomizeParam.append(modelBaseCurParam)
        
    #     apiUrl = self.base_service.Config.initApiUrl(apiConfig, dateReport, lstCustomizeParam)
    #     if apiUrl:
    #         content = self.util_data.readJsonFromUrl(apiUrl)
    #         return content

    #     return None

    


    
     

        



