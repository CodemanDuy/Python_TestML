import os, sys

ROOT_DIR = os.getcwd()  # Get root directory
sys.path.append(os.path.dirname(ROOT_DIR + r'/'))# Add absolute path to current sys.path
# print("Root Directory:", ROOT_DIR)
# print('Path: ' + str(sys.path))


from core_utils.util_common import Core_UtilityCommon
from core_utils.util_data import Core_UtilityData

from domains.domain_container import DomainContainer
from config import Configuration

"""
doc: Service class to process logic
"""
class BaseService():

    Config = Configuration()

    def __init__(self):
        pass

    def DomainContainer(self):
        return DomainContainer()
    
    def UtilCommon(self):
        return Core_UtilityCommon()

    def UtilData(self):
        return Core_UtilityData()


        



