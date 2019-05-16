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
    def site_domain(self):
        return self.__site_domain
    @site_domain.setter
    def site_domain(self, val):
        self.__site_domain = val


    @property
    def api_url(self):
        return self.__api_url
    @api_url.setter
    def api_url(self, val):
        self.__api_url = val

    
    @property
    def api_extension(self):
        return self.__api_extension
    @api_extension.setter
    def api_extension(self, val):
        self.__api_extension = val

    @property
    def api_params(self):
        return self.__api_params
    @api_params.setter
    def api_params(self, val):
        self.__api_params = val
