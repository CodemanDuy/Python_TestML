import sys
import os
import datetime


ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from config import Configuration

from service.banking.exchangerate_service import ExchangeRateService

"""
doc: Main base class
"""
class Main():

    def __init__(self):
        self.ApiGetExcRateConfig = Configuration().getApiConfig("get_exchangerate")
        self.ApiGetCurrencyConfig = Configuration().getApiConfig("get_currency")
        

    def mainProcess(self):

        try:

            print("Welcome to Exchange Rates Service!")
            option = input("Which services do you want to use?: \
                \n1. Predict tight range of matching (Quick process) \
                \n2. Predict wide range of matching (Long process) \
                \n3. Check exchange rates of specific currency \
                \n4. Check all exchange rates \
                \nAny key to quit... \
                \nPlease input your choice's number: ").strip()
           

            while ( option.isdigit() and int(option) > 0 and int(option) < 5 ):
                option = int(option)

                checkedDate = input("Which date do you want to check? (YYYY-MM-DD): ").strip()
                baseCurrency = input("From currency (Code ISO 4217): ").strip()
                toCurrency = ''

                if(option == 1):
                    self.validateInput(option, checkedDate, baseCurrency, toCurrency)

                    service = ExchangeRateService()
                    data = service.predicted_quick_exrate(self.ApiGetExcRateConfig, self.checkedDate, self.baseCurrency, self.toCurrency)
                    service.display_graph(data)

                elif(option == 2):
                    self.validateInput(option, checkedDate, baseCurrency, toCurrency)
                    checkedDaysPerMonth = 10

                    service = ExchangeRateService()
                    data = service.predicted_long_exrate(self.ApiGetExcRateConfig, self.checkedDate, self.baseCurrency, self.toCurrency, checkedDaysPerMonth)
                    service.display_graph(data)

                elif(option == 3):
                    self.validateInput(option, checkedDate, baseCurrency, toCurrency)
                    
                    service = ExchangeRateService()
                    data = service.get_specific_exrate_byDate(self.ApiGetExcRateConfig, self.checkedDate, self.baseCurrency, self.toCurrency)
                    print(str(data.Currency) + " - " +  str(data.RateValue))

                elif(option == 4):
                    self.validateInput(option, checkedDate, baseCurrency, toCurrency)
                    
                    service = ExchangeRateService()
                    data = service.get_exrate_byDate(self.ApiGetExcRateConfig, self.checkedDate, self.baseCurrency)
                    print("\n".join([str(m.Currency) + " - " + str(m.RateValue) for m in data]))

                else:
                   pass

                print("-"*30 + "PROCESS DONE" + "-"*30)
                
                option = input("Which services do you want to use?: \
                \n1. Predict tight range of matching (Quick process) \
                \n2. Predict wide range of matching (Long process) \
                \n3. Check exchange rates of specific currency \
                \n4. Check all exchange rates \
                \nAny key to quit... \
                \nPlease input your choice's number: ").strip()

        except Exception as ex:
            print('Error: ', ex)

        print('#'*40)
        return

    def validateInput(self, option, checkedDate, baseCurrency, toCurrency):
        self.baseCurrency = (not baseCurrency) and 'USD' or str(baseCurrency).upper()
        
        currentDate = datetime.date.today()
        if ExchangeRateService().UtilCommon().validateDateFormat(checkedDate):
            checkedDate = ExchangeRateService().UtilCommon().parseStringToDateTime(checkedDate).date()
            self.checkedDate = (checkedDate >= currentDate) and currentDate or checkedDate
        else:                
            self.checkedDate = currentDate

        if(option == 1 or option == 2 or option == 3):
            self.toCurrency = toCurrency
            countFail = 0
            while not toCurrency:
                if countFail > 0:
                    print("###Error: No data for To Currency")
                toCurrency = input("To currency (Code ISO 4217): ").strip()
                self.toCurrency = str(toCurrency).upper()
                countFail += 1
        

"""
doc: Code will begin from here
"""
if __name__ == '__main__':
    proc = Main()
    proc.mainProcess()



### BUILD APP
# Step 1: Put all images folder to "dist" folder (folder to deploy app) 
# Step 2: Open CMD/Terminal and change directory path to main python script
# Step 3: Run command in first time => pyinstaller --clean --distpath=./app_build --workpath=./temp --onefile --name ExchangeRatesPrediction ./__main__.py
# Or Run this command when already have .spec file => pyinstaller --clean --distpath=./app_build --workpath=./temp --add-data="config.json;." --add-data="/model_trained/linear_model.pkl;." --onefile ExchangeRatesPrediction.spec
