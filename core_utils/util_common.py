from datetime import datetime


class Core_UtilityCommon():


    def __init__(self):
        pass

    def validateDateFormat(self, date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False

    