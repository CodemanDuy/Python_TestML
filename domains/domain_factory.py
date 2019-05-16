import inspect
import sys

from domains.analysis_data.ExchangeRateModel import ExchangeRateModel
from domains.api.ApiOpenExcRateModel import ApiOpenExcRateModel
from domains.config.ConfigApiModel import ConfigApiModel
from domains.config.ConfigApiParamModel import ConfigApiParamModel

#Factory Pattern
"""
doc: Container to declare all entities model
"""
class DomainFactory():

    def __init__(self):
        pass


    def get_allDomainClassRegistered(self):

        container = [(name, obj) for name, obj in list(inspect.getmembers(sys.modules[__name__], inspect.isclass)) if name not in DomainFactory.__name__]
        return container
            

    def init_ModelClass(self, className):

        clsmembers = self.get_allDomainClassRegistered()
        for name, obj in clsmembers:
            if name in className:
                return obj


    def init_ObjectClass(self, className):

        clsmembers = self.get_allDomainClassRegistered()
        for name, obj in clsmembers:
            if name in className:
                return obj()


    def map_JsonToDomainClass(self, modelClass, obj):

        if modelClass is None or obj is None:
            return None

        modelAttrs = [str(item[0]).lower() for item in inspect.getmembers(modelClass) if isinstance(getattr(modelClass, item[0], None), property)]
        
        model = modelClass()

        for key, value in obj.items():
            if any(item in key for item in modelAttrs):
                setattr(model, key, value)#setattr(object, name, value)

        return model


    def map_ListJsonToListDomainClass(self, modelClass, listObj):

        if modelClass is None or not listObj:
            return None
        
        modelAttrs = [str(item[0]).lower() for item in inspect.getmembers(modelClass) if isinstance(getattr(modelClass, item[0], None), property)]  
        listModel = []
        for obj in listObj:  
            model = modelClass()
            for key, value in obj.items():
                if any(item in key for item in modelAttrs):
                    setattr(model, key, value)#setattr(object, name, value)
            listModel.append(model)
        
        return listModel
    

    def map_UpdateValueToAnDomainClass(self, modelClass, attrName, attrValue):

        if attrName is None or attrValue is None:
            return None
            
        setattr(modelClass, attrName, attrValue)
        
        return modelClass

       