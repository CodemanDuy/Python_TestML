import json
import sys, os
from pathlib import Path, PureWindowsPath

ROOT_DIR = os.getcwd()# Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print('Path: ' + str(sys.path))

from domains.domain_factory import DomainFactory

class Configuration():
    

    def __init__(self):
        self.ConfigFileName = "config.json"
        self.ConfigFilePath = Path(ROOT_DIR + r'\\' + self.ConfigFileName)
        self.Platform = self.getOSplatform()
        self.domain_factory = DomainFactory()
        self.ConfigApiModel = self.domain_factory.init_ModelClass('ConfigApiModel')
        self.ConfigApiQueryModel = self.domain_factory.init_ModelClass('ConfigApiQueryModel')

        
    def getOSplatform(self):        
        os = ""

        if sys.platform == "linux" or sys.platform == "linux2":            
            os = "Linux"
        elif sys.platform == "darwin":            
            os = "OSX"
        elif sys.platform == "win32":
            os = "Window"
        
        return os
    

    def getApiConfig(self, apiType):        
        try:
            if apiType:

                with open(self.ConfigFilePath, 'rt') as config_file:
                    config = json.load(config_file)
                    # print(config)  
                    for cf in list(config['configurations']):
                        if(cf['type'] == "api" and cf['api_type'] == apiType and cf['is_using'] == "True"):
                            modelApiConfig = self.domain_factory.map_JsonToDomainClass(self.ConfigApiModel, cf)
                            return modelApiConfig

        except Exception as ex:
            print('Error: ', ex)
        
        return 


    def initApiQueryString(self, config, lstParamModel):
        if config:
            lstApiParam = self.domain_factory.map_ListJsonToListDomainClass(self.ConfigApiQueryModel, config.api_queries)
            apiStr = ""
            for idx, para in enumerate(lstApiParam):
                actual_value = para.param_defvalue
                if lstParamModel and len(lstParamModel) > 0:
                    pr = [pr for pr in lstParamModel if pr.param_name == para.param_name]
                    if pr:
                        actual_value = pr[0].param_curvalue
                singleParam = "{0}={1}".format(para.param_name, actual_value)
                if(idx == 0):
                    apiStr = singleParam
                    continue
                apiStr += "&" + singleParam                    
            return apiStr
        return None


    def initApiUrl(self, config, customPath, lstParamModel):        
        if config:
            apiUrl = "{0}{1}{2}{3}?{4}".format(config.api_host, config.api_path, customPath, config.api_extension, self.initApiQueryString(config, lstParamModel))
            return apiUrl
        return None
    

    

        
