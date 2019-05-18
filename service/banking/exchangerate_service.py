import os, sys
import inspect, types
from datetime import timedelta, date, datetime

import matplotlib.pyplot as plt

import sklearn.utils._cython_blas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add abase_serviceolute path to current sys.path


from service.base_service import BaseService

"""
doc: Service class to process logic
"""
class ExchangeRateService(BaseService):
    


    def __init__(self):
        self.base_service = BaseService()        
        self.domain_factory = self.base_service.DomainFactory()
        self.util_common = self.base_service.UtilCommon()
        self.util_data = self.base_service.UtilData()        
        
        self.ConfigApiModel = self.domain_factory.init_ModelClass('ConfigApiModel')
        self.ConfigApiQueryModel = self.domain_factory.init_ModelClass('ConfigApiQueryModel')
        self.ApiOpenExcRateModel = self.domain_factory.init_ModelClass('ApiOpenExcRateModel')
        self.ExchangeRateModel = self.domain_factory.init_ModelClass('ExchangeRateModel')
        

    def get_exrate_byDate(self, apiConfig, dateReport, baseCurrency):
        modelBaseCurParam = self.ConfigApiQueryModel()    
        modelBaseCurParam.param_name = "base"
        modelBaseCurParam.param_curvalue = baseCurrency

        lstCustomizeQuery = []
        lstCustomizeQuery.append(modelBaseCurParam)
        
        apiUrl = self.base_service.Config.initApiUrl(apiConfig, dateReport, lstCustomizeQuery)
        if apiUrl:
            content = self.util_data.readJsonFromUrl(apiUrl)
            lstRates = []
            for key, value in content.items():
                # print(key + ' - ' + str(value))
                if(isinstance(value, dict) and key == "rates"):
                    for cur, rate in value.items():
                        model = self.ApiOpenExcRateModel()
                        model.Currency = cur
                        model.RateValue = rate
                        lstRates.append(model)
            
            return lstRates

        return None


    def get_specific_exrate_byDate(self, apiConfig, dateReport, baseCurrency, toCurrency):
        data = self.get_exrate_byDate(apiConfig, dateReport, baseCurrency)
        for model in data:
            if(model.Currency == toCurrency):                
                return model

        return None       


    def get_specific_exrate_byDateRange(self, apiConfig, fromDate, toDate, checkedDate, baseCurrency, toCurrency):        
        # print('Checked Date: Exchange Rates')  
        lstExcRates = []
        for single_date in self.util_common.dateRange(fromDate, toDate):
            if any(da == single_date.day for da in checkedDate):             
                data = self.get_specific_exrate_byDate(apiConfig, single_date.strftime("%Y-%m-%d"), baseCurrency, toCurrency)  
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

    def training_linear_model(self, listdata):
        date = [[x.OnDate] for x in listdata]
        rate = [[x.RateValue] for x in listdata]

        #Use 80% of data as training, rest 20% to Test model
        x_train, x_test, y_train, y_test = train_test_split(date, rate, test_size=0.2)
        # training model
        linear = LinearRegression()
        linear.fit(x_train, y_train)

        # evaluating model
        score_trained = linear.score(x_test, y_test)
        print("Model scored:", score_trained)

        # saving model
        modelPathDir = Path(ROOT_DIR + r'/model_trained/linear_model.pkl')
        joblib.dump(linear, modelPathDir)

        # loading model
        clf = joblib.load(modelPathDir)
        predicted = clf.predict(x_test)#linear.predict(x_test)
        print("Predicted Max:", predicted.max())
        print("Predicted Min:", predicted.min())
        print("Predicted: ", predicted)

        return predicted
    

    def predicted_quick_exrate(self, apiConfig, strPredictedDate, baseCurrency, toCurrency):
        predictedDate = self.util_common.parseStringToDateTime(strPredictedDate)
        dateLastMonth = self.util_common.getDateByYearCount(strPredictedDate, -1)
        dateLastYear = self.util_common.getDateByMonthCount(strPredictedDate, -1)
        checkedDate = []
        checkedDate.append(predictedDate.day)
        

        data = self.get_specific_exrate_byDateRange(apiConfig, dateLastMonth, dateLastYear, checkedDate, baseCurrency, toCurrency)

        self.training_linear_model(data)

        return data

    def predicted_long_exrate(self, apiConfig, strPredictedDate, baseCurrency, toCurrency, checkedDaysPerMonth=5):
        predictedDate = self.util_common.parseStringToDateTime(strPredictedDate)
        dateLastMonth = self.util_common.getDateByYearCount(strPredictedDate, -1)
        dateLastYear = self.util_common.getDateByMonthCount(strPredictedDate, -1)
        checkedDate = self.util_common.generateRandomDateInMonth(year=predictedDate.year, month=predictedDate.month, totalRandom=checkedDaysPerMonth)
        if not predictedDate.day in checkedDate:
            checkedDate.append(predictedDate.day)


        data = self.get_specific_exrate_byDateRange(apiConfig, dateLastMonth, dateLastYear, checkedDate, baseCurrency, toCurrency)

        self.training_linear_model(data)

        return data


    
     

        



