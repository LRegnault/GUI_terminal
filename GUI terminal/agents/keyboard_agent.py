from agents.agent import Agent

import time
from typing import List, Dict
import threading
from pynput import keyboard

class KeyboardAgent(Agent):
	def __init__(self, action_delay, action_list, key_pointer, key_pressed_event_pointer: List[threading.Event], action_mapping: Dict, action_builder):
		self.key_pointer = key_pointer
		self.key_pressed_event_pointer = key_pressed_event_pointer
		self.action_mapping = action_mapping
		self.action_builder = action_builder

		self.final_action_processed = False
		self.current_action = {}

		super().__init__(action_delay, action_list)
	
	def selectAction(self):
		while not self.close_event.is_set():
			if self.final_action_processed:
				action = self.action_builder(self.current_action)
				if action is not None:
					self.action_queue.push(action)
				self.final_action_processed = False
				self.current_action["action"] = None
			elif self.key_pressed_event_pointer[0].is_set():
				if type(self.key_pointer[0]) == keyboard.KeyCode:
					key = self.key_pointer[0].char
				else:
					key = self.key_pointer[0]
				if key in self.action_mapping.keys():
					action = self.action_mapping[key]
					if action[0] == "final":
						self.final_action_processed = True
						self.current_action["action"] = action[1]
					elif action[0] == "modifier":
						if not action[1] in self.current_action.keys():
							self.current_action[action[1]] = True
						else:
							self.current_action[action[1]] = not self.current_action[action[1]]
				self.key_pressed_event_pointer[0].clear()
			time.sleep(self.action_delay)