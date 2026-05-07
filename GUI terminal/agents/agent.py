from utils.data_structures import Queue

import threading

class Agent:
	def __init__(self, action_delay, action_list):
		self.action_delay = action_delay
		self.action_list = action_list
		self.action_queue = Queue()

		self.close_event = threading.Event()
		self.controller_thread = threading.Thread(target=self.selectAction, daemon=True)
		self.controller_thread.start()
	
	def close(self):
		self.close_event.set()