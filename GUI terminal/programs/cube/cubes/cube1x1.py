from programs.cube.cubes.cube import Cube

class Cube1x1(Cube):
	def __init__(self):
		super().__init__(1)

		self.moves = {
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
				["w"]
			],
			"F" :
			[
				["g"]
			],
			"R" :
			[
				["r"]
			],
			"D" :
			[
				["y"]
			],
			"B" :
			[
				["b"]
			],
			"L" :
			[
				["o"]
			]
		}
	
	def x(self):
		self.cube_array[0][0][0].x()

	def xPrime(self):
		self.cube_array[0][0][0].xPrime()

	def xDouble(self):
		self.cube_array[0][0][0].xDouble()

	def y(self):
		self.cube_array[0][0][0].y()

	def yPrime(self):
		self.cube_array[0][0][0].yPrime()

	def yDouble(self):
		self.cube_array[0][0][0].yDouble()

	def z(self):
		self.cube_array[0][0][0].z()

	def zPrime(self):
		self.cube_array[0][0][0].zPrime()

	def zDouble(self):
		self.cube_array[0][0][0].zDouble()
	
	def update(self):
		self.cube["U"][0][0] = self.cube_array[0][0][0].sides["U"]
		self.cube["F"][0][0] = self.cube_array[0][0][0].sides["F"]
		self.cube["R"][0][0] = self.cube_array[0][0][0].sides["R"]
		self.cube["D"][0][0] = self.cube_array[0][0][0].sides["D"]
		self.cube["B"][0][0] = self.cube_array[0][0][0].sides["B"]
		self.cube["L"][0][0] = self.cube_array[0][0][0].sides["L"]