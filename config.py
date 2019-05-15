import json
import sys, os
from pathlib import Path, PureWindowsPath

ROOT_DIR = os.getcwd()# Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from domains.domain_container import DomainContainer

class Configuration():
    

    def __init__(self):
        self.ConfigFileName = "config.json"
        self.ConfigFilePath = Path(ROOT_DIR + r'\\' + self.ConfigFileName)
        self.Platform = self.getOSplatform()
        self.domain_container = DomainContainer()
        self.ApiConfigModel = self.domain_container.init_ModelClass('ApiConfigModel')

        
    def getOSplatform(self):        
        os = ""

        if sys.platform == "linux" or sys.platform == "linux2":            
            os = "Linux"
        elif sys.platform == "darwin":            
            os = "OSX"
        elif sys.platform == "win32":
            os = "Window"
        
        return os
    

    def getApiConfig(self, apiName):
        
        try:
            if apiName:

                with open(self.ConfigFilePath, 'rt') as config_file:
                    config = json.load(config_file)
                    # print(config)  
                    for cf in list(config['configurations']):
                        if(cf['type'] == "api" and cf['api_name'] == apiName):                            
                            modelApiConfig = self.domain_container.map_JsonToAnDomainClass(self.ApiConfigModel, cf)
                            return modelApiConfig

        except Exception as ex:
            print('Error: ', ex)
        
        return None

    

    

        
