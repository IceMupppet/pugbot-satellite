from BluemixVoiceToText import BluemixVoiceToText
from MicrophoneControl import MicrophoneControl, SAMPLE_RATE

microphone_control = MicrophoneControl()
bluemix_vtt = BluemixVoiceToText(SAMPLE_RATE)


def send_to_bluemix(in_data, frame_count, time_info, status):
	bluemix_vtt.send_data(in_data)


def run():
	microphone_control.add_callback(send_to_bluemix)
	microphone_control.start()


if __name__ == '__main__':
	run()
	i = raw_input('push to close')
