from utils.data_structures import State

import numpy as np

class Cube(State):
	class Cubee:
		def __init__(self):
			self.sides = {
				"U" : "w",
				"F" : "g",
				"R" : "r",
				"D" : "y",
				"B" : "b",
				"L" : "o"
			}
		
		def __repr__(self):
			return str(self.sides)
		
		def apply(self, action):
			if action == "x":
				self.x()
			elif action == "x'":
				self.xPrime()
			elif action == "x2":
				self.xDouble()
			elif action == "y":
				self.y()
			elif action == "y'":
				self.yPrime()
			elif action == "y2":
				self.yDouble()
			elif action == "z":
				self.z()
			elif action == "z'":
				self.zPrime()
			elif action == "z2":
				self.zDouble()
		
		def x(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["F"]
			self.sides["F"] = self.sides["D"]
			self.sides["D"] = self.sides["B"]
			self.sides["B"] = tmp

		def xPrime(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["B"]
			self.sides["B"] = self.sides["D"]
			self.sides["D"] = self.sides["F"]
			self.sides["F"] = tmp

		def xDouble(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["D"]
			self.sides["D"] = tmp
			tmp = self.sides["F"]
			self.sides["F"] = self.sides["B"]
			self.sides["B"] = tmp

		def y(self):
			tmp = self.sides["F"]
			self.sides["F"] = self.sides["R"]
			self.sides["R"] = self.sides["B"]
			self.sides["B"] = self.sides["L"]
			self.sides["L"] = tmp

		def yPrime(self):
			tmp = self.sides["F"]
			self.sides["F"] = self.sides["L"]
			self.sides["L"] = self.sides["B"]
			self.sides["B"] = self.sides["R"]
			self.sides["R"] = tmp

		def yDouble(self):
			tmp = self.sides["F"]
			self.sides["F"] = self.sides["B"]
			self.sides["B"] = tmp
			tmp = self.sides["R"]
			self.sides["R"] = self.sides["L"]
			self.sides["L"] = tmp

		def z(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["L"]
			self.sides["L"] = self.sides["D"]
			self.sides["D"] = self.sides["R"]
			self.sides["R"] = tmp

		def zPrime(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["R"]
			self.sides["R"] = self.sides["D"]
			self.sides["D"] = self.sides["L"]
			self.sides["L"] = tmp

		def zDouble(self):
			tmp = self.sides["U"]
			self.sides["U"] = self.sides["D"]
			self.sides["D"] = tmp
			tmp = self.sides["R"]
			self.sides["R"] = self.sides["L"]
			self.sides["L"] = tmp
	
	def __init__(self, size):
		self.color_dict = {
			"w" : (255, 255, 255),
			"g" : (0, 255, 0),
			"o" : (255, 128, 0),
			"b" : (0, 0, 255),
			"r" : (255, 0, 0),
			"y" : (255, 255, 0),
			"core" : (24, 24, 24)
		}

		self.size = size
		self.center = -1
		if ((self.size - 1) // 2) * 2 == self.size - 1:
			self.center = (self.size - 1) // 2
		self.generateArray()

		self.cube = {
			"U" : [],
			"F" : [],
			"R" : [],
			"D" : [],
			"B" : [],
			"L" : []
		}

		self.moves = {}
		self.reverse_moves = {}
	
	def generateArray(self):
		self.cube_array = np.empty([self.size, self.size, self.size], dtype=self.Cubee)
		for x in range(self.size):
			for y in range(self.size):
				for z in range(self.size):
					self.cube_array[x][y][z] = self.Cubee()
	
	def apply(self, action):
		if not action in self.moves.keys():
			pass
		else:
			self.moves[action]()
	
	def isSolved(self):
		for side in self.cube.keys():
			color = None
			for x in range(self.size):
				for y in range(self.size):
					if color is not None:
						if self.cube[side][x][y] != color:
							return False
					else:
						color = self.cube[side][x][y]
		return True
	
	def reverse(self, action):
		return self.reverse_moves[action]

	def represent(self):
		translation_table = {
			"UF" : 0 * 2 ** 2 + 0,
			"UR" : 0 * 2 ** 2 + 1,
			"UB" : 0 * 2 ** 2 + 2,
			"UL" : 0 * 2 ** 2 + 3,
			"FU" : 1 * 2 ** 2 + 0,
			"FR" : 1 * 2 ** 2 + 1,
			"FD" : 1 * 2 ** 2 + 2,
			"FL" : 1 * 2 ** 2 + 3,
			"RU" : 2 * 2 ** 2 + 0,
			"RF" : 2 * 2 ** 2 + 1,
			"RD" : 2 * 2 ** 2 + 2,
			"RB" : 2 * 2 ** 2 + 3,
			"DF" : 3 * 2 ** 2 + 0,
			"DR" : 3 * 2 ** 2 + 1,
			"DB" : 3 * 2 ** 2 + 2,
			"DL" : 3 * 2 ** 2 + 3,
			"BU" : 4 * 2 ** 2 + 0,
			"BR" : 4 * 2 ** 2 + 1,
			"BD" : 4 * 2 ** 2 + 2,
			"BL" : 4 * 2 ** 2 + 3,
			"LU" : 5 * 2 ** 2 + 0,
			"LF" : 5 * 2 ** 2 + 1,
			"LD" : 5 * 2 ** 2 + 2,
			"LB" : 5 * 2 ** 2 + 3
		}
		representation = []
		for x in range(self.size):
			for y in range(self.size):
				for z in range(self.size):
					if (x == self.center and y == self.center and z == self.center) or x in [0, self.size - 1] or y in [0, self.size - 1] or z in [0, self.size - 1]:
						cubee = self.cube_array[x][y][z]
						w_cubee = ""
						g_cubee = ""
						for side in cubee.sides:
							if cubee.sides[side] == "w":
								w_cubee = side
							elif cubee.sides[side] == "g":
								g_cubee = side
							if w_cubee != "" and g_cubee != "":
								break
						cubee_orientation_key = w_cubee + g_cubee
						representation.append(x * 2 ** 11 + y * 2 ** 8 + z * 2 ** 5 + translation_table[cubee_orientation_key])
		return representation
	
	def fromRepresentation(self, representation):
		translation_table = {
			0 * 2 ** 2 + 0 : [],
			0 * 2 ** 2 + 1 : ["y'"],
			0 * 2 ** 2 + 2 : ["y2"],
			0 * 2 ** 2 + 3 : ["y"],
			1 * 2 ** 2 + 0 : ["y2", "x'"],
			1 * 2 ** 2 + 1 : ["y'", "x'"],
			1 * 2 ** 2 + 2 : ["x'"],
			1 * 2 ** 2 + 3 : ["y", "x'"],
			2 * 2 ** 2 + 0 : ["y", "z"],
			2 * 2 ** 2 + 1 : ["z"],
			2 * 2 ** 2 + 2 : ["y'", "z"],
			2 * 2 ** 2 + 3 : ["y2", "z"],
			3 * 2 ** 2 + 0 : ["z2"],
			3 * 2 ** 2 + 1 : ["y'", "x2"],
			3 * 2 ** 2 + 2 : ["x2"],
			3 * 2 ** 2 + 3 : ["y'", "z2"],
			4 * 2 ** 2 + 0 : ["x"],
			4 * 2 ** 2 + 1 : ["y'", "x"],
			4 * 2 ** 2 + 2 : ["y2", "x"],
			4 * 2 ** 2 + 3 : ["y", "x"],
			5 * 2 ** 2 + 0 : ["y'", "z'"],
			5 * 2 ** 2 + 1 : ["z'"],
			5 * 2 ** 2 + 2 : ["y", "z'"],
			5 * 2 ** 2 + 3 : ["y2", "z'"]
		}
		self.cube_array = np.empty([self.size, self.size, self.size], dtype=self.Cubee)
		for i in range(len(representation)):
			if representation[i] // 2 ** 11 == self.center and (representation[i] % 11) // 2 ** 8 == self.center and (representation[i] % 2 ** 8) // 2 ** 5 == self.center:
				cu = self.Cubee()
				cf = self.Cubee()
				cr = self.Cubee()
				cd = self.Cubee()
				cb = self.Cubee()
				cl = self.Cubee()
				for action in translation_table[representation[i] % 2 ** 5]:
					cu.apply(action)
					cf.apply(action)
					cr.apply(action)
					cd.apply(action)
					cb.apply(action)
					cl.apply(action)
				self.cube_array[self.center, 0, self.center] = cu
				self.cube_array[self.center, self.center, self.size - 1] = cf
				self.cube_array[self.size - 1, self.center, self.center] = cr
				self.cube_array[self.center, self.size - 1, self.center] = cd
				self.cube_array[self.center, self.center, 0] = cb
				self.cube_array[0, self.center, self.center] = cl
			cubee = self.Cubee()
			for action in translation_table[representation[i] % 2 ** 5]:
				cubee.apply(action)
			self.cube_array[representation[i] // 2 ** 11][(representation[i] % 2 ** 11) // 2 ** 8][(representation[i] % 2 ** 8) // 2 ** 5] = cubee
		self.update()