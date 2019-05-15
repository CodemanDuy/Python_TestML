import urllib
import json
import urllib.request

class Core_UtilityData():

    def __init__(self):
        pass

    def readJsonFromFile(self, path):        
        file = open(path, encoding='utf-8')
        content = json.load(file)
        file.close()
        return content

    def readJsonFromUrl(self, url):
        with urllib.request.urlopen(url) as data:
            content = json.loads(data.read().decode())
            return content


