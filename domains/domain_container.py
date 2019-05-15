import inspect
import sys


from domains.api.ApiOpenExcRateModel import ApiOpenExcRateModel
from domains.config.ApiConfigModel import ApiConfigModel
from domains.config.ApiParamConfigModel import ApiParamConfigModel

"""
doc: Container to declare all entities model
"""
class DomainContainer():

    def __init__(self):
        pass


    def get_allDomainClassRegistered(self):

        container = [(name, obj) for name, obj in list(inspect.getmembers(sys.modules[__name__], inspect.isclass)) if name not in DomainContainer.__name__]
        return container
            

    def init_ModelClass(self, className):

        clsmembers = self.get_allDomainClassRegistered()
        for name, obj in clsmembers:
            if name in className:
                return obj


    # def print_ValueDomainClass(self, model):

    #     if(model is not None and inspect.isclass(type(model))):
    #         attrs = [ (key, value) for key, value in inspect.getmembers(model) 
    #             if (key not in dir(type('dummy', (object,), {}))) 
    #             and not (key.startswith('_') or key.endswith('_')) 
    #         ]

    #         for key, value in attrs:
    #             print(str(key) + ': ' + str(value))


    # def print_ValueListDomainClass(self, listmodel):

    #     if(listmodel is not None):
    #         for item in listmodel:
    #             print('#'*40)
    #             self.print_ValueDomainClass(item)


    def map_JsonToAnDomainClass(self, modelClass, obj):

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

       