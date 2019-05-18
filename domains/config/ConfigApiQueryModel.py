# Facade Pattern
"""
doc: Model class with the decorator
"""
class ConfigApiQueryModel(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass


    @property
    def param_name(self):
        return self.__param_name
    @param_name.setter
    def param_name(self, val):
        self.__param_name = val


    @property
    def param_defvalue(self):
        return self.__param_defvalue
    @param_defvalue.setter
    def param_defvalue(self, val):
        self.__param_defvalue = val

    @property
    def param_curvalue(self):
        return self.__param_curvalue
    @param_curvalue.setter
    def param_curvalue(self, val):
        self.__param_curvalue = val

