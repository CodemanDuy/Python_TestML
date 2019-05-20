
class Core_UtilityLogic():


    def __init__(self):
        pass

    def calTotalSumOfSeries(self, lstValue):
        try:
            if lstValue and len(lstValue) > 0:
                return sum(lstValue)
        except ValueError as ex:
            print('Error: ', ex)
        
        return 0

    
    def calLinearRegressionOfY(self, lstSampleValueX, lstSampleValueY, xVal):
        try:
            lstSpX = 0
            lstSpY = 0

            if lstSampleValueX and len(lstSampleValueX) > 0:
                lstSpX = lstSampleValueX
            if lstSampleValueY and len(lstSampleValueY) > 0:
                lstSpY = lstSampleValueY
            
            numberOfVal = (len(lstSpX) > len(lstSpY)) and len(lstSpX) or len(lstSpY) 
            sumX = self.calTotalSumOfSeries(lstSpX)
            sumY = self.calTotalSumOfSeries(lstSpY)
            sumXY = sum([x * y for (x, y) in zip(lstSpX, lstSpY)])
            sumXX = sum([x * y for (x, y) in zip(lstSpX, lstSpX)])

            #the more list of value X and Y passed in, the more calculation for accurate slope and intercept be matched
            slope = (numberOfVal*sumXY - sumX*sumY) / (numberOfVal*sumXX - pow(sumX,2))            
            intercept = (sumY - slope*sumX) / numberOfVal

            #calculate approximate Y value (predict Y) for specific X value by regression equation: y = a + bx            
            equationResult = intercept + slope*xVal

            return equationResult

        except ValueError as ex:
            print('Error: ', ex)
        
        return 0

    def calLinearRegressionOfListY(self, lstSampleValueX, lstSampleValueY, lstXVal):
        try:
            if lstXVal and len(lstXVal) > 0:
                lstYVal = []
                for x in lstXVal:
                    y = self.calLinearRegressionOfY(lstSampleValueX, lstSampleValueY, x)
                    lstYVal.append(y)

                return lstYVal

        except ValueError as ex:
            print('Error: ', ex)
        
        return None

