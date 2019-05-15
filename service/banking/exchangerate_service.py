import os, sys
import inspect, types

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add abase_serviceolute path to current sys.path


from service.base_service import BaseService

"""
doc: Service class to process logic
"""
class ExchangeRateService():
    
    def __init__(self):
        self.base_service = BaseService()        
        self.domain_container = self.base_service.DomainContainer()
        self.util_common = self.base_service.UtilCommon()
        self.util_data = self.base_service.UtilData()
        self.ApiConfigModel = self.domain_container.init_ModelClass('ApiConfigModel')
        self.ApiParamConfigModel = self.domain_container.init_ModelClass('ApiParamConfigModel')
        self.ApiOpenExcRateModel = self.domain_container.init_ModelClass('ApiOpenExcRateModel')
        self.ApiConfig1 = self.base_service.Config.getApiConfig("openexchangerates_exchange_rates")
        

    def __init_apiUrl(self):        
        if self.ApiConfig1:
            return "{0}{1}".format(self.ApiConfig1.site_domain, self.ApiConfig1.api_url)
        return None
    

    def __init_apiParamsString(self):
        if self.ApiConfig1:
            lstApiParam = self.domain_container.map_ListJsonToListDomainClass(self.ApiParamConfigModel, self.ApiConfig1.api_params)
            apiStr = ""
            for idx, para in enumerate(lstApiParam):
                singleParam = "{0}={1}".format(para.param_name, para.default_value)
                if(idx == 0):
                    apiStr = singleParam
                    continue
                apiStr += "&" + singleParam                    
            return apiStr
        return None


    def get_exrate_byDate(self, dateReport, baseCurrency):       
        apiUrl = "{0}{1}{2}?{3}".format(self.__init_apiUrl(), dateReport, self.ApiConfig1.api_extension, self.__init_apiParamsString())
        if apiUrl:
            content = self.util_data.readJsonFromUrl(apiUrl)
            return content

        return None


    def get_specific_exrate_byDate(self, dateReport, baseCurrency, toCurrency):
        data = self.get_exrate_byDate(dateReport, baseCurrency)
        for key, value in data.items():
            print(key + ' - ' + str(value))
            if(isinstance(value, dict) and key == "rates"):
                for cur, rate in value.items():
                    if(cur == toCurrency):
                        model = self.ApiOpenExcRateModel()
                        model.Currency = toCurrency
                        model.RateValue = rate
                        return model

        return None       


    def get_specific_exrate_byDateRange(self, fromDate, toDate, baseCurrency, toCurrency):
        from datetime import timedelta, date

        def daterange(start_date, end_date):
            for n in range(int ((end_date - start_date).days)):
                yield start_date + timedelta(n)

        start_date = date(2013, 1, 1)
        end_date = date(2015, 6, 2)
        for single_date in daterange(start_date, end_date):
            print(single_date.strftime("%Y-%m-%d"))
        
        # data = self.get_specific_exrate_byDate()
        
        

        return None                   

        



