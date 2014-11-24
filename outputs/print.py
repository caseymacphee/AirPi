import output
import datetime

class Print(output.Output):
	"""
	This class is built for the main method 'outputData' which takes a list of dictionairies that
	contain at least the three keys 'name', 'value', and 'symbol'. The values are then printed
	to the console. If a key value error is raised on the datapoint, the method will return False.

	"""
	requiredData = []
	optionalData = []

	def __init__(self, data):
		pass	
	def outputData(self,dataPoints):
		print "Time: " + str(datetime.datetime.now())
		for data_point in dataPoints:
			try:
				print data_point["name"] + ": " + str(data_point["value"]) + " " + data_point["symbol"]
			except:
				return False
		return True
