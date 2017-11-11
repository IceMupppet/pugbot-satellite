from Tkconstants import END, S, E, W, N
from Tkinter import Frame, Label, Button, PanedWindow, Listbox
import tkFileDialog

from BluemixVoiceToText import BluemixVoiceToText
from MicrophoneControl import MicrophoneControl, SAMPLE_RATE

__author__ = 'Pux0r3'


class MicrophoneFrame(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid(sticky=(N, W, E, S))
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

		self.grid_rowconfigure(3, weight=1)

		self.__title = Label(self)
		self.__title["text"] = "Microphone Test"
		self.__title.grid(row=0, columnspan=2, sticky=(N, W, E))

		self.__record = Button(self, command=self.__record_clicked)
		self.__record["text"] = "Record"
		self.__record.grid(row=1, column=0, sticky=(N, W, E))

		self.__save_button = Button(self, command=self.__save_clicked, text="Save")
		self.__save_button.grid(row=1, column=1, sticky=(N, W, E))
		self.__save_file_name = None
		self.__output_file = None

		self.__is_recording = False

		self.__result = Label(self)
		self.__result["text"] = "No Results"
		self.__result.grid(row=2, columnspan=2, sticky=(N, W, E))

		self.__microphone = MicrophoneControl()
		self.__microphone.add_callback(self.__write_file_callback)
		self.__microphone.add_callback(self.__send_to_tts_callback)

		self.__voice_to_text_service = BluemixVoiceToText(SAMPLE_RATE)
		self.__voice_to_text_service.add_received_text_listener(self.__vtt_listener)

		self.__last_result = []
		self.__results_dic = {}

		self.__results_paned_window = PanedWindow(self)
		self.__results_paned_window.grid(row=3, columnspan=2, sticky=(N, S, W, E))

		self.__results_list = Listbox(self.__results_paned_window)
		self.__results_list.bind('<<ListboxSelect>>', self.__listbox_selection_changed)
		self.__results_paned_window.add(self.__results_list)

		self.__results_desc = Label(text="Selected Result")
		self.__results_paned_window.add(self.__results_desc)

	def __record_clicked(self):
		if self.__is_recording:
			self.stop_recording()
		else:
			self.start_recording()

	def stop_recording(self):
		self.__record["text"] = "Record"
		self.__microphone.stop()
		if self.__output_file is not None:
			self.__output_file.flush()
			self.__output_file.close()
			self.__output_file = None
		self.__is_recording = False

	def start_recording(self):
		self.__record["text"] = "Stop Recording"
		if self.__save_file_name is not None:
			self.__output_file = open(self.__save_file_name, 'wb')
		self.__microphone.start()
		self.__is_recording = True

	def __save_clicked(self):
		self.__save_file_name = tkFileDialog.asksaveasfilename(defaultextension="RAW", title="Open File")

	def __write_file_callback(self, in_data, frame_count, time_info, status):
		if self.__output_file is not None:
			self.__output_file.write(in_data)

	def __send_to_tts_callback(self, in_data, frame_count, time_info, status):
		self.__voice_to_text_service.send_data(in_data)

	def __vtt_listener(self, speech_result, final_results):
		if speech_result is None:
			final_string = 'No Result'
		else:
			self.__set_last_result(speech_result)
			if final_results:
				self.__save_result(speech_result)

			strings = list(speech_result.get_results())
			strings.append('Final? %s' % final_results)
			final_string = '\n'.join(strings)

		self.__result['text'] = final_string

	def __set_last_result(self, speech_result):
		self.__last_result = speech_result

	def __save_result(self, speech_result):
		self.__results_dic[speech_result.get_id()] = speech_result
		self.__results_list.delete(0, END)
		for key in self.__results_dic.keys():
			current_result = self.__results_dic[key]
			self.__results_list.insert(
				END,
				'{0}> {1}'.format(current_result.get_id(), current_result.get_default_result()))

	def __listbox_selection_changed(self, evt):
		widget = evt.widget
		index = int(widget.curselection()[0])
		key = self.__results_dic.keys()[index]
		self.__results_desc['text'] = '\n'.join(self.__results_dic[key].get_results())
