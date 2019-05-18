# Facade Pattern
"""
doc: Model class with the decorator
"""
class ConfigApiModel(object):
    """
    A data descriptor that sets and returns values normally and optional prints a message logging their access.
    """
    def __init__(self):
        pass


    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, val):
        self.__type = val

    @property
    def api_name(self):
        return self.__api_name
    @api_name.setter
    def api_name(self, val):
        self.__api_name = val

    @property
    def site_name(self):
        return self.__site_name
    @site_name.setter
    def site_name(self, val):
        self.__site_name = val


    @property
    def api_host(self):
        return self.__api_host
    @api_host.setter
    def api_host(self, val):
        self.__api_host = val


    @property
    def api_path(self):
        return self.__api_path
    @api_path.setter
    def api_path(self, val):
        self.__api_path = val

    
    @property
    def api_extension(self):
        return self.__api_extension
    @api_extension.setter
    def api_extension(self, val):
        self.__api_extension = val

    @property
    def api_queries(self):
        return self.__api_queries
    @api_queries.setter
    def api_queries(self, val):
        self.__api_queries = val
