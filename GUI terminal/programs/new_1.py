import os
import threading
import time
import random
import math

from pynput import keyboard

os.system("")

class Display:
	def __init__(self, width, height, scale, ratio, refresh_rate):
		os.system(f"mode {width * scale * ratio[0]},{height * scale * ratio[1]}")
		print("\x1b[?25l", end="")
		self.width = width
		self.height = height
		self.scale = scale
		self.ratio = ratio
		self.refresh_rate = refresh_rate
		self.pixel_data = {}
		
		for y in range(self.height):
			for x in range(self.width):
				 self.pixel_data[(x, y)] = (0, 0, 0)
		
		self.refresh_thread = threading.Thread(target=self.refresh, daemon=True)
		self.refresh_thread.start()
		
		string = "\x1b[H\x1b[J\x1b[48;2;0;0;0m"
		for i in range(self.height * self.scale * self.ratio[1]):
			string += " " * self.width * self.scale * self.ratio[0]
			string += "\n"
		string += "\x1b[m"
		print(string, end="")
	
	def update(self):
		string = "\x1b[H\x1b[J"
		for y in range(self.height * self.scale * self.ratio[1]):
			for x in range(self.width):
				r = self.pixel_data[(x, y // (self.scale * self.ratio[1]))][0]
				g = self.pixel_data[(x, y // (self.scale * self.ratio[1]))][1]
				b = self.pixel_data[(x, y // (self.scale * self.ratio[1]))][2]
				string += f"\x1b[48;2;{r};{g};{b}m"
				string += " " * self.scale * self.ratio[0]
		string += "\x1b[m"
		print(string, end="")
	
	def updatePixel(self, x, y, r, g, b):
		self.pixel_data[(x, y)] = (r, g, b)
	
	def refresh(self):
		while not close_event.is_set():
			self.update()
			time.sleep(1 / self.refresh_rate)

maze_color_dict = {"wall" : (0, 0, 0), "tile" : (255, 255, 255), "agent" : (255, 0, 0), "goal" : (0, 255, 0), "visited_tile" : (255, 200, 200), "explored_tile" : (200, 200, 255)}
position_pointer = [(0, 0)]
agent_pointer = [None]

def generateMaze(display_pointer):
	c_wall = maze_color_dict["wall"]
	c_tile = maze_color_dict["tile"]
	c_agent = maze_color_dict["agent"]
	c_goal = maze_color_dict["goal"]
	
	def maze(size):
		if size == 1:
			return [[c_tile, c_wall], [c_wall, c_wall]]
		elif size % 2 != 0:
			raise ValueError
		else:
			array = maze(size // 2)
			result = []
			for i in range(2):
				for line in array:
					line_result = []
					for j in range(2):
						for cell in line:
							line_result.append(cell)
					result.append(line_result)
			center = ((len(result) - 1) // 2, (len(result) - 1) // 2)
			left = []
			right = []
			up = []
			down = []
			for y in range(len(result) - 1):
				for x in range(len(result) - 1):
					if (x, y) == center:
						continue
					if x == center[0] and y < center[1] and y % 2 == 0:
						up.append((x, y))
					elif x == center[0] and y > center[1] and y % 2 == 0:
						down.append((x, y))
					elif x < center[0] and y == center[1] and x % 2 == 0:
						left.append((x, y))
					elif x > center[0] and y == center[1] and x % 2 == 0:
						right.append((x, y))
			choices = [left, right, up, down]
			choices.remove(random.choice(choices))
			for side in choices:
				x, y = random.choice(side)
				result[y][x] = c_tile
			return result
	
	m = maze(display_pointer[0].height // 2)
	m[0][0] = c_agent
	position_pointer[0] = (0, 0)
	if agent_pointer[0] != None:
		agent_pointer[0].position = (0, 0)
	m[(len(m) - 2)][(len(m) - 2)] = c_goal
	
	for y in range(len(m)):
		for x in range(len(m[y])):
			display_pointer[0].pixel_data[(x, y)] = m[y][x]

def generateMaze8x8(display_pointer):
	if display_pointer[0].height != 16 or display_pointer[0].width != 16:
		generateMaze(display_pointer)
		return
	
	c_wall = maze_color_dict["wall"]
	c_tile = maze_color_dict["tile"]
	c_agent = maze_color_dict["agent"]
	c_goal = maze_color_dict["goal"]
	
	maze = [[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall],
			[c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall, c_tile, c_wall],
			[c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall, c_wall]]
	
	
	bit_sequence_1 = generateBitSequence(16)
	bit_sequence_2 = generateBitSequence(16)
	bit_sequence_3 = generateBitSequence(16)
	bit_sequence_4 = generateBitSequence(16)
	
	if bit_sequence_1[0] == 0 and bit_sequence_1[1] == 0:
		maze[1][0] = c_tile
		maze[1][2] = c_tile
		maze[2][1] = c_tile
	elif bit_sequence_1[0] == 0 and bit_sequence_1[1] == 1:
		maze[0][1] = c_tile
		maze[1][0] = c_tile
		maze[2][1] = c_tile
	elif bit_sequence_1[0] == 1 and bit_sequence_1[1] == 0:
		maze[0][1] = c_tile
		maze[1][0] = c_tile
		maze[1][2] = c_tile
	elif bit_sequence_1[0] == 1 and bit_sequence_1[1] == 1:
		maze[0][1] = c_tile
		maze[1][2] = c_tile
		maze[2][1] = c_tile
	
	if bit_sequence_1[2] == 0 and bit_sequence_1[3] == 0:
		maze[1][4] = c_tile
		maze[1][6] = c_tile
		maze[2][5] = c_tile
	elif bit_sequence_1[2] == 0 and bit_sequence_1[3] == 1:
		maze[0][5] = c_tile
		maze[1][4] = c_tile
		maze[2][5] = c_tile
	elif bit_sequence_1[2] == 1 and bit_sequence_1[3] == 0:
		maze[0][5] = c_tile
		maze[1][4] = c_tile
		maze[1][6] = c_tile
	elif bit_sequence_1[2] == 1 and bit_sequence_1[3] == 1:
		maze[0][5] = c_tile
		maze[1][6] = c_tile
		maze[2][5] = c_tile
	
	if bit_sequence_1[4] == 0 and bit_sequence_1[5] == 0:
		maze[5][0] = c_tile
		maze[5][2] = c_tile
		maze[6][1] = c_tile
	elif bit_sequence_1[4] == 0 and bit_sequence_1[5] == 1:
		maze[4][1] = c_tile
		maze[5][0] = c_tile
		maze[6][1] = c_tile
	elif bit_sequence_1[4] == 1 and bit_sequence_1[5] == 0:
		maze[4][1] = c_tile
		maze[5][0] = c_tile
		maze[5][2] = c_tile
	elif bit_sequence_1[4] == 1 and bit_sequence_1[5] == 1:
		maze[4][1] = c_tile
		maze[5][2] = c_tile
		maze[6][1] = c_tile
	
	if bit_sequence_1[6] == 0 and bit_sequence_1[7] == 0:
		maze[5][4] = c_tile
		maze[5][6] = c_tile
		maze[6][5] = c_tile
	elif bit_sequence_1[6] == 0 and bit_sequence_1[7] == 1:
		maze[4][5] = c_tile
		maze[5][4] = c_tile
		maze[6][5] = c_tile
	elif bit_sequence_1[6] == 1 and bit_sequence_1[7] == 0:
		maze[4][5] = c_tile
		maze[5][4] = c_tile
		maze[5][6] = c_tile
	elif bit_sequence_1[6] == 1 and bit_sequence_1[7] == 1:
		maze[4][5] = c_tile
		maze[5][6] = c_tile
		maze[6][5] = c_tile
	
	if bit_sequence_1[8] == 0 and bit_sequence_1[9] == 0:
		maze[1][8] = c_tile
		maze[1][10] = c_tile
		maze[2][9] = c_tile
	elif bit_sequence_1[8] == 0 and bit_sequence_1[9] == 1:
		maze[0][9] = c_tile
		maze[1][8] = c_tile
		maze[2][9] = c_tile
	elif bit_sequence_1[8] == 1 and bit_sequence_1[9] == 0:
		maze[0][9] = c_tile
		maze[1][8] = c_tile
		maze[1][10] = c_tile
	elif bit_sequence_1[8] == 1 and bit_sequence_1[9] == 1:
		maze[0][9] = c_tile
		maze[1][10] = c_tile
		maze[2][9] = c_tile
	
	if bit_sequence_1[10] == 0 and bit_sequence_1[11] == 0:
		maze[1][12] = c_tile
		maze[1][14] = c_tile
		maze[2][13] = c_tile
	elif bit_sequence_1[10] == 0 and bit_sequence_1[11] == 1:
		maze[0][13] = c_tile
		maze[1][12] = c_tile
		maze[2][13] = c_tile
	elif bit_sequence_1[10] == 1 and bit_sequence_1[11] == 0:
		maze[0][13] = c_tile
		maze[1][12] = c_tile
		maze[1][14] = c_tile
	elif bit_sequence_1[10] == 1 and bit_sequence_1[11] == 1:
		maze[0][13] = c_tile
		maze[1][14] = c_tile
		maze[2][13] = c_tile
	
	if bit_sequence_1[12] == 0 and bit_sequence_1[13] == 0:
		maze[5][8] = c_tile
		maze[5][10] = c_tile
		maze[6][9] = c_tile
	elif bit_sequence_1[12] == 0 and bit_sequence_1[13] == 1:
		maze[4][9] = c_tile
		maze[5][8] = c_tile
		maze[6][9] = c_tile
	elif bit_sequence_1[12] == 1 and bit_sequence_1[13] == 0:
		maze[4][9] = c_tile
		maze[5][8] = c_tile
		maze[5][10] = c_tile
	elif bit_sequence_1[12] == 1 and bit_sequence_1[13] == 1:
		maze[4][9] = c_tile
		maze[5][10] = c_tile
		maze[6][9] = c_tile
	
	if bit_sequence_1[14] == 0 and bit_sequence_1[15] == 0:
		maze[5][12] = c_tile
		maze[5][14] = c_tile
		maze[6][13] = c_tile
	elif bit_sequence_1[14] == 0 and bit_sequence_1[15] == 1:
		maze[4][13] = c_tile
		maze[5][12] = c_tile
		maze[6][13] = c_tile
	elif bit_sequence_1[14] == 1 and bit_sequence_1[15] == 0:
		maze[4][13] = c_tile
		maze[5][12] = c_tile
		maze[5][14] = c_tile
	elif bit_sequence_1[14] == 1 and bit_sequence_1[15] == 1:
		maze[4][13] = c_tile
		maze[5][14] = c_tile
		maze[6][13] = c_tile
	
	if bit_sequence_2[0] == 0 and bit_sequence_2[1] == 0:
		maze[9][0] = c_tile
		maze[9][2] = c_tile
		maze[10][1] = c_tile
	elif bit_sequence_2[0] == 0 and bit_sequence_2[1] == 1:
		maze[8][1] = c_tile
		maze[9][0] = c_tile
		maze[10][1] = c_tile
	elif bit_sequence_2[0] == 1 and bit_sequence_2[1] == 0:
		maze[8][1] = c_tile
		maze[9][0] = c_tile
		maze[9][2] = c_tile
	elif bit_sequence_2[0] == 1 and bit_sequence_2[1] == 1:
		maze[8][1] = c_tile
		maze[9][2] = c_tile
		maze[10][1] = c_tile
	
	if bit_sequence_2[2] == 0 and bit_sequence_2[3] == 0:
		maze[9][4] = c_tile
		maze[9][6] = c_tile
		maze[10][5] = c_tile
	elif bit_sequence_2[2] == 0 and bit_sequence_2[3] == 1:
		maze[8][5] = c_tile
		maze[9][4] = c_tile
		maze[10][5] = c_tile
	elif bit_sequence_2[2] == 1 and bit_sequence_2[3] == 0:
		maze[8][5] = c_tile
		maze[9][4] = c_tile
		maze[9][6] = c_tile
	elif bit_sequence_2[2] == 1 and bit_sequence_2[3] == 1:
		maze[8][5] = c_tile
		maze[9][6] = c_tile
		maze[10][5] = c_tile
	
	if bit_sequence_2[4] == 0 and bit_sequence_2[5] == 0:
		maze[13][0] = c_tile
		maze[13][2] = c_tile
		maze[14][1] = c_tile
	elif bit_sequence_2[4] == 0 and bit_sequence_2[5] == 1:
		maze[12][1] = c_tile
		maze[13][0] = c_tile
		maze[14][1] = c_tile
	elif bit_sequence_2[4] == 1 and bit_sequence_2[5] == 0:
		maze[12][1] = c_tile
		maze[13][0] = c_tile
		maze[13][2] = c_tile
	elif bit_sequence_2[4] == 1 and bit_sequence_2[5] == 1:
		maze[12][1] = c_tile
		maze[13][2] = c_tile
		maze[14][1] = c_tile
	
	if bit_sequence_2[6] == 0 and bit_sequence_2[7] == 0:
		maze[13][4] = c_tile
		maze[13][6] = c_tile
		maze[14][5] = c_tile
	elif bit_sequence_2[6] == 0 and bit_sequence_2[7] == 1:
		maze[12][5] = c_tile
		maze[13][4] = c_tile
		maze[14][5] = c_tile
	elif bit_sequence_2[6] == 1 and bit_sequence_2[7] == 0:
		maze[12][5] = c_tile
		maze[13][4] = c_tile
		maze[13][6] = c_tile
	elif bit_sequence_2[6] == 1 and bit_sequence_2[7] == 1:
		maze[12][5] = c_tile
		maze[13][6] = c_tile
		maze[14][5] = c_tile
	
	if bit_sequence_2[8] == 0 and bit_sequence_2[9] == 0:
		maze[9][8] = c_tile
		maze[9][10] = c_tile
		maze[10][9] = c_tile
	elif bit_sequence_2[8] == 0 and bit_sequence_2[9] == 1:
		maze[8][9] = c_tile
		maze[9][8] = c_tile
		maze[10][9] = c_tile
	elif bit_sequence_2[8] == 1 and bit_sequence_2[9] == 0:
		maze[8][9] = c_tile
		maze[9][8] = c_tile
		maze[9][10] = c_tile
	elif bit_sequence_2[8] == 1 and bit_sequence_2[9] == 1:
		maze[8][9] = c_tile
		maze[9][10] = c_tile
		maze[10][9] = c_tile
	
	if bit_sequence_2[10] == 0 and bit_sequence_2[11] == 0:
		maze[9][12] = c_tile
		maze[9][14] = c_tile
		maze[10][13] = c_tile
	elif bit_sequence_2[10] == 0 and bit_sequence_2[11] == 1:
		maze[8][13] = c_tile
		maze[9][12] = c_tile
		maze[10][13] = c_tile
	elif bit_sequence_2[10] == 1 and bit_sequence_2[11] == 0:
		maze[8][13] = c_tile
		maze[9][12] = c_tile
		maze[9][14] = c_tile
	elif bit_sequence_2[10] == 1 and bit_sequence_2[11] == 1:
		maze[8][13] = c_tile
		maze[9][14] = c_tile
		maze[10][13] = c_tile
	
	if bit_sequence_2[12] == 0 and bit_sequence_2[13] == 0:
		maze[13][8] = c_tile
		maze[13][10] = c_tile
		maze[14][9] = c_tile
	elif bit_sequence_2[12] == 0 and bit_sequence_2[13] == 1:
		maze[12][9] = c_tile
		maze[13][8] = c_tile
		maze[14][9] = c_tile
	elif bit_sequence_2[12] == 1 and bit_sequence_2[13] == 0:
		maze[12][9] = c_tile
		maze[13][8] = c_tile
		maze[13][10] = c_tile
	elif bit_sequence_2[12] == 1 and bit_sequence_2[13] == 1:
		maze[12][9] = c_tile
		maze[13][10] = c_tile
		maze[14][9] = c_tile
	
	if bit_sequence_2[14] == 0 and bit_sequence_2[15] == 0:
		maze[13][12] = c_tile
		maze[13][14] = c_tile
		maze[14][13] = c_tile
	elif bit_sequence_2[14] == 0 and bit_sequence_2[15] == 1:
		maze[12][13] = c_tile
		maze[13][12] = c_tile
		maze[14][13] = c_tile
	elif bit_sequence_2[14] == 1 and bit_sequence_2[15] == 0:
		maze[12][13] = c_tile
		maze[13][12] = c_tile
		maze[13][14] = c_tile
	elif bit_sequence_2[14] == 1 and bit_sequence_2[15] == 1:
		maze[12][13] = c_tile
		maze[13][14] = c_tile
		maze[14][13] = c_tile
	
	if bit_sequence_3[0] == 0 and bit_sequence_3[1] == 0:
		if bit_sequence_3[2] == 0:
			maze[3][6] = c_tile
		elif bit_sequence_3[2] == 1:
			maze[3][4] = c_tile
		
		if bit_sequence_3[3] == 0:
			maze[6][3] = c_tile
		elif bit_sequence_3[3] == 1:
			maze[4][3] = c_tile
		
		if bit_sequence_3[4] == 0:
			maze[3][0] = c_tile
		elif bit_sequence_3[4] == 1:
			maze[3][2] = c_tile
	
	elif bit_sequence_3[0] == 0 and bit_sequence_3[1] == 1:
		if bit_sequence_3[2] == 0:
			maze[0][3] = c_tile
		elif bit_sequence_3[2] == 1:
			maze[2][3] = c_tile
		
		if bit_sequence_3[3] == 0:
			maze[6][3] = c_tile
		elif bit_sequence_3[3] == 1:
			maze[4][3] = c_tile
		
		if bit_sequence_3[4] == 0:
			maze[3][0] = c_tile
		elif bit_sequence_3[4] == 1:
			maze[3][2] = c_tile
	
	elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 0:
		if bit_sequence_3[2] == 0:
			maze[0][3] = c_tile
		elif bit_sequence_3[2] == 1:
			maze[2][3] = c_tile
		
		if bit_sequence_3[3] == 0:
			maze[3][6] = c_tile
		elif bit_sequence_3[3] == 1:
			maze[3][4] = c_tile
		
		if bit_sequence_3[4] == 0:
			maze[3][0] = c_tile
		elif bit_sequence_3[4] == 1:
			maze[3][2] = c_tile
	
	elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 1:
		if bit_sequence_3[2] == 0:
			maze[0][3] = c_tile
		elif bit_sequence_3[2] == 1:
			maze[2][3] = c_tile
		
		if bit_sequence_3[3] == 0:
			maze[3][6] = c_tile
		elif bit_sequence_3[3] == 1:
			maze[3][4] = c_tile
		
		if bit_sequence_3[4] == 0:
			maze[6][3] = c_tile
		elif bit_sequence_3[4] == 1:
			maze[4][3] = c_tile
	
	if bit_sequence_3[5] == 0 and bit_sequence_3[6] == 0:
		if bit_sequence_3[7] == 0:
			maze[3][14] = c_tile
		elif bit_sequence_3[7] == 1:
			maze[3][12] = c_tile
		
		if bit_sequence_3[8] == 0:
			maze[6][11] = c_tile
		elif bit_sequence_3[8] == 1:
			maze[4][11] = c_tile
		
		if bit_sequence_3[9] == 0:
			maze[3][8] = c_tile
		elif bit_sequence_3[9] == 1:
			maze[3][10] = c_tile
	
	elif bit_sequence_3[5] == 0 and bit_sequence_3[6] == 1:
		if bit_sequence_3[7] == 0:
			maze[0][11] = c_tile
		elif bit_sequence_3[7] == 1:
			maze[2][11] = c_tile
		
		if bit_sequence_3[8] == 0:
			maze[6][11] = c_tile
		elif bit_sequence_3[8] == 1:
			maze[4][11] = c_tile
		
		if bit_sequence_3[9] == 0:
			maze[3][8] = c_tile
		elif bit_sequence_3[9] == 1:
			maze[3][10] = c_tile
	
	elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 0:
		if bit_sequence_3[7] == 0:
			maze[0][11] = c_tile
		elif bit_sequence_3[7] == 1:
			maze[2][11] = c_tile
		
		if bit_sequence_3[8] == 0:
			maze[3][14] = c_tile
		elif bit_sequence_3[8] == 1:
			maze[3][12] = c_tile
		
		if bit_sequence_3[9] == 0:
			maze[3][8] = c_tile
		elif bit_sequence_3[9] == 1:
			maze[3][10] = c_tile
	
	elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 1:
		if bit_sequence_3[7] == 0:
			maze[0][11] = c_tile
		elif bit_sequence_3[7] == 1:
			maze[2][11] = c_tile
		
		if bit_sequence_3[8] == 0:
			maze[3][14] = c_tile
		elif bit_sequence_3[8] == 1:
			maze[3][12] = c_tile
		
		if bit_sequence_3[9] == 0:
			maze[6][11] = c_tile
		elif bit_sequence_3[9] == 1:
			maze[4][11] = c_tile
	
	if bit_sequence_3[10] == 0 and bit_sequence_3[11] == 0:
		if bit_sequence_3[12] == 0:
			maze[11][6] = c_tile
		elif bit_sequence_3[12] == 1:
			maze[11][4] = c_tile
		
		if bit_sequence_3[13] == 0:
			maze[14][3] = c_tile
		elif bit_sequence_3[13] == 1:
			maze[12][3] = c_tile
		
		if bit_sequence_3[14] == 0:
			maze[11][0] = c_tile
		elif bit_sequence_3[14] == 1:
			maze[11][2] = c_tile
	
	elif bit_sequence_3[10] == 0 and bit_sequence_3[11] == 1:
		if bit_sequence_3[12] == 0:
			maze[8][3] = c_tile
		elif bit_sequence_3[12] == 1:
			maze[10][3] = c_tile
		
		if bit_sequence_3[13] == 0:
			maze[14][3] = c_tile
		elif bit_sequence_3[13] == 1:
			maze[12][3] = c_tile
		
		if bit_sequence_3[14] == 0:
			maze[11][0] = c_tile
		elif bit_sequence_3[14] == 1:
			maze[11][2] = c_tile
	
	elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 0:
		if bit_sequence_3[12] == 0:
			maze[8][3] = c_tile
		elif bit_sequence_3[12] == 1:
			maze[10][3] = c_tile
		
		if bit_sequence_3[13] == 0:
			maze[11][6] = c_tile
		elif bit_sequence_3[13] == 1:
			maze[11][4] = c_tile
		
		if bit_sequence_3[14] == 0:
			maze[11][0] = c_tile
		elif bit_sequence_3[14] == 1:
			maze[11][2] = c_tile
	
	elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 1:
		if bit_sequence_3[12] == 0:
			maze[8][3] = c_tile
		elif bit_sequence_3[12] == 1:
			maze[10][3] = c_tile
		
		if bit_sequence_3[13] == 0:
			maze[11][6] = c_tile
		elif bit_sequence_3[13] == 1:
			maze[11][4] = c_tile
		
		if bit_sequence_3[14] == 0:
			maze[14][3] = c_tile
		elif bit_sequence_3[14] == 1:
			maze[12][3] = c_tile
	
	if bit_sequence_4[0] == 0 and bit_sequence_4[1] == 0:
		if bit_sequence_4[2] == 0:
			maze[11][14] = c_tile
		elif bit_sequence_4[2] == 1:
			maze[11][12] = c_tile
		
		if bit_sequence_4[3] == 0:
			maze[14][11] = c_tile
		elif bit_sequence_4[3] == 1:
			maze[12][11] = c_tile
		
		if bit_sequence_4[4] == 0:
			maze[11][8] = c_tile
		elif bit_sequence_4[4] == 1:
			maze[11][10] = c_tile
	
	elif bit_sequence_4[0] == 0 and bit_sequence_4[1] == 1:
		if bit_sequence_4[2] == 0:
			maze[8][11] = c_tile
		elif bit_sequence_4[2] == 1:
			maze[10][11] = c_tile
		
		if bit_sequence_4[3] == 0:
			maze[14][11] = c_tile
		elif bit_sequence_4[3] == 1:
			maze[12][11] = c_tile
		
		if bit_sequence_4[4] == 0:
			maze[11][8] = c_tile
		elif bit_sequence_4[4] == 1:
			maze[11][10] = c_tile
	
	elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 0:
		if bit_sequence_4[2] == 0:
			maze[8][11] = c_tile
		elif bit_sequence_4[2] == 1:
			maze[10][11] = c_tile
		
		if bit_sequence_4[3] == 0:
			maze[11][14] = c_tile
		elif bit_sequence_4[3] == 1:
			maze[11][12] = c_tile
		
		if bit_sequence_4[4] == 0:
			maze[11][8] = c_tile
		elif bit_sequence_4[4] == 1:
			maze[11][10] = c_tile
	
	elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 1:
		if bit_sequence_4[2] == 0:
			maze[8][11] = c_tile
		elif bit_sequence_4[2] == 1:
			maze[10][11] = c_tile
		
		if bit_sequence_4[3] == 0:
			maze[11][14] = c_tile
		elif bit_sequence_4[3] == 1:
			maze[11][12] = c_tile
		
		if bit_sequence_4[4] == 0:
			maze[14][11] = c_tile
		elif bit_sequence_4[4] == 1:
			maze[12][11] = c_tile
	
	if bit_sequence_4[8] == 0 and bit_sequence_4[9] == 0:
		if bit_sequence_4[10] == 0 and bit_sequence_4[11] == 0:
			maze[7][14] = c_tile
		elif bit_sequence_4[10] == 0 and bit_sequence_4[11] == 1:
			maze[7][12] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 0:
			maze[7][10] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 1:
			maze[7][8] = c_tile
		
		if bit_sequence_4[12] == 0 and bit_sequence_4[13] == 0:
			maze[14][7] = c_tile
		elif bit_sequence_4[12] == 0 and bit_sequence_4[13] == 1:
			maze[12][7] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 0:
			maze[10][7] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 1:
			maze[8][7] = c_tile
		
		if bit_sequence_4[14] == 0 and bit_sequence_4[15] == 0:
			maze[7][0] = c_tile
		elif bit_sequence_4[14] == 0 and bit_sequence_4[15] == 1:
			maze[7][2] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 0:
			maze[7][4] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 1:
			maze[7][6] = c_tile
	
	elif bit_sequence_4[8] == 0 and bit_sequence_4[9] == 1:
		if bit_sequence_4[10] == 0 and bit_sequence_4[11] == 0:
			maze[0][7] = c_tile
		elif bit_sequence_4[10] == 0 and bit_sequence_4[11] == 1:
			maze[2][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 0:
			maze[4][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 1:
			maze[6][7] = c_tile
		
		if bit_sequence_4[12] == 0 and bit_sequence_4[13] == 0:
			maze[14][7] = c_tile
		elif bit_sequence_4[12] == 0 and bit_sequence_4[13] == 1:
			maze[12][7] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 0:
			maze[10][7] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 1:
			maze[8][7] = c_tile
		
		if bit_sequence_4[14] == 0 and bit_sequence_4[15] == 0:
			maze[7][0] = c_tile
		elif bit_sequence_4[14] == 0 and bit_sequence_4[15] == 1:
			maze[7][2] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 0:
			maze[7][4] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 1:
			maze[7][6] = c_tile
	
	elif bit_sequence_4[8] == 1 and bit_sequence_4[9] == 0:
		if bit_sequence_4[10] == 0 and bit_sequence_4[11] == 0:
			maze[0][7] = c_tile
		elif bit_sequence_4[10] == 0 and bit_sequence_4[11] == 1:
			maze[2][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 0:
			maze[4][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 1:
			maze[6][7] = c_tile
		
		if bit_sequence_4[12] == 0 and bit_sequence_4[13] == 0:
			maze[7][14] = c_tile
		elif bit_sequence_4[12] == 0 and bit_sequence_4[13] == 1:
			maze[7][12] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 0:
			maze[7][10] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 1:
			maze[7][8] = c_tile
		
		if bit_sequence_4[14] == 0 and bit_sequence_4[15] == 0:
			maze[7][0] = c_tile
		elif bit_sequence_4[14] == 0 and bit_sequence_4[15] == 1:
			maze[7][2] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 0:
			maze[7][4] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 1:
			maze[7][6] = c_tile
	
	elif bit_sequence_4[8] == 1 and bit_sequence_4[9] == 1:
		if bit_sequence_4[10] == 0 and bit_sequence_4[11] == 0:
			maze[0][7] = c_tile
		elif bit_sequence_4[10] == 0 and bit_sequence_4[11] == 1:
			maze[2][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 0:
			maze[4][7] = c_tile
		elif bit_sequence_4[10] == 1 and bit_sequence_4[11] == 1:
			maze[6][7] = c_tile
		
		if bit_sequence_4[12] == 0 and bit_sequence_4[13] == 0:
			maze[7][14] = c_tile
		elif bit_sequence_4[12] == 0 and bit_sequence_4[13] == 1:
			maze[7][12] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 0:
			maze[7][10] = c_tile
		elif bit_sequence_4[12] == 1 and bit_sequence_4[13] == 1:
			maze[7][8] = c_tile
		
		if bit_sequence_4[14] == 0 and bit_sequence_4[15] == 0:
			maze[14][7] = c_tile
		elif bit_sequence_4[14] == 0 and bit_sequence_4[15] == 1:
			maze[12][7] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 0:
			maze[10][7] = c_tile
		elif bit_sequence_4[14] == 1 and bit_sequence_4[15] == 1:
			maze[8][7] = c_tile
	
	end_points = [[-1, -1, -1], [-1, -1, -1]]
	colors = [c_agent, c_goal]
	
	if bit_sequence_4[8] == 0 and bit_sequence_4[9] == 0:
		end_points[0][0] = 0
		end_points[1][0] = 1
	elif bit_sequence_4[8] == 0 and bit_sequence_4[9] == 1:
		end_points[0][0] = 5
		end_points[1][0] = 7
	elif bit_sequence_4[8] == 1 and bit_sequence_4[9] == 0:
		end_points[0][0] = 2
		end_points[1][0] = 3
	elif bit_sequence_4[8] == 1 and bit_sequence_4[9] == 1:
		end_points[0][0] = 4
		end_points[1][0] = 6
	
	for end_point in end_points:
		if end_point[0] == 0:
			if bit_sequence_3[0] == 0 and bit_sequence_3[1] == 0 and bit_sequence_4[14] == 0:
				end_point[1] = 1
			elif bit_sequence_3[0] == 0 and bit_sequence_3[1] == 0 and bit_sequence_4[14] == 1:
				end_point[1] = 0
			elif bit_sequence_3[0] == 0 and bit_sequence_3[1] == 1:
				end_point[1] = 5
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 0 and bit_sequence_4[14] == 0:
				end_point[1] = 3
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 0 and bit_sequence_4[14] == 1:
				end_point[1] = 2
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 1:
				end_point[1] = 4
		
		elif end_point[0] == 1:
			if bit_sequence_3[5] == 0 and bit_sequence_3[6] == 0 and bit_sequence_4[10] == 0:
				end_point[1] = 0
			elif bit_sequence_3[5] == 0 and bit_sequence_3[6] == 0 and bit_sequence_4[10] == 1:
				end_point[1] = 1
			elif bit_sequence_3[5] == 0 and bit_sequence_3[6] == 1:
				end_point[1] = 5
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 0 and bit_sequence_4[10] == 0:
				end_point[1] = 2
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 0 and bit_sequence_4[10] == 1:
				end_point[1] = 3
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 1:
				end_point[1] = 4
		
		elif end_point[0] == 2:
			if bit_sequence_3[10] == 0 and bit_sequence_3[11] == 0 and bit_sequence_4[14] == 0:
				end_point[1] = 1
			elif bit_sequence_3[10] == 0 and bit_sequence_3[11] == 0 and bit_sequence_4[14] == 1:
				end_point[1] = 0
			elif bit_sequence_3[10] == 0 and bit_sequence_3[11] == 1:
				end_point[1] = 7
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 0 and bit_sequence_4[14] == 0:
				end_point[1] = 3
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 0 and bit_sequence_4[14] == 1:
				end_point[1] = 2
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 1:
				end_point[1] = 6
		
		elif end_point[0] == 3:
			if bit_sequence_4[0] == 0 and bit_sequence_4[1] == 0 and bit_sequence_4[12] == 0:
				end_point[1] = 0
			elif bit_sequence_4[0] == 0 and bit_sequence_4[1] == 0 and bit_sequence_4[12] == 1:
				end_point[1] = 1
			elif bit_sequence_4[0] == 0 and bit_sequence_4[1] == 1:
				end_point[1] = 7
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 0 and bit_sequence_4[12] == 0:
				end_point[1] = 2
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 0 and bit_sequence_4[12] == 1:
				end_point[1] = 3
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 1:
				end_point[1] = 6
		
		elif end_point[0] == 4:
			if bit_sequence_3[0] == 0 and bit_sequence_3[1] == 0:
				end_point[1] = 0
			elif bit_sequence_3[0] == 0 and bit_sequence_3[1] == 1 and bit_sequence_4[10] == 0:
				end_point[1] = 7
			elif bit_sequence_3[0] == 0 and bit_sequence_3[1] == 1 and bit_sequence_4[10] == 1:
				end_point[1] = 5
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 0:
				end_point[1] = 2
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 1 and bit_sequence_4[10] == 0:
				end_point[1] = 6
			elif bit_sequence_3[0] == 1 and bit_sequence_3[1] == 1 and bit_sequence_4[10] == 1:
				end_point[1] = 4
		
		elif end_point[0] == 5:
			if bit_sequence_3[5] == 0 and bit_sequence_3[6] == 0:
				end_point[1] = 1
			elif bit_sequence_3[5] == 0 and bit_sequence_3[6] == 1 and bit_sequence_4[10] == 0:
				end_point[1] = 7
			elif bit_sequence_3[5] == 0 and bit_sequence_3[6] == 1 and bit_sequence_4[10] == 1:
				end_point[1] = 5
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 0:
				end_point[1] = 3
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 1 and bit_sequence_4[10] == 0:
				end_point[1] = 6
			elif bit_sequence_3[5] == 1 and bit_sequence_3[6] == 1 and bit_sequence_4[10] == 1:
				end_point[1] = 4
		
		elif end_point[0] == 6:
			if bit_sequence_3[10] == 0 and bit_sequence_3[11] == 0:
				end_point[1] = 0
			elif bit_sequence_3[10] == 0 and bit_sequence_3[11] == 1 and bit_sequence_4[14] == 0:
				end_point[1] = 5
			elif bit_sequence_3[10] == 0 and bit_sequence_3[11] == 1 and bit_sequence_4[14] == 1:
				end_point[1] = 7
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 0:
				end_point[1] = 2
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 1 and bit_sequence_4[14] == 0:
				end_point[1] = 4
			elif bit_sequence_3[10] == 1 and bit_sequence_3[11] == 1 and bit_sequence_4[14] == 1:
				end_point[1] = 6
		
		elif end_point[0] == 7:
			if bit_sequence_4[0] == 0 and bit_sequence_4[1] == 0:
				end_point[1] = 1
			elif bit_sequence_4[0] == 0 and bit_sequence_4[1] == 1 and bit_sequence_4[12] == 0:
				end_point[1] = 5
			elif bit_sequence_4[0] == 0 and bit_sequence_4[1] == 1 and bit_sequence_4[12] == 1:
				end_point[1] = 7
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 0:
				end_point[1] = 3
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 1 and bit_sequence_4[12] == 0:
				end_point[1] = 4
			elif bit_sequence_4[0] == 1 and bit_sequence_4[1] == 1 and bit_sequence_4[12] == 1:
				end_point[1] = 6
		
		seq = []
		offset = -1
		connections = []
		if end_point[0] in [0, 4]:
			seq = bit_sequence_1
			offset = 0
			connections = [bit_sequence_3[2], bit_sequence_3[3], bit_sequence_3[4]]
		elif end_point[0] in [1, 5]:
			seq = bit_sequence_1
			offset = 8
			connections = [bit_sequence_3[7], bit_sequence_3[8], bit_sequence_3[9]]
		elif end_point[0] in [2, 6]:
			seq = bit_sequence_2
			offset = 0
			connections = [bit_sequence_3[12], bit_sequence_3[13], bit_sequence_3[14]]
		elif end_point[0] in [3, 7]:
			seq = bit_sequence_2
			offset = 8
			connections = [bit_sequence_4[2], bit_sequence_4[3], bit_sequence_4[4]]
		
		if end_point[1] == 0:
			if seq[0 + offset] == 0 and seq[1 + offset] == 0 and connections[2] == 0:
				end_point[2] = 1
			elif seq[0 + offset] == 0 and seq[1 + offset] == 0 and connections[2] == 1:
				end_point[2] = 0
			elif seq[0 + offset] == 0 and seq[1 + offset] == 1:
				end_point[2] = 1
			elif seq[0 + offset] == 1 and seq[1 + offset] == 0 and connections[2] == 0:
				end_point[2] = 3
			elif seq[0 + offset] == 1 and seq[1 + offset] == 0 and connections[2] == 1:
				end_point[2] = 2
			elif seq[0 + offset] == 1 and seq[1 + offset] == 1:
				end_point[2] = 0
		
		elif end_point[1] == 1:
			if seq[2 + offset] == 0 and seq[3 + offset] == 0 and connections[0] == 0:
				end_point[2] = 0
			elif seq[2 + offset] == 0 and seq[3 + offset] == 0 and connections[0] == 1:
				end_point[2] = 1
			elif seq[2 + offset] == 0 and seq[3 + offset] == 1:
				end_point[2] = 1
			elif seq[2 + offset] == 1 and seq[3 + offset] == 0 and connections[0] == 0:
				end_point[2] = 2
			elif seq[2 + offset] == 1 and seq[3 + offset] == 0 and connections[0] == 1:
				end_point[2] = 3
			elif seq[2 + offset] == 1 and seq[3 + offset] == 1:
				end_point[2] = 0
		
		elif end_point[1] == 2:
			if seq[4 + offset] == 0 and seq[5 + offset] == 0 and connections[2] == 0:
				end_point[2] = 1
			elif seq[4 + offset] == 0 and seq[5 + offset] == 0 and connections[2] == 1:
				end_point[2] = 0
			elif seq[4 + offset] == 0 and seq[5 + offset] == 1:
				end_point[2] = 3
			elif seq[4 + offset] == 1 and seq[5 + offset] == 0 and connections[2] == 0:
				end_point[2] = 3
			elif seq[4 + offset] == 1 and seq[5 + offset] == 0 and connections[2] == 1:
				end_point[2] = 2
			elif seq[4 + offset] == 1 and seq[5 + offset] == 1:
				end_point[2] = 2
		
		elif end_point[1] == 3:
			if seq[6 + offset] == 0 and seq[7 + offset] == 0 and connections[1] == 0:
				end_point[2] = 0
			elif seq[6 + offset] == 0 and seq[7 + offset] == 0 and connections[1] == 1:
				end_point[2] = 1
			elif seq[6 + offset] == 0 and seq[7 + offset] == 1:
				end_point[2] = 3
			elif seq[6 + offset] == 1 and seq[7 + offset] == 0 and connections[1] == 0:
				end_point[2] = 2
			elif seq[6 + offset] == 1 and seq[7 + offset] == 0 and connections[1] == 1:
				end_point[2] = 3
			elif seq[6 + offset] == 1 and seq[7 + offset] == 1:
				end_point[2] = 2
		
		elif end_point[1] == 4:
			if seq[0 + offset] == 0 and seq[1 + offset] == 0:
				end_point[2] = 0
			elif seq[0 + offset] == 0 and seq[1 + offset] == 1 and connections[0] == 0:
				end_point[2] = 3
			elif seq[0 + offset] == 0 and seq[1 + offset] == 1 and connections[0] == 1:
				end_point[2] = 1
			elif seq[0 + offset] == 1 and seq[1 + offset] == 0:
				end_point[2] = 2
			elif seq[0 + offset] == 1 and seq[1 + offset] == 1 and connections[0] == 0:
				end_point[2] = 2
			elif seq[0 + offset] == 1 and seq[1 + offset] == 1 and connections[0] == 1:
				end_point[2] = 0
		
		elif end_point[1] == 5:
			if seq[2 + offset] == 0 and seq[3 + offset] == 0:
				end_point[2] = 1
			elif seq[2 + offset] == 0 and seq[3 + offset] == 1 and connections[0] == 0:
				end_point[2] = 3
			elif seq[2 + offset] == 0 and seq[3 + offset] == 1 and connections[0] == 1:
				end_point[2] = 1
			elif seq[2 + offset] == 1 and seq[3 + offset] == 0:
				end_point[2] = 3
			elif seq[2 + offset] == 1 and seq[3 + offset] == 1 and connections[0] == 0:
				end_point[2] = 2
			elif seq[2 + offset] == 1 and seq[3 + offset] == 1 and connections[0] == 1:
				end_point[2] = 0
		
		elif end_point[1] == 6:
			if seq[4 + offset] == 0 and seq[5 + offset] == 0:
				end_point[2] = 0
			elif seq[4 + offset] == 0 and seq[5 + offset] == 1 and connections[2] == 0:
				end_point[2] = 1
			elif seq[4 + offset] == 0 and seq[5 + offset] == 1 and connections[2] == 1:
				end_point[2] = 3
			elif seq[4 + offset] == 1 and seq[5 + offset] == 0:
				end_point[2] = 2
			elif seq[4 + offset] == 1 and seq[5 + offset] == 1 and connections[2] == 0:
				end_point[2] = 0
			elif seq[4 + offset] == 1 and seq[5 + offset] == 1 and connections[2] == 1:
				end_point[2] = 2
		
		elif end_point[1] == 7:
			if seq[6 + offset] == 0 and seq[7 + offset] == 0:
				end_point[2] = 1
			elif seq[6 + offset] == 0 and seq[7 + offset] == 1 and connections[1] == 0:
				end_point[2] = 1
			elif seq[6 + offset] == 0 and seq[7 + offset] == 1 and connections[1] == 1:
				end_point[2] = 3
			elif seq[6 + offset] == 1 and seq[7 + offset] == 0:
				end_point[2] = 3
			elif seq[6 + offset] == 1 and seq[7 + offset] == 1 and connections[1] == 0:
				end_point[2] = 0
			elif seq[6 + offset] == 1 and seq[7 + offset] == 1 and connections[1] == 1:
				end_point[2] = 2
		
		if end_point[0] in [0, 4]:
			if end_point[1] in [0, 4]:
				if end_point[2] == 0:
					maze[0][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[0][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[2][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[2][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [1, 5]:
				if end_point[2] == 0:
					maze[0][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[0][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[2][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[2][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [2, 6]:
				if end_point[2] == 0:
					maze[4][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[4][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[6][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[6][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [3, 7]:
				if end_point[2] == 0:
					maze[4][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[4][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[6][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[6][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
		
		elif end_point[0] in [1, 5]:
			if end_point[1] in [0, 4]:
				if end_point[2] == 0:
					maze[0][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[0][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[2][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[2][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [1, 5]:
				if end_point[2] == 0:
					maze[0][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[0][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[2][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[2][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [2, 6]:
				if end_point[2] == 0:
					maze[4][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[4][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[6][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[6][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [3, 7]:
				if end_point[2] == 0:
					maze[4][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[4][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[6][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[6][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
		
		elif end_point[0] in [2, 6]:
			if end_point[1] in [0, 4]:
				if end_point[2] == 0:
					maze[8][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[8][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[10][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[10][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [1, 5]:
				if end_point[2] == 0:
					maze[8][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[8][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[10][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[10][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [2, 6]:
				if end_point[2] == 0:
					maze[12][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[12][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[14][0] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[14][2] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [3, 7]:
				if end_point[2] == 0:
					maze[12][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[12][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[14][4] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[14][6] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
		
		elif end_point[0] in [3, 7]:
			if end_point[1] in [0, 4]:
				if end_point[2] == 0:
					maze[8][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[8][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[10][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[10][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [1, 5]:
				if end_point[2] == 0:
					maze[8][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[8][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[10][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[10][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [2, 6]:
				if end_point[2] == 0:
					maze[12][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[12][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[14][8] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[14][10] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
			
			elif end_point[1] in [3, 7]:
				if end_point[2] == 0:
					maze[12][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 1:
					maze[12][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 2:
					maze[14][12] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
				elif end_point[2] == 3:
					maze[14][14] = colors[(end_points.index(end_point) + bit_sequence_4[6]) % 2]
	
	for y in range(len(maze)):
		for x in range(len(maze)):
			display_pointer[0].pixel_data[(x, y)] = maze[y][x]
			if maze[y][x] == c_agent:
				position_pointer[0] = (x, y)
				if agent_pointer[0] != None:
					agent_pointer[0].position = (x, y)


def generateBitSequence(n):
	vals = [0, 1]
	sequence = []
	for i in range(n):
		sequence.append(random.choice(vals))
	return sequence


key_pressed_event = threading.Event()
close_event = threading.Event()
test_event = threading.Event()
key_pointer = [None]

def victory(display_pointer):
	generateMaze8x8(display_pointer)
	if agent_pointer[0].type == "SearchAgent":
		agent_pointer[0].search()
	key_pressed_event.clear()

def onPress(key):
	if key == keyboard.Key.esc:
		return False
	if not key_pressed_event.is_set():
		# try:
		# 	print(f"alphanumeric key {key.char} pressed")
		# except AttributeError:
		# 	print(f"special key {key} pressed")
		key_pointer[0] = key
		key_pressed_event.set()

def onRelease(key):
	pass

def eventTest(display_pointer):
	while not close_event.is_set():
		if key_pressed_event.is_set():
			# print(f"key pressed: {key_pointer[0]}")
			display_pointer[0].pixel_data[position_pointer[0]] = (255, 255, 255)
			x, y = position_pointer[0]
			if key_pointer[0] == keyboard.Key.up:
				if y > 0:
					y -= 1
			elif key_pointer[0] == keyboard.Key.down:
				if y < 15:
					y += 1
			elif key_pointer[0] == keyboard.Key.left:
				if x > 0:
					x -= 1
			elif key_pointer[0] == keyboard.Key.right:
				if x < 15:
					x += 1
			
			if display_pointer[0].pixel_data[(x, y)] == (0, 255, 0):
				victory(display_pointer)
				continue
			if not display_pointer[0].pixel_data[(x, y)] == (0, 0, 0):
				position_pointer[0] = (x, y)
			display_pointer[0].pixel_data[position_pointer[0]] = (255, 0, 0)
			key_pressed_event.clear()
		time.sleep(0.1)


class Tree:
	class Node:
		def __init__(self, value):
			self.value = value
			self.childs = []
	
	def __init__(self):
		self.root = None
		self.nodes = []
	
	def getParent(self, node):
		for n in self.nodes:
			if node in n.childs:
				return n
	
	def addNode(self, node, parent):
		parent.childs.append(node)
		self.nodes.append(node)
	
	def removeNode(self, node):
		if len(node.childs) == 0:
			raise RuntimeError("Tree.removeNode: tried to remove non-leaf node")
		
		parent = self.getParent(node)
		return parent.childs.pop(parent.childs.index(node))

class Stack:
	def __init__(self):
		self.stack = []
	
	def size(self):
		return len(self.stack)
	
	def isEmpty(self):
		return self.size() == 0
	
	def push(self, item):
		self.stack.append(item)
	
	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Stack.pop(): stack is empty")
		return self.stack.pop()

class Queue:
	def __init__(self):
		self.input_stack = Stack()
		self.output_stack = Stack()
	
	def size(self):
		return self.input_stack.size() + self.output_stack.size()
	
	def isEmpty(self):
		return self.size() == 0
	
	def push(self, item):
		self.input_stack.push(item)
	
	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Queue.pop(): queue is empty")
		if self.output_stack.isEmpty():
			n = self.input_stack.size()
			for i in range(n):
				self.output_stack.push(self.input_stack.pop())
		return self.output_stack.pop()

class Heap:
	def __init__(self, comparison_function, low_root=True):
		self.compare = comparison_function
		self.low_root = low_root
		self.heap = []
	
	def size(self):
		return len(self.heap)
	
	def isEmpty(self):
		return self.size() == 0
	
	def height(self):
		pass
	
	def trickle(self):
		pass
	
	def sift(self):
		pass
	
	def addLeaf(self, item):
		self.heap.append(item)
		self.sift()
	
	def RemoveRoot(self):
		root = self.heap[0]
		self.trickle()
		return root

class PriorityQueue:
	def __init__(self, comparison_function):
		self.heap = Heap(comparison_function)
	
	def size(self):
		return self.heap.size()
	
	def isEmpty(self):
		return self.heap.isEmpty()
	
	def push(self, item):
		self.heap.addLeaf(item)
	
	def pop(self):
		return self.heap.RemoveRoot()


class Agent:
	def __init__(self, display_pointer, action_delay, dummy=False):
		self.type = None
		self.position = position_pointer[0]
		self.display_pointer = display_pointer
		self.action_delay = action_delay
		if not dummy:
			self.controller_thread = threading.Thread(target=self.controller, daemon=True)
			self.controller_thread.start()
	
	def up(self, x, y):
		if not self.isWall(x, y - 1):
			y -= 1
		return x, y
	
	def down(self, x, y):
		if not self.isWall(x, y + 1):
			y += 1
		return x, y
	
	def left(self, x, y):
		if not self.isWall(x - 1, y):
			x -= 1
		return x, y
	
	def right(self, x, y):
		if not self.isWall(x + 1, y):
			x += 1
		return x, y
	
	def updatePosition(self, x, y):
		self.position = (x, y)
		self.display_pointer[0].pixel_data[self.position] = maze_color_dict["agent"]
	
	def visit(self, x, y):
		self.display_pointer[0].pixel_data[(x, y)] = maze_color_dict["visited_tile"]
	
	def isVisited(self, x, y):
		return self.display_pointer[0].pixel_data[(x, y)] == maze_color_dict["visited_tile"]
	
	def isGoal(self, x, y):
		return self.display_pointer[0].pixel_data[(x, y)] == maze_color_dict["goal"]
	
	def isWall(self, x, y):
		return x < 0 or y < 0 or x >= self.display_pointer[0].width - 1 or y >= self.display_pointer[0].height - 1 or self.display_pointer[0].pixel_data[(x, y)] == maze_color_dict["wall"]

class KeyboardAgent(Agent):
	def __init__(self, display_pointer, action_delay):
		super().__init__(display_pointer, action_delay)
		self.type = "KeyboardAgent"
	
	def controller(self):
		while not close_event.is_set():
			if key_pressed_event.is_set():
				x, y = self.position
				self.visit(x, y)
				if key_pointer[0] == keyboard.Key.up:
					x, y = self.up(x, y)
				elif key_pointer[0] == keyboard.Key.down:
					x, y = self.down(x, y)
				elif key_pointer[0] == keyboard.Key.left:
					x, y = self.left(x, y)
				elif key_pointer[0] == keyboard.Key.right:
					x, y = self.right(x, y)
				
				if self.isGoal(x, y):
					victory(self.display_pointer)
					continue
				
				self.updatePosition(x, y)
				
				key_pressed_event.clear()
			time.sleep(self.action_delay)

class ComputerAgent(Agent):
	def __init__(self, display_pointer, action_delay, dummy=False):
		super().__init__(display_pointer, action_delay, dummy)
		self.type = "ComputerAgent"
	
	def controller(self):
		try:
			while not close_event.is_set():
				x, y = self.position
				self.visit(x, y)
				
				x, y = self.action(x, y)
				
				if self.isGoal(x, y):
					victory(self.display_pointer)
					continue
				
				self.updatePosition(x, y)
				
				time.sleep(self.action_delay)
		except Exception as e:
			self.display_pointer[0].refresh_thread.stop()
			raise e
	
class RandomAgent(ComputerAgent):
	def __init__(self, display_pointer, action_delay):
		super().__init__(display_pointer, action_delay)
	
	def action(self, x, y):
		directions = [self.up, self.down, self.left, self.right]
		action = random.choice(directions)
		return action(x, y)

class AlwaysLeftAgent(ComputerAgent):
	def __init__(self, display_pointer, action_delay):
		self.last_action = "up"
		super().__init__(display_pointer, action_delay)
	
	def action(self, x, y):
		if self.last_action == "up":
			if not self.isWall(x - 1, y):
				self.last_action = "left"
				action = self.left
			elif not self.isWall(x, y - 1):
				self.last_action = "up"
				action = self.up
			elif not self.isWall(x + 1, y):
				self.last_action = "right"
				action = self.right
			elif not self.isWall(x, y + 1):
				self.last_action = "down"
				action = self.down
		
		elif self.last_action == "left":
			if not self.isWall(x, y + 1):
				self.last_action = "down"
				action = self.down
			elif not self.isWall(x - 1, y):
				self.last_action = "left"
				action = self.left
			elif not self.isWall(x, y - 1):
				self.last_action = "up"
				action = self.up
			elif not self.isWall(x + 1, y):
				self.last_action = "right"
				action = self.right
		
		elif self.last_action == "down":
			if not self.isWall(x + 1, y):
				self.last_action = "right"
				action = self.right
			elif not self.isWall(x, y + 1):
				self.last_action = "down"
				action = self.down
			elif not self.isWall(x - 1, y):
				self.last_action = "left"
				action = self.left
			elif not self.isWall(x, y - 1):
				self.last_action = "up"
				action = self.up
		
		elif self.last_action == "right":
			if not self.isWall(x, y - 1):
				self.last_action = "up"
				action = self.up
			elif not self.isWall(x + 1, y):
				self.last_action = "right"
				action = self.right
			elif not self.isWall(x, y + 1):
				self.last_action = "down"
				action = self.down
			elif not self.isWall(x - 1, y):
				self.last_action = "left"
				action = self.left
		
		return action(x, y)

class ExplorerAgent(ComputerAgent):
	def __init__(self, display_pointer, action_delay):
		self.path = Stack()
		super().__init__(display_pointer, action_delay)
	
	def action(self, x, y):
		"""
		moves randomly, but avoids walls and priorites unvisited spaces (goal has top priority)
		keeps list (stack) of previous actions to backtrack
		"""
		choices = []
		if not self.isWall(x, y - 1):
			if self.isGoal(x, y - 1):
				return self.up(x, y)
			if not self.isVisited(x, y - 1):
				choices.append(self.up)
		
		if not self.isWall(x + 1, y):
			if self.isGoal(x + 1, y):
				return self.right(x, y)
			if not self.isVisited(x + 1, y):
				choices.append(self.right)
		
		if not self.isWall(x, y + 1):
			if self.isGoal(x, y + 1):
				return self.down(x, y)
			if not self.isVisited(x, y + 1):
				choices.append(self.down)
		
		if not self.isWall(x - 1, y):
			if self.isGoal(x - 1, y):
				return self.left(x, y)
			if not self.isVisited(x - 1, y):
				choices.append(self.left)
		
		if len(choices) > 0:
			action = random.choice(choices)
			self.path.push(action)
		else:
			previous = self.path.pop()
			if previous == self.up:
				action = self.down
			elif previous == self.down:
				action = self.up
			elif previous == self.left:
				action = self.right
			elif previous == self.right:
				action = self.left
		return action(x, y)

class SearchAgent(ComputerAgent):
	def __init__(self, display_pointer, action_delay, dummy=False):
		self.path = Stack()
		self.actions = Stack()
		self.search_complete_event = threading.Event()
		super().__init__(display_pointer, action_delay, dummy)
		self.type = "SearchAgent"
		if not dummy:
			self.search()
	
	def isExplored(self, x, y):
		return (x, y) == self.position or self.display_pointer[0].pixel_data[(x, y)] == maze_color_dict["explored_tile"]
	
	def explore(self, x, y):
		self.display_pointer[0].pixel_data[(x, y)] = maze_color_dict["explored_tile"]
	
	def actionsFromPath(self):
		x, y, action = self.path.pop()
		previous = (-1, -1)
		while action != None:
			if self.isGoal(x, y):
				self.actions.push(action)
				if action == self.left:
					previous = (x + 1, y)
				elif action == self.right:
					previous = (x - 1, y)
				elif action == self.up:
					previous = (x, y + 1)
				elif action == self.down:
					previous = (x, y - 1)
			elif (x, y) == previous:
				self.actions.push(action)
				if action == self.left:
					previous = (x + 1, y)
				elif action == self.right:
					previous = (x - 1, y)
				elif action == self.up:
					previous = (x, y + 1)
				elif action == self.down:
					previous = (x, y - 1)
			x, y, action = self.path.pop()
	
	def action(self, x, y):
		if not self.search_complete_event.is_set():
			return x, y
		if self.actions.isEmpty():
			return x, y
		return self.actions.pop()(x, y)

class DepthFirstAgent(SearchAgent):
	def __init__(self, display_pointer, action_delay, dummy=False):
		super().__init__(display_pointer, action_delay, dummy)
	
	def search(self):
		self.search_complete_event.clear()
		opened_tiles = Stack()
		x, y = self.position
		action = None
		searching = True
		while searching:
			if self.isGoal(x, y):
				searching = False
				self.path.push((x, y, action))
				continue
			
			if not (x, y) == self.position:
				self.explore(x, y)
			
			self.path.push((x, y, action))
			if not self.isWall(x - 1, y) and not self.isExplored(x - 1, y):
				opened_tiles.push((x - 1, y, self.left))
			if not self.isWall(x + 1, y) and not self.isExplored(x + 1, y):
				opened_tiles.push((x + 1, y, self.right))
			if not self.isWall(x, y - 1) and not self.isExplored(x, y - 1):
				opened_tiles.push((x, y - 1, self.up))
			if not self.isWall(x, y + 1) and not self.isExplored(x, y + 1):
				opened_tiles.push((x, y + 1, self.down))
			
			if opened_tiles.isEmpty():
				searching = False
				continue
			
			x, y, action = opened_tiles.pop()
			time.sleep(self.action_delay)
		
		self.actionsFromPath()
		self.search_complete_event.set()

class BreadthFirstAgent(SearchAgent):
	def __init__(self, display_pointer, action_delay, dummy=False):
		super().__init__(display_pointer, action_delay, dummy)
	
	def search(self):
		self.search_complete_event.clear()
		opened_tiles = Queue()
		x, y = self.position
		action = None
		searching = True
		while searching:
			if self.isGoal(x, y):
				searching = False
				self.path.push((x, y, action))
				continue
			
			if not (x, y) == self.position:
				self.explore(x, y)
			
			self.path.push((x, y, action))
			if not self.isWall(x - 1, y) and not self.isExplored(x - 1, y):
				opened_tiles.push((x - 1, y, self.left))
			if not self.isWall(x + 1, y) and not self.isExplored(x + 1, y):
				opened_tiles.push((x + 1, y, self.right))
			if not self.isWall(x, y - 1) and not self.isExplored(x, y - 1):
				opened_tiles.push((x, y - 1, self.up))
			if not self.isWall(x, y + 1) and not self.isExplored(x, y + 1):
				opened_tiles.push((x, y + 1, self.down))
			
			if opened_tiles.isEmpty():
				searching = False
				continue
			
			x, y, action = opened_tiles.pop()
			time.sleep(self.action_delay)
		
		self.actionsFromPath()
		self.search_complete_event.set()

class HeuristicSearchAgent(SearchAgent):
	def __init__(self, display_pointer, action_delay, heuristic, dummy=False):
		self.heuristic = heuristic
		super().__init__(display_pointer, action_delay, dummy)

class AStarAgent(HeuristicSearchAgent):
	def __init__(self, display_pointer, action_delay, heuristic, dummy=False):
		super().__init__(display_pointer, action_delay, dummy)
	
	def search(self):
		pass

class LearningAgent(ComputerAgent):
	def __init__(self, display_pointer, action_delay):
		super().__init__(display_pointer, action_delay)
		self.type = "LearningAgent"


class Heuristic:
	def findDistance(self, state):
		pass

class ManhatanDistanceHeuristic(Heuristic):
	def findDistance(self, state):
		x_agent, y_agent = state[0]
		x_goal, y_goal = state[1]
		return abs(x_agent - x_goal) + abs(y_agent - y_goal)

class EulerDistanceHeuristic(Heuristic):
	def findDistance(self, state):
		x_agent, y_agent = state[0]
		x_goal, y_goal = state[1]
		return math.sqrt((x_agent - x_goal) * 2 + (y_agent - y_goal) * 2)


def testClosingProcess():
	while not close_event.is_set():
		pass
	time.sleep(5)


def run():
	try:
		scale = 2
		width = 16
		height = 16
		ratio = (2, 1) # characters, lines; 2 characters = 1 line
		refresh_rate = 60 # frames per second
		display_pointer = [Display(width, height, scale, ratio, refresh_rate)]
		
		
		# generateMaze(display_pointer)
		generateMaze8x8(display_pointer)
		# display_pointer[0].update()
		
		# event_test_thread = threading.Thread(target=eventTest, args=(display_pointer,), daemon=True)
		# event_test_thread.start()
		
		# agent = KeyboardAgent(display_pointer, 0.1)
		# agent = RandomAgent(display_pointer, 0.005)
		# agent = AlwaysLeftAgent(display_pointer, 0.05)
		# agent = ExplorerAgent(display_pointer, 0.05)
		# agent = DepthFirstAgent(display_pointer, 0.05)
		agent = BreadthFirstAgent(display_pointer, 0.05)
		# agent = AStarAgent(display_pointer, 0.05, ManhatanDistanceHeuristic())
		
		agent_pointer[0] = agent
		
		# t = threading.Thread(target=testClosingProcess)
		# t.start()
		
		with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
			listener.join()
		
		# close_event.set()
# 		i = 0
# 		while True:
# 			if i % 256 == 0:
# 				i = 0
# 			for y in range(height):
# 				for x in range(width):
# 					r = x * (i // width) % 256
# 					g = y * (i // height) % 256
# 					b = max(i - (r + g), 0)
# 					display_pointer[0].updatePixel(x, y, r, g, b)
# 			i += 1
		
		# input()
	except KeyboardInterrupt:
		pass