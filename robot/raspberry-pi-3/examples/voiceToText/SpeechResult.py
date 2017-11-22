__author__ = 'Pux0r3'


class SpeechResult:
	"""
	A result from the speech engine
	"""

	def __init__(self, results, response_id):
		"""
		Creates a new SpeechResult given data from the server
		:param results: a list of results from the server
		:param response_id: an identifier for this result
		:return:
		"""
		self.__results = results
		self.__id = response_id

	def get_results(self):
		"""
		Get the results that have been stored in this object
		:return: a list of the results
		"""
		return self.__results

	def get_id(self):
		"""
		Gets the unique identifier for this instance
		:return: the identifier for this speech result
		"""
		return self.__id

	def get_default_result(self):
		"""
		Gets the default (preferred) result
		:return: the default (preferred) result
		"""
		if (self.__results is None) or (len(self.__results) <= 0):
			return None
		return self.__results[0]
