from Tkinter import Tk

from MicrophoneFrame import MicrophoneFrame

__author__ = 'Pux0r3'


def run():
	root = Tk()
	app = MicrophoneFrame(master=root)

	root.grid_columnconfigure(0, weight=1)
	root.grid_rowconfigure(0, weight=1)
	root.wm_resizable(True, True)

	app.mainloop()

if __name__ == '__main__':
	run()
