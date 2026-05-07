from programs.cube.cubes.cube import Cube

class Cube2x2(Cube):
	def __init__(self):
		super().__init__(2)
		
		self.moves = {
			"U" : self.u,
			"U'" : self.uPrime,
			"U2" : self.uDouble,
			"F" : self.f,
			"F'" : self.fPrime,
			"F2" : self.fDouble,
			"R" : self.r,
			"R'" : self.rPrime,
			"R2" : self.rDouble,
			"D" : self.d,
			"D'" : self.dPrime,
			"D2" : self.dDouble,
			"B" : self.b,
			"B'" : self.bPrime,
			"B2" : self.bDouble,
			"L" : self.l,
			"L'" : self.lPrime,
			"L2" : self.lDouble,
			"x" : self.x,
			"x'" : self.xPrime,
			"x2" : self.xDouble,
			"y" : self.y,
			"y'" : self.yPrime,
			"y2" : self.yDouble,
			"z" : self.z,
			"z'" : self.zPrime,
			"z2" : self.zDouble
		}

		self.reverse_moves = {
			"U" : "U'",
			"U'" : "U",
			"U2" : "U2",
			"F" : "F'",
			"F'" : "F",
			"F2" : "F2",
			"R" : "R'",
			"R'" : "R",
			"R2" : "R2",
			"D" : "D'",
			"D'" : "D",
			"D2" : "D2",
			"B" : "B'",
			"B'" : "B",
			"B2" : "B2",
			"L" : "L'",
			"L'" : "L",
			"L2" : "L2",
			"x" : "x'",
			"x'" : "x",
			"x2" : "x2",
			"y" : "y'",
			"y'" : "y",
			"y2" : "y2",
			"z" : "z'",
			"z'" : "z",
			"z2" : "z2"
		}

		self.cube = {
			"U" :
			[
				["w", "w"],
				["w", "w"]
			],
			"F" :
			[
				["g", "g"],
				["g", "g"]
			],
			"R" :
			[
				["r", "r"],
				["r", "r"]
			],
			"D" :
			[
				["y", "y"],
				["y", "y"]
			],
			"B" :
			[
				["b", "b"],
				["b", "b"]
			],
			"L" :
			[
				["o", "o"],
				["o", "o"]
			]
		}

	def u(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		self.cube_array[0][0][0].y()
		self.cube_array[0][0][1].y()
		self.cube_array[1][0][0].y()
		self.cube_array[1][0][1].y()

		self.update()

	def uPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		self.cube_array[0][0][0].yPrime()
		self.cube_array[0][0][1].yPrime()
		self.cube_array[1][0][0].yPrime()
		self.cube_array[1][0][1].yPrime()

		self.update()

	def uDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		self.cube_array[0][0][0].yDouble()
		self.cube_array[0][0][1].yDouble()
		self.cube_array[1][0][0].yDouble()
		self.cube_array[1][0][1].yDouble()

		self.update()
	
	def f(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		self.cube_array[0][0][1].z()
		self.cube_array[0][1][1].z()
		self.cube_array[1][0][1].z()
		self.cube_array[1][1][1].z()

		self.update()

	def fPrime(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		self.cube_array[0][0][1].zPrime()
		self.cube_array[0][1][1].zPrime()
		self.cube_array[1][0][1].zPrime()
		self.cube_array[1][1][1].zPrime()

		self.update()

	def fDouble(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self. cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		self.cube_array[0][0][1].zDouble()
		self.cube_array[0][1][1].zDouble()
		self.cube_array[1][0][1].zDouble()
		self.cube_array[1][1][1].zDouble()

		self.update()

	def r(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[1][0][0].x()
		self.cube_array[1][0][1].x()
		self.cube_array[1][1][0].x()
		self.cube_array[1][1][1].x()

		self.update()

	def rPrime(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		self.cube_array[1][0][0].xPrime()
		self.cube_array[1][0][1].xPrime()
		self.cube_array[1][1][0].xPrime()
		self.cube_array[1][1][1].xPrime()

		self.update()

	def rDouble(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[1][0][0].xDouble()
		self.cube_array[1][0][1].xDouble()
		self.cube_array[1][1][0].xDouble()
		self.cube_array[1][1][1].xDouble()

		self.update()

	def d(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		self.cube_array[0][1][0].yPrime()
		self.cube_array[0][1][1].yPrime()
		self.cube_array[1][1][0].yPrime()
		self.cube_array[1][1][1].yPrime()

		self.update()

	def dPrime(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[0][1][0].y()
		self.cube_array[0][1][1].y()
		self.cube_array[1][1][0].y()
		self.cube_array[1][1][1].y()

		self.update()

	def dDouble(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp
		
		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[0][1][0].yDouble()
		self.cube_array[0][1][1].yDouble()
		self.cube_array[1][1][0].yDouble()
		self.cube_array[1][1][1].yDouble()

		self.update()

	def b(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		self.cube_array[0][0][0].zPrime()
		self.cube_array[0][1][0].zPrime()
		self.cube_array[1][0][0].zPrime()
		self.cube_array[1][1][0].zPrime()

		self.update()

	def bPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		self.cube_array[0][0][0].z()
		self.cube_array[0][1][0].z()
		self.cube_array[1][0][0].z()
		self.cube_array[1][1][0].z()

		self.update()

	def bDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		self.cube_array[0][0][0].zDouble()
		self.cube_array[0][1][0].zDouble()
		self.cube_array[1][0][0].zDouble()
		self.cube_array[1][1][0].zDouble()

		self.update()

	def l(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		self.cube_array[0][0][0].xPrime()
		self.cube_array[0][0][1].xPrime()
		self.cube_array[0][1][0].xPrime()
		self.cube_array[0][1][1].xPrime()

		self.update()

	def lPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		self.cube_array[0][0][0].x()
		self.cube_array[0][0][1].x()
		self.cube_array[0][1][0].x()
		self.cube_array[0][1][1].x()

		self.update()

	def lDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		self.cube_array[0][0][0].xDouble()
		self.cube_array[0][0][1].xDouble()
		self.cube_array[0][1][0].xDouble()
		self.cube_array[0][1][1].xDouble()

		self.update()

	def x(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp
		
		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].x()
		
		self.update()

	def xPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp
		
		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].xPrime()

		self.update()

	def xDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].xDouble()
		
		self.update()

	def y(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].y()
		
		self.update()

	def yPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].yPrime()
		
		self.update()

	def yDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].yDouble()
		
		self.update()

	def z(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].z()
		
		self.update()

	def zPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].zPrime()
		
		self.update()

	def zDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][1][1]
		self.cube_array[1][1][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = tmp

		for x in range(2):
			for y in range(2):
				for z in range(2):
					self.cube_array[x][y][z].zDouble()
		
		self.update()
	
	def update(self):
		self.cube["U"][0][0] = self.cube_array[0][0][0].sides["U"]
		self.cube["U"][0][1] = self.cube_array[0][0][1].sides["U"]
		self.cube["U"][1][0] = self.cube_array[1][0][0].sides["U"]
		self.cube["U"][1][1] = self.cube_array[1][0][1].sides["U"]

		self.cube["F"][0][0] = self.cube_array[0][0][1].sides["F"]
		self.cube["F"][0][1] = self.cube_array[0][1][1].sides["F"]
		self.cube["F"][1][0] = self.cube_array[1][0][1].sides["F"]
		self.cube["F"][1][1] = self.cube_array[1][1][1].sides["F"]

		self.cube["R"][0][0] = self.cube_array[1][0][1].sides["R"]
		self.cube["R"][0][1] = self.cube_array[1][0][0].sides["R"]
		self.cube["R"][1][0] = self.cube_array[1][1][1].sides["R"]
		self.cube["R"][1][1] = self.cube_array[1][1][0].sides["R"]

		self.cube["D"][0][0] = self.cube_array[0][1][0].sides["D"]
		self.cube["D"][0][1] = self.cube_array[0][1][1].sides["D"]
		self.cube["D"][1][0] = self.cube_array[1][1][0].sides["D"]
		self.cube["D"][1][1] = self.cube_array[1][1][1].sides["D"]

		self.cube["B"][0][0] = self.cube_array[0][0][0].sides["B"]
		self.cube["B"][0][1] = self.cube_array[0][1][0].sides["B"]
		self.cube["B"][1][0] = self.cube_array[1][0][0].sides["B"]
		self.cube["B"][1][1] = self.cube_array[1][1][0].sides["B"]

		self.cube["L"][0][0] = self.cube_array[0][0][1].sides["L"]
		self.cube["L"][0][1] = self.cube_array[0][0][0].sides["L"]
		self.cube["L"][1][0] = self.cube_array[0][1][1].sides["L"]
		self.cube["L"][1][1] = self.cube_array[0][1][0].sides["L"]
	
	def drawIsometric(self, display_pointer, padx=0, pady=0, init=False):
		display_pointer[0].pixel_data[(padx + 8, pady + 1)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 1)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 7, pady + 2)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 2)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 2)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 2)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 3)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 3)] = self.color_dict[self.cube["U"][0][0]]

		display_pointer[0].pixel_data[(padx + 5, pady + 3)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 6, pady + 3)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 4, pady + 4)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 4)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 6, pady + 4)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 7, pady + 4)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 5)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 6, pady + 5)] = self.color_dict[self.cube["U"][0][1]]

		display_pointer[0].pixel_data[(padx + 11, pady + 3)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 3)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 11, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 13, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 11, pady + 5)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 5)] = self.color_dict[self.cube["U"][1][0]]

		display_pointer[0].pixel_data[(padx + 8, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 7, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 7)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 7)] = self.color_dict[self.cube["U"][1][1]]

		display_pointer[0].pixel_data[(padx + 1, pady + 7)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 1, pady + 8)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 8)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 9)] = self.color_dict[self.cube["F"][0][0]]

		display_pointer[0].pixel_data[(padx + 1, pady + 10)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 1, pady + 11)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 2, pady + 11)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 2, pady + 12)] = self.color_dict[self.cube["F"][0][1]]

		display_pointer[0].pixel_data[(padx + 4, pady + 9)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 11)] = self.color_dict[self.cube["F"][1][0]]

		display_pointer[0].pixel_data[(padx + 4, pady + 12)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 4, pady + 13)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 13)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 14)] = self.color_dict[self.cube["F"][1][1]]

		display_pointer[0].pixel_data[(padx + 13, pady + 9)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 13, pady + 10)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 10)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 11)] = self.color_dict[self.cube["R"][0][0]]

		display_pointer[0].pixel_data[(padx + 13, pady + 12)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 13, pady + 13)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 13)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 14)] = self.color_dict[self.cube["R"][1][0]]

		display_pointer[0].pixel_data[(padx + 10, pady + 11)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 12)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 12)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 13)] = self.color_dict[self.cube["R"][0][1]]

		display_pointer[0].pixel_data[(padx + 10, pady + 14)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 15)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 15)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 16)] = self.color_dict[self.cube["R"][1][1]]

		if init:
			display_pointer[0].pixel_data[(padx + 1, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 1, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 2, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 2, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 8)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 3, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 4, pady + 5)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 4, pady + 7)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 4, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 4, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 5, pady + 6)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 5, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 5, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 6)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 16)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 6, pady + 17)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 3)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 5)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 7)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 7, pady + 16)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 8, pady + 4)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 8, pady + 8)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 8, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 8, pady + 17)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 9, pady + 4)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 9, pady + 8)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 9, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 9, pady + 17)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 3)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 5)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 7)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 10, pady + 16)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 6)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 16)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 11, pady + 17)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 12, pady + 6)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 12, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 12, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 13, pady + 5)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 13, pady + 7)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 13, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 13, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 8)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 11)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 12)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 14)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 14, pady + 15)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 15, pady + 10)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 15, pady + 13)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 16, pady + 9)] = self.color_dict["core"]
			display_pointer[0].pixel_data[(padx + 16, pady + 12)] = self.color_dict["core"]