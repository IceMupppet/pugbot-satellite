import json
import thread

import requests as requests
import websocket

from SpeechResult import SpeechResult

__author__ = 'Pux0r3'

PRODUCTION_SERVER = 'http://spherowatsontestapp.mybluemix.net'
APP_PATH = '/spherowatsontestapp/v1/apps/ac4c1bcc-dc8c-4418-83f8-e808925320e4'
TOKEN_API = '/token'

WATSON_API_BASE = 'wss://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
WATSON_TOKEN = '?watson-token='
WATSON_MODEL = '&model=en-US_BroadbandModel'


class BluemixVoiceToText:
	"""
	Takes audio in uint16 LE format and writes it out to a websocket
	"""

	def __init__(self, bitrate):
		"""
		:param bitrate: the bitrate to record at
		:return:
		"""
		self.__callbacks = []

		self.__bitrate = bitrate
		self.__token = self.__renew_token()

		self.__socket_ready = False
		self.__listening = False

		self.__web_socket = websocket.WebSocketApp(
			WATSON_API_BASE + WATSON_TOKEN + self.__token + WATSON_MODEL,
			on_message=self.__on_message,
			on_error=self.__on_error,
			on_close=self.__on_close,
			on_open=self.__on_open
		)
		thread.start_new_thread(self.__web_socket.run_forever, ())

	@staticmethod
	def __renew_token():
		"""
		Renews the token for the web voice recognition
		:return: the token generated for web voice recognition
		"""
		request = requests.get(PRODUCTION_SERVER + APP_PATH + TOKEN_API)
		return request.text

	def __on_message(self, ws, message):
		"""
		Handles a message coming in from the websocket
		:param ws: the web socket that received a message
		:param message: the message that was received
		:return:
		"""
		parsed_message = json.loads(message)
		print('received: ' + message)
		if 'state' in parsed_message:
			state = parsed_message['state']
			if state == 'listening':
				self.__listening = True
			else:
				self.__listening = False

		if 'results' in parsed_message:
			# TODO: pass this in!
			result_index = 0
			if 'result_index' in parsed_message:
				result_index = parsed_message['result_index']

			results = parsed_message['results'][0]
			final_results = False
			if 'final' in results:
				final_results = results['final']
			alternatives = []
			if 'alternatives' in results:
				alternatives = results['alternatives']

			transcripts = [self.__get_transcript_from_alternative(alternative) for alternative in alternatives]
			speech_result = SpeechResult(transcripts, result_index)

			for callback in self.__callbacks:
				callback(speech_result, final_results)

	def __on_error(self, ws, error):
		"""
		Handles an error coming in via the websocket
		:param ws: the web socket that received an error
		:param error: the error that was received
		:return:
		"""
		self.__web_socket.close()
		print('Received error:' + error)

	def __on_close(self, ws):
		"""
		Handles the websocket closing
		:param ws: the websocket that closed
		:return:
		"""
		self.__socket_ready = False
		print('Closed Connection')

	def __on_open(self, ws):
		"""
		Handles the websocket opening
		:param ws: the websocket that opened
		:return:
		"""
		print('Connection Opened')
		self.__socket_ready = True
		bitrate_string = "audio/l16;rate=%d" % self.__bitrate
		json_dict = {
			'action': 'start',
			'content-type': bitrate_string,
			'interim_results': True,
			'continuous': True,
			'max_alternatives': 3
		}
		salutation = json.dumps(json_dict)
		ws.send(salutation)
		print('sending salutation!:%s' % salutation)

	def send_data(self, data):
		"""
		Sends data via the websocket to the server
		:param data: binary data, should be uint16 formatted in little endian
		:return:
		"""
		if self.__socket_ready:
			self.__web_socket.send(data, opcode=websocket.ABNF.OPCODE_BINARY)

	def add_received_text_listener(self, callback):
		"""
		Adds a listener that is raised when we receive text from the server

		The callback should take a SpeechResult and a boolean indicating that it's the final result
		ex: def callback(speech_result, is_final)

		:param callback: the callback to add
		:return:
		"""
		self.__callbacks.append(callback)

	def remove_received_text_listener(self, callback):
		"""
		Removes a previously added callback
		:param callback: the callback to remove
		:return:
		"""
		self.__callbacks.remove(callback)

	@staticmethod
	def __get_transcript_from_alternative(alternative):
		"""
		Given an "alternative" from the JSON server response, retrieves the actual transcript text
		:param alternative: the alternative to extract a transcript from
		:return:
		"""
		if 'transcript' in alternative:
			return alternative['transcript']
		return None
