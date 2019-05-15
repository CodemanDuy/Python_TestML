import json
import sys, os
from pathlib import Path, PureWindowsPath

ROOT_DIR = os.getcwd()# Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

class Configuration():
    

    def __init__(self):
        Configuration.ConfigFileName = "config.json"
        Configuration.Platform = self.getOSplatform()
        self.apiType_banking = "banking_exchange_rates"

        
    def getOSplatform(self):        
        os = ""

        if sys.platform == "linux" or sys.platform == "linux2":            
            os = "Linux"
        elif sys.platform == "darwin":            
            os = "OSX"
        elif sys.platform == "win32":
            os = "Window"
        
        return os
    

    def getApiConnection(self, apiName, apiType):
        
        try:
            filename = Path(ROOT_DIR + r'\\' + Configuration.ConfigFileName)
            with open(filename, 'rt') as config_file:
                config = json.load(config_file)
                # print(config)  
                for cf in list(config['configurations']):
                    if(cf['type'] == "api" and cf['api_type'] == self.apiType_banking and cf['is_default'] == "True"):
                        return cf
            
            return None

        except Exception as ex:
            print('Error: ', ex)


    

        
