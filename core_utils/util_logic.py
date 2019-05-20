
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
            print("Formula Equation: y = {0}x + {1}".format(slope, intercept))
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

    def calPolynomialRegressionOfY(self, lstSampleValueX, lstSampleValueY, xVal):
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
            sumXX = sum([x1 * x2 for (x1, x2) in zip(lstSpX, lstSpX)])
            sumXXX = sum([x1 * x2 * x3 for (x1, x2, x3) in zip(lstSpX, lstSpX, lstSpX)])
            sumXXXX = sum([x1 * x2 * x3 * x4 for (x1, x2, x3, x4) in zip(lstSpX, lstSpX, lstSpX, lstSpX)])
            sumXXY = sum([x1 * x2 * y for (x1, x2, y) in zip(lstSpX, lstSpX, lstSpY)])

            #the more list of value X and Y passed in, the more calculation for coefficients be matched
            coefficientA = (sumXXY * sumXX - sumXY * sumXXX) / (sumXX * sumXXXX - pow(sumXXX, 2))
            coefficientB = (sumXY * sumXXXX - sumXXY * sumXXX) / (sumXX * sumXXXX - pow(sumXXX, 2))
            coefficientC = (sumY/numberOfVal) - (coefficientB * (sumX/numberOfVal)) - (coefficientA * (sumXX/numberOfVal))

            #calculate approximate Y value (predict Y) for specific X value by quadratic equation: y = ax^2 + bx + c
            print("Formula Equation: y = {0}x^2 + {1}x + {2}".format(coefficientA, coefficientB, coefficientC))
            equationResult = coefficientA*pow(xVal, 2) + coefficientB*xVal + coefficientC

            return equationResult

        except ValueError as ex:
            print('Error: ', ex)
        
        return 0
