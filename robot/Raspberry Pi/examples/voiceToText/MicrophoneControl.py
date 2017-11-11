import pyaudio

# 44100Hz, Mono, UInt16, LittleEndian
SAMPLE_RATE = 44100
CHANNELS = 1
WIDTH = 2


class MicrophoneControl:
	"""
	Handles configuring a Microphone and returning data that works well for Bluemix
	"""

	def __init__(self):
		self.__pyAudio = pyaudio.PyAudio()
		self.__callbacks = []
		self.__stream = None

	def start(self):
		"""
		Starts recording from the default microphone
		:return:
		"""
		if self.__stream is None:
			self.__stream = self.__pyAudio.open(
				format=pyaudio.get_format_from_width(WIDTH),
				channels=CHANNELS,
				rate=SAMPLE_RATE,
				input=True,
				stream_callback=self.__handle_audio_data
			)
			self.__stream.start_stream()

	def stop(self):
		"""
		Stops the microphone stream
		:return:
		"""
		if self.__stream is not None:
			self.__stream.stop_stream()
			self.__stream.close()
			self.__stream = None

	def add_callback(self, callback):
		"""
		Adds a callback for when microphone data comes back

		Callbacks should take:
			input data
			the number of audio frames
			whatever "time_info" is from the microphone
			whatever the "status" is from the microphone

		ex: callback(in_data, frame_count, time_info, status)

		:param callback: the callback to add
		:return:
		"""
		self.__callbacks.append(callback)

	def remove_callback(self, callback):
		"""
		Removes the previously added callback
		:param callback: the callback to remove
		:return:
		"""
		self.__callbacks.remove(callback)

	def __handle_audio_data(self, in_data, frame_count, time_info, status):
		"""
		Handle audio data coming in
		:param in_data: the data that we received
		:param frame_count: how many frames we got
		:param time_info: timing info for the frame
		:param status: the current status of the audio
		:return:
		"""
		for callback in self.__callbacks:
			callback(in_data, frame_count, time_info, status)
		return in_data, pyaudio.paContinue
