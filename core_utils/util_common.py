from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import calendar
import random


class Core_UtilityCommon():


    def __init__(self):
        pass

    def validateDateFormat(self, date_text):
        try:
            if not parse(date_text, fuzzy=False):
                raise ValueError
            return True
        except ValueError as ex:
            # print('Error: ', ex)
            return False

    def parseStringToDate(self, date_text):
        try:
            if(type(date_text) is date or type(date_text) is datetime):                   
                return date_text
            
            date_obj = datetime.strptime(date_text, '%Y-%m-%d')
            datetime.combine(date_obj, datetime.min.time())
            # print('Date:', date_obj.date())  
            return date_obj 
        except Exception as ex:
            print('Error: ', ex)
            return None

    def parseStringToDateTime(self, datetime_text):
        try:
            if(type(datetime_text) is date or type(datetime_text) is datetime):              
                return datetime_text
                       
            return parse(datetime_text, fuzzy=False)

        except Exception as ex:
            print('Error: ', ex)
            return None

    def dateRange(self, start_date, end_date):              
        try:
            start_date = (type(start_date) is str) and self.parseStringToDateTime(start_date) or start_date
            end_date = (type(end_date) is str) and self.parseStringToDateTime(end_date) or end_date                
            
            for n in range(int ((end_date - start_date).days + 1)):
                yield start_date + timedelta(n)
        except Exception as ex:
            print('Error: ', ex)
            return None   
        
    def getDateByYearCount(self, date, yearcount):
        try:            
            checkedDate = self.parseStringToDateTime(date)
            return checkedDate + relativedelta(years=yearcount)

        except Exception as ex:
            print('Error: ', ex)
            return None   
    
    def getDateByMonthCount(self, date, monthcount):
        try:            
            checkedDate = self.parseStringToDateTime(date)
            return checkedDate + relativedelta(months=monthcount)
         
        except Exception as ex:
            print('Error: ', ex)
            return None   

    def generateRandomDateInMonth(self, year, month, totalRandom = 1):
        lstDate = []
        currentTotalDays = calendar.monthrange(year, month)[1]
        
        if totalRandom <= currentTotalDays:            
            rdt = random.randint(1, currentTotalDays)
            d = datetime(year, month, rdt)
            # check if random number not exist in list and list size must smaller than total random times
            while(len(lstDate) < totalRandom):
                if not d in lstDate:
                    lstDate.append(d)
                rdt = random.randint(1, currentTotalDays)
                d = datetime(year, month, rdt)
            
        return lstDate            
        

