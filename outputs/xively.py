import output
import requests
import json

class Xively(output.Output):
	"""
	This class takes 2 required values to be initialized, your Xively account API key,
	and your feed ID.
	"""
	requiredData = ["APIKey","FeedID"]
	optionalData = []

	def __init__(self,data):
		self.APIKey=data["APIKey"]
		self.FeedID=data["FeedID"]

	def outputData(self,dataPoints):
		"""
		The outputData method takes a list of dictionaries which have at least the following
		keys: 'name' and 'value', which are converted to a json object along with some metadata
		about the current version. The result is a dictionary of dictionaries pattern which is 
		sent using a PUT request to the xively using the feed id and api key that are associated
		with this Xively instance. If successfull the method returns True, else if there is an 
		error with the request the method will return False, and print an error message if instance
		comes from there.
		"""
		arr = []
		for data_point in dataPoints:
			arr.append({"id":data_point["name"], "current_value":data_point["value"]})
		json_data = json.dumps({"version":"1.0.0", "datastreams":arr})
		try:
			xively_request = requests.put("https://api.xively.com/v2/feeds/" + self.FeedID + ".json", headers = {"X-ApiKey":self.APIKey}, data = json_data)
			if xively_request.text != "": 
				print "Xively Error: " + xively_request.text
				return False
		except Exception:
			return False
		return True
