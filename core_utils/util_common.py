from datetime import datetime, timedelta, date


class Core_UtilityCommon():


    def __init__(self):
        pass

    def validateDateFormat(self, date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError as ex:
            print('Error: ', ex)
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
            
            date_time_obj = datetime.strptime(datetime_text, '%Y-%m-%d %H:%M:%S.%f')
            # print('Date:', date_time_obj.date())  
            # print('Time:', date_time_obj.time())  
            # print('Date-time:', date_time_obj)  
            return date_time_obj
        except Exception as ex:
            print('Error: ', ex)
            return None

    def dateRange(self, start_date, end_date):              
        try:
            start_date = (type(start_date) is str) and self.parseStringToDate(start_date) or start_date
            end_date = (type(end_date) is str) and self.parseStringToDate(end_date) or end_date                
            
            for n in range(int ((end_date - start_date).days + 1)):
                yield start_date + timedelta(n)
        except Exception as ex:
            print('Error: ', ex)
            return None   
        
        
