"""
Controls:
	modifiers:
		toggle wide moves: shift
		toggle double moves: control
		toggle counterclowise moves: alt
	actions:
		rotate top face: u
		rotate front face (on the left in isometric view): f
		rotate right face: r
		rotate left face: l
		rotate back face: b
		rotate bottom face: d
		
		rotate cube around x axis (through center of right and left faces): x
		rotate cube around y axis (through center of top and bottom faces): y
		rotate cube around z axis (through center of front and back faces): z

The cube will be scrambled automatically shortly after resolution
The modifier indicators on the right of the screen light up when the related modifier is toggled on

The 2 digits between the isometric and top-down views show the number of moves required to reache the
solved state from the current state according to the selected heuristic
Currently, an implementation of the manhattan distance is used. However, this heuristic is not well
fitted for this problem and its estimation should be disregarded
"""


from utils.display import Display
from utils.data_structures import Queue
import utils.text as text
from programs.cube.heuristics.manhattan3d import cubeManhattan3dHeuristic as manhattan
from programs.cube.heuristics.cube_pattern_heuristics import cube3x3PatternHeuristic as pattern
from programs.cube.cubes.cube3x3 import Cube3x3
from agents.agent import Agent
from agents.keyboard_agent import KeyboardAgent

from heuristics.pattern_database import generateDatabase
from programs.cube.cubes.cube import Cube
from programs.cube.cubes.cube1x1 import Cube1x1

import time
from typing import List, Dict
import threading
from pynput import keyboard
import random

class App:
	def __init__(self, display_pointer: List[Display], agent_pointer: List[Agent]):
		self.display_pointer = display_pointer
		self.agent_pointer = agent_pointer
		self.cube = Cube3x3()

		self.color_dict = {
			"bg" : (0, 0, 0),
			"info" : (128, 128, 128),
			"active" : (128, 128, 0)
		}

		self.close_event = threading.Event()
		self.mainloop_thread = threading.Thread(target=self.mainloop, daemon=True)
		self.mainloop_thread.start()
		# pattern(self.cube)

	def mainloop(self):
		for pixel in self.display_pointer[0].pixel_data.keys():
			self.display_pointer[0].pixel_data[pixel] = self.color_dict["bg"]
		self.cube.drawIsometric(self.display_pointer, init=True)
		self.cube.drawTopdown(self.display_pointer, padx=22, pady=8, init=True)
		self.scramble(30)
		while not self.close_event.is_set():
			if self.cube.isSolved():
				time.sleep(5)
				self.scramble(30)
			try:
				if not self.agent_pointer[0].action_queue.isEmpty():
					action = self.agent_pointer[0].action_queue.pop()
					self.cube.apply(action)
					self.cube.drawIsometric(self.display_pointer)
					self.cube.drawTopdown(self.display_pointer, padx=22, pady=8)
				
				if type(self.agent_pointer[0]) is KeyboardAgent:
					if not self.agent_pointer[0].final_action_processed:
						self.drawInfo()
				time.sleep(1 / self.display_pointer[0].refresh_rate)
			except KeyboardInterrupt:
				break
		
	def drawInfo(self):
		text.c_upper(self.display_pointer, padx=19, pady=1, color=self.color_dict["info"])
		text.u_upper(self.display_pointer, padx=24, pady=1, color=self.color_dict["info"])
		text.b_upper(self.display_pointer, padx=29, pady=1, color=self.color_dict["info"])
		text.e_upper(self.display_pointer, padx=34, pady=1, color=self.color_dict["info"])

		current_move = self.agent_pointer[0].current_action
		keys = current_move.keys()
		wide_color = "info"
		prime_color = "info"
		double_color = "info"
		if "wide" in keys:
			if current_move["wide"]:
				wide_color = "active"
		if "prime" in keys:
			if current_move["prime"]:
				prime_color = "active"
		if "double" in keys:
			if current_move["double"]:
				double_color = "active"
		
		text.w_upper(self.display_pointer, padx=32, pady=6, color=self.color_dict[wide_color])
		text.num_2(self.display_pointer, padx=34, pady=12, color=self.color_dict[double_color])
		text.comma(self.display_pointer, padx=36, pady=15, color=self.color_dict[prime_color])

		dist = manhattan(self.cube.cube_array)
		# dist = pattern(self.cube)
		dist_str = str(dist)
		if len(dist_str) == 1:
			dist_str = "0" + dist_str
		tens = None
		units = None
		if dist_str[0] == "0":
			tens = text.num_0
		elif dist_str[0] == "1":
			tens = text.num_1
		elif dist_str[0] == "2":
			tens = text.num_2
		elif dist_str[0] == "3":
			tens = text.num_3
		elif dist_str[0] == "4":
			tens = text.num_4
		elif dist_str[0] == "5":
			tens = text.num_5
		elif dist_str[0] == "6":
			tens = text.num_6
		elif dist_str[0] == "7":
			tens = text.num_7
		elif dist_str[0] == "8":
			tens = text.num_8
		elif dist_str[0] == "9":
			tens = text.num_9

		if dist_str[1] == "0":
			units = text.num_0
		elif dist_str[1] == "1":
			units = text.num_1
		elif dist_str[1] == "2":
			units = text.num_2
		elif dist_str[1] == "3":
			units = text.num_3
		elif dist_str[1] == "4":
			units = text.num_4
		elif dist_str[1] == "5":
			units = text.num_5
		elif dist_str[1] == "6":
			units = text.num_6
		elif dist_str[1] == "7":
			units = text.num_7
		elif dist_str[1] == "8":
			units = text.num_8
		elif dist_str[1] == "9":
			units = text.num_9
		
		text.num_8(self.display_pointer, padx=19, pady=8)
		text.num_8(self.display_pointer, padx=19, pady=14)
		tens(self.display_pointer, padx=19, pady=8, color=self.color_dict["info"])
		units(self.display_pointer, padx=19, pady=14, color=self.color_dict["info"])
	
	def scramble(self, lenght):
		move_queue = Queue()
		move_list = ["U", "U'", "U2", "F", "F'", "F2", "R", "R'", "R2", "D", "D'", "D2", "B", "B'", "B2", "L", "L'", "L2"]
		rotation_list = ["x", "x'", "x2", "y", "y'", "y2", "z", "z'", "z2"]
		for i in range(lenght):
			move_queue.push(random.choice(move_list))
		for i in range(10):
			move_queue.push(random.choice(rotation_list))
		while not move_queue.isEmpty():
			self.cube.apply(move_queue.pop())
		self.cube.drawIsometric(self.display_pointer)
		self.cube.drawTopdown(self.display_pointer, padx=22, pady=8)

key_pointer = [None]
key_pressed_event_pointer = [threading.Event()]

def onPress(key):
	if key == keyboard.Key.esc:
		return False
	
	if not key_pressed_event_pointer[0].is_set():
		key_pointer[0] = key
		key_pressed_event_pointer[0].set()

def onRelease(key):
	pass

move_list = ["U", "U'", "U2", "u", "u'", "u2", "F", "F'", "F2", "f", "f'", "f2", "R", "R'", "R2", "r", "r'", "r2", "D", "D'", "D2", "d", "d'", "d2", "B", "B'", "B2", "b", "b'", "b2", "L", "L'", "L2", "l", "l'", "l2", "M", "M'", "M2", "E", "E'", "E2", "S", "S'", "S2", "x", "x'", "x2", "y", "y'", "y2", "z", "z'", "z2"]

action_map = {
	keyboard.Key.alt_l : ("modifier", "prime"),
	keyboard.Key.alt_r : ("modifier", "prime"),
	keyboard.Key.ctrl_l : ("modifier", "double"),
	keyboard.Key.ctrl_r : ("modifier", "double"),
	keyboard.Key.shift_l : ("modifier", "wide"),
	keyboard.Key.shift_r : ("modifier", "wide"),
	"u" : ("final", "u"),
	"f" : ("final", "f"),
	"r" : ("final", "r"),
	"d" : ("final", "d"),
	"b" : ("final", "b"),
	"l" : ("final", "l"),
	"m" : ("final", "m"),
	"e" : ("final", "e"),
	"s" : ("final", "s"),
	"x" : ("final", "x"),
	"y" : ("final", "y"),
	"z" : ("final", "z")
}

def moveBuilder(elements: Dict):
	keys = elements.keys()

	if not "action" in keys:
		return None
	else:
		move = elements["action"]
	
	if not "prime" in keys:
		is_prime = False
	else:
		is_prime = elements["prime"]
	
	if not "double" in keys:
		is_double = False
	else:
		is_double = elements["double"]
	
	if not "wide" in keys:
		is_wide = False
	else:
		is_wide = elements["wide"]
	
	if is_prime and is_double:
		return None

	if move == "u":
		if is_wide:
			if is_prime:
				return "u'"
			elif is_double:
				return "u2"
			else:
				return "u"
		else:
			if is_prime:
				return "U'"
			elif is_double:
				return "U2"
			else:
				return "U"

	elif move == "f":
		if is_wide:
			if is_prime:
				return "f'"
			elif is_double:
				return "f2"
			else:
				return "f"
		else:
			if is_prime:
				return "F'"
			elif is_double:
				return "F2"
			else:
				return "F"

	elif move == "r":
		if is_wide:
			if is_prime:
				return "r'"
			elif is_double:
				return "r2"
			else:
				return "r"
		else:
			if is_prime:
				return "R'"
			elif is_double:
				return "R2"
			else:
				return "R"

	elif move == "d":
		if is_wide:
			if is_prime:
				return "d'"
			elif is_double:
				return "d2"
			else:
				return "d"
		else:
			if is_prime:
				return "D'"
			elif is_double:
				return "D2"
			else:
				return "D"

	elif move == "b":
		if is_wide:
			if is_prime:
				return "b'"
			elif is_double:
				return "b2"
			else:
				return "b"
		else:
			if is_prime:
				return "B'"
			elif is_double:
				return "B2"
			else:
				return "B"

	elif move == "l":
		if is_wide:
			if is_prime:
				return "l'"
			elif is_double:
				return "l2"
			else:
				return "l"
		else:
			if is_prime:
				return "L'"
			elif is_double:
				return "L2"
			else:
				return "L"

	elif move == "m":
		if is_prime:
			return "M'"
		elif is_double:
			return "M2"
		else:
			return "M"

	elif move == "e":
		if is_prime:
			return "E'"
		elif is_double:
			return "E2"
		else:
			return "E"

	elif move == "s":
		if is_prime:
			return "S'"
		elif is_double:
			return "S2"
		else:
			return "S"

	elif move == "x":
		if is_prime:
			return "x'"
		elif is_double:
			return "x2"
		else:
			return "x"

	elif move == "y":
		if is_prime:
			return "y'"
		elif is_double:
			return "y2"
		else:
			return "y"

	elif move == "z":
		if is_prime:
			return "z'"
		elif is_double:
			return "z2"
		else:
			return "z"

def run():
	width = 18 + 20
	height = 21
	scale = 1
	ratio = (2, 1)
	refresh_rate = 60

	display_pointer = [Display(width, height, scale, ratio, refresh_rate)]

	agent = KeyboardAgent(0.1, move_list, key_pointer, key_pressed_event_pointer, action_map, moveBuilder)
	agent_pointer = [agent]

	app = App(display_pointer, agent_pointer)

	with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
		listener.join()