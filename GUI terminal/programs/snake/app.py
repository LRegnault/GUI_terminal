from utils.display import Display
from agents.keyboard_agent import KeyboardAgent

import threading
from pynput import keyboard
import time
import random

class App:
	def __init__(self, display_pointer):
		self.display_pointer = display_pointer
		self.position_pointer = [(0, 0)]
		self.food_position_pointer = [None]
		self.spawnFood()

		self.close_event = threading.Event()

		self.agent_key_pressed_event_pointer = [threading.Event()]
		self.agent_key_pointer = [None]
		self.agent_controls = {"up" : keyboard.Key.up, "down" : keyboard.Key.down, "left" : keyboard.Key.left, "right" : keyboard.Key.right}
		self.food_key_pressed_event_pointer = [threading.Event()]
		self.food_key_pointer = [None]
		self.food_controls = {"up" : "w", "down" : "s", "left" : "a", "right" : "d"}

		self.agent = KeyboardAgent(display_pointer, self.position_pointer, self.agent_key_pointer, self.agent_key_pressed_event_pointer, 0.1, (0, 0, 1))
		self.food = KeyboardAgent(display_pointer, self.food_position_pointer, self.food_key_pointer, self.food_key_pressed_event_pointer, 0.1, (0, 0, 1), self.food_controls)
		self.color_dict = {
			"void" : (0, 0, 0),
			"head" : (255, 0, 0),
			"body" : (0, 255, 0),
			"food" : (0, 0, 255)
		}

		self.main_loop_thread = threading.Thread(target=self.mainLoop, daemon=True)
		self.main_loop_thread.start()

		with keyboard.Listener(on_press=self.onPress, on_release=self.onRelease) as listener:
			listener.join()
		
	def mainLoop(self):
		while not self.close_event.is_set():
			# print(f"\x1b[H\x1b[J{self.position_pointer[0]}\n{self.food_position_pointer[0]}\n{self.agent_key_pointer[0]}\n{self.food_key_pointer[0]}")
			for x, y in self.display_pointer[0].pixel_data.keys():
				if (x, y) == self.position_pointer[0]:
					self.display_pointer[0].pixel_data[(x, y)] = self.color_dict["head"]
					if (x, y) == self.food_position_pointer[0]:
						self.spawnFood()
				elif (x, y) == self.food_position_pointer[0]:
					self.display_pointer[0].pixel_data[(x, y)] = self.color_dict["food"]
				else:
					self.display_pointer[0].pixel_data[(x, y)] = (0, 0, 0)
			if not self.foodExists():
				self.spawnFood()
			time.sleep(1 / self.display_pointer[0].refresh_rate)
	
	def foodExists(self):
		return self.food_position_pointer[0] is not None
	
	def spawnFood(self):
		# if not self.foodExists():
			self.food_position_pointer[0] = (random.randint(0, self.display_pointer[0].width - 1), random.randint(0, self.display_pointer[0].height - 1))
	
	def onPress(self, key):
		if key == keyboard.Key.esc:
			self.display_pointer[0].close()
			self.agent.close()
			self.food.close()
			self.close_event.set()
			return False
		
		try:
			if not self.agent_key_pressed_event_pointer[0].is_set() and (key in self.agent_controls.values() or key.char in self.agent_controls.values()):
				self.agent_key_pointer[0] = key
				self.agent_key_pressed_event_pointer[0].set()

			elif not self.food_key_pressed_event_pointer[0].is_set() and (key in self.food_controls.values() or key.char in self.food_controls.values()):
				self.food_key_pointer[0] = key.char
				self.food_key_pressed_event_pointer[0].set()
		except AttributeError:
			pass

	def onRelease(self, key):
		pass

def run():
	try:
		width = 30
		height = 15
		scale = 2
		ratio = (2, 1)
		frame_rate = 30

		display_pointer = [Display(width, height, scale, ratio, frame_rate)]
		app = App(display_pointer)
	except KeyboardInterrupt:
		pass