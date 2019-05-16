import os, sys
import inspect, types
from datetime import timedelta, date, datetime

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add abase_serviceolute path to current sys.path


from service.base_service import BaseService

"""
doc: Service class to process logic
"""
class ExchangeRateService():
    


    def __init__(self):
        self.base_service = BaseService()        
        self.domain_factory = self.base_service.DomainFactory()
        self.util_common = self.base_service.UtilCommon()
        self.util_data = self.base_service.UtilData()        
        self.ApiConfig1 = self.base_service.Config.getApiConfig("openexchangerates_exchange_rates")
        
        self.ConfigApiModel = self.domain_factory.init_ModelClass('ConfigApiModel')
        self.ConfigApiParamModel = self.domain_factory.init_ModelClass('ConfigApiParamModel')
        self.ApiOpenExcRateModel = self.domain_factory.init_ModelClass('ApiOpenExcRateModel')
        self.ExchangeRateModel = self.domain_factory.init_ModelClass('ExchangeRateModel')
        

    def __init_apiUrl(self):        
        if self.ApiConfig1:
            return "{0}{1}".format(self.ApiConfig1.site_domain, self.ApiConfig1.api_url)
        return None
    

    def __init_apiParamsString(self):
        if self.ApiConfig1:
            lstApiParam = self.domain_factory.map_ListJsonToListDomainClass(self.ConfigApiParamModel, self.ApiConfig1.api_params)
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
            # print(key + ' - ' + str(value))
            if(isinstance(value, dict) and key == "rates"):
                for cur, rate in value.items():
                    if(cur == toCurrency):
                        model = self.ApiOpenExcRateModel()
                        model.Currency = toCurrency
                        model.RateValue = rate
                        return model

        return None       


    def get_specific_exrate_byDateRange(self, fromDate, toDate, checkedDate, baseCurrency, toCurrency):        
        # print('Checked Date: Exchange Rates')  
        lstExcRates = []
        for single_date in self.util_common.dateRange(fromDate, toDate):
            if any(da == single_date.day for da in checkedDate):
            # if(single_date.day == checkedDate):                
                data = self.get_specific_exrate_byDate(single_date.strftime("%Y-%m-%d"), baseCurrency, toCurrency)  
                # print(single_date.strftime("%Y-%m-%d") + ': ' + str(data.RateValue))         

                model = self.ExchangeRateModel()
                model.BaseCurrency = baseCurrency
                model.ConvertedCurrency = toCurrency
                model.OnDate = single_date.month#datetime.timestamp(single_date)#convert datetime to timestamp
                model.RateValue = data.RateValue

                lstExcRates.append(model)

        return len(lstExcRates) > 0 and lstExcRates or None

    def display_graph(self, listdata):       

        date = [x.OnDate for x in listdata]
        rate = [x.RateValue for x in listdata]

        plt.scatter(
            date,
            rate,
            c='black'
        )
        plt.xlabel("Date")
        plt.ylabel("Rates")
        plt.show()

    def training_model(self, listdata):
        date = [[x.OnDate] for x in listdata]
        rate = [[x.RateValue] for x in listdata]

        #Use 70% of data as training, rest 30% to Test model
        x_train, x_test, y_train, y_test = train_test_split(date, rate, test_size=0.3)
        # training model
        linear = LinearRegression()
        linear.fit(x_train, y_train)

        # evaluating model
        score_trained = linear.score(x_test, y_test)
        print("Model scored:", score_trained)

        # saving model
        joblib.dump(linear, ROOT_DIR + r'/domains/analysis_data/linear_model_v1.pkl')

        # loading model
        clf = joblib.load(ROOT_DIR + r'/domains/analysis_data/linear_model_v1.pkl')
        predicted = clf.predict(x_test)#linear.predict(x_test)
        print("Predicted Max:", predicted.max())
        print("Predicted Min:", predicted.min())
        print("Predicted: ", predicted)
    


    
     

        



