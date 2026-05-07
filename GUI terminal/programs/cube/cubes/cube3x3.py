from programs.cube.cubes.cube import Cube

class Cube3x3(Cube):
	def __init__(self):
		super().__init__(3)
		
		self.moves = {
			"U" : self.u,
			"U'" : self.uPrime,
			"U2" : self.uDouble,
			"u" : self.uWide,
			"u'" : self.uPrimeWide,
			"u2" : self.uDoubleWide,
			"F" : self.f,
			"F'" : self.fPrime,
			"F2" : self.fDouble,
			"f" : self.fWide,
			"f'" : self.fPrimeWide,
			"f2" : self.fDoubleWide,
			"R" : self.r,
			"R'" : self.rPrime,
			"R2" : self.rDouble,
			"r" : self.rWide,
			"r'" : self.rPrimeWide,
			"r2" : self.rDoubleWide,
			"D" : self.d,
			"D'" : self.dPrime,
			"D2" : self.dDouble,
			"d" : self.dWide,
			"d'" : self.dPrimeWide,
			"d2" : self.dDoubleWide,
			"B" : self.b,
			"B'" : self.bPrime,
			"B2" : self.bDouble,
			"b" : self.bWide,
			"b'" : self.bPrimeWide,
			"b2" : self.bDoubleWide,
			"L" : self.l,
			"L'" : self.lPrime,
			"L2" : self.lDouble,
			"l" : self.lWide,
			"l'" : self.lPrimeWide,
			"l2" : self.lDoubleWide,
			"M" : self.m,
			"M'" : self.mPrime,
			"M2" : self.mDouble,
			"E" : self.e,
			"E'" : self.ePrime,
			"E2" : self.eDouble,
			"S" : self.s,
			"S'" : self.sPrime,
			"S2" : self.sDouble,
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
			"u" : "u'",
			"u'" : "u",
			"u2" : "u2",
			"F" : "F'",
			"F'" : "F",
			"F2" : "F2",
			"f" : "f'",
			"f'" : "f",
			"f2" : "f2",
			"R" : "R'",
			"R'" : "R",
			"R2" : "R2",
			"r" : "r'",
			"r'" : "r",
			"r2" : "r2",
			"D" : "D'",
			"D'" : "D",
			"D2" : "D2",
			"d" : "d'",
			"d'" : "d",
			"d2" : "d2",
			"B" : "B'",
			"B'" : "B",
			"B2" : "B2",
			"b" : "b'",
			"b'" : "b",
			"b2" : "b2",
			"L" : "L'",
			"L'" : "L",
			"L2" : "L2",
			"l" : "l'",
			"l'" : "l",
			"l2" : "l2",
			"M" : "M'",
			"M'" : "M",
			"M2" : "M2",
			"E" : "E'",
			"E'" : "E",
			"E2" : "E2",
			"S" : "S'",
			"S'" : "S",
			"S2" : "S2",
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
				["w", "w", "w"],
				["w", "w", "w"],
				["w", "w", "w"]
			],
			"F" :
			[
				["g", "g", "g"],
				["g", "g", "g"],
				["g", "g", "g"]
			],
			"R" :
			[
				["r", "r", "r"],
				["r", "r", "r"],
				["r", "r", "r"]
			],
			"D" :
			[
				["y", "y", "y"],
				["y", "y", "y"],
				["y", "y", "y"]
			],
			"B" :
			[
				["b", "b", "b"],
				["b", "b", "b"],
				["b", "b", "b"]
			],
			"L" :
			[
				["o", "o", "o"],
				["o", "o", "o"],
				["o", "o", "o"]
			]
		}

	def u(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		self.cube_array[0][0][0].y()
		self.cube_array[1][0][0].y()
		self.cube_array[2][0][0].y()
		self.cube_array[0][0][1].y()
		self.cube_array[2][0][1].y()
		self.cube_array[0][0][2].y()
		self.cube_array[1][0][2].y()
		self.cube_array[2][0][2].y()

		self.update()

	def uPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		self.cube_array[0][0][0].yPrime()
		self.cube_array[1][0][0].yPrime()
		self.cube_array[2][0][0].yPrime()
		self.cube_array[0][0][1].yPrime()
		self.cube_array[2][0][1].yPrime()
		self.cube_array[0][0][2].yPrime()
		self.cube_array[1][0][2].yPrime()
		self.cube_array[2][0][2].yPrime()

		self.update()

	def uDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp
		
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		self.cube_array[0][0][0].yDouble()
		self.cube_array[1][0][0].yDouble()
		self.cube_array[2][0][0].yDouble()
		self.cube_array[0][0][1].yDouble()
		self.cube_array[2][0][1].yDouble()
		self.cube_array[0][0][2].yDouble()
		self.cube_array[1][0][2].yDouble()
		self.cube_array[2][0][2].yDouble()

		self.update()
	
	def uWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(2):
				for z in range(3):
					self.cube_array[x][y][z].y()
		self.cube_array[1][2][1].y()
		
		self.update()
	
	def uPrimeWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(2):
				for z in range(3):
					self.cube_array[x][y][z].yPrime()
		self.cube_array[1][2][1].yPrime()
		
		self.update()
	
	def uDoubleWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] =tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(2):
				for z in range(3):
					self.cube_array[x][y][z].yDouble()
		self.cube_array[1][2][1].yDouble()
		
		self.update()
	
	def f(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		self.cube_array[0][0][2].z()
		self.cube_array[0][1][2].z()
		self.cube_array[0][2][2].z()
		self.cube_array[1][0][2].z()
		self.cube_array[1][2][2].z()
		self.cube_array[2][0][2].z()
		self.cube_array[2][1][2].z()
		self.cube_array[2][2][2].z()

		self.update()

	def fPrime(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		self.cube_array[0][0][2].zPrime()
		self.cube_array[0][1][2].zPrime()
		self.cube_array[0][2][2].zPrime()
		self.cube_array[1][0][2].zPrime()
		self.cube_array[1][2][2].zPrime()
		self.cube_array[2][0][2].zPrime()
		self.cube_array[2][1][2].zPrime()
		self.cube_array[2][2][2].zPrime()

		self.update()

	def fDouble(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self. cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		self.cube_array[0][0][2].zDouble()
		self.cube_array[0][1][2].zDouble()
		self.cube_array[0][2][2].zDouble()
		self.cube_array[1][0][2].zDouble()
		self.cube_array[1][2][2].zDouble()
		self.cube_array[2][0][2].zDouble()
		self.cube_array[2][1][2].zDouble()
		self.cube_array[2][2][2].zDouble()

		self.update()
	
	def fWide(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(1, 3):
					self.cube_array[x][y][z].z()
		self.cube_array[1][1][0].z()
		
		self.update()
	
	def fPrimeWide(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(1, 3):
					self.cube_array[x][y][z].zPrime()
		self.cube_array[1][1][0].zPrime()
		
		self.update()
	
	def fDoubleWide(self):
		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(1, 3):
					self.cube_array[x][y][z].zDouble()
		self.cube_array[1][1][0].zDouble()
		
		self.update()

	def r(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		self.cube_array[2][0][0].x()
		self.cube_array[2][0][1].x()
		self.cube_array[2][0][2].x()
		self.cube_array[2][1][0].x()
		self.cube_array[2][1][2].x()
		self.cube_array[2][2][0].x()
		self.cube_array[2][2][1].x()
		self.cube_array[2][2][2].x()

		self.update()

	def rPrime(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		self.cube_array[2][0][0].xPrime()
		self.cube_array[2][0][1].xPrime()
		self.cube_array[2][0][2].xPrime()
		self.cube_array[2][1][0].xPrime()
		self.cube_array[2][1][2].xPrime()
		self.cube_array[2][2][0].xPrime()
		self.cube_array[2][2][1].xPrime()
		self.cube_array[2][2][2].xPrime()

		self.update()

	def rDouble(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp
		
		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		self.cube_array[2][0][0].xDouble()
		self.cube_array[2][0][1].xDouble()
		self.cube_array[2][0][2].xDouble()
		self.cube_array[2][1][0].xDouble()
		self.cube_array[2][1][2].xDouble()
		self.cube_array[2][2][0].xDouble()
		self.cube_array[2][2][1].xDouble()
		self.cube_array[2][2][2].xDouble()

		self.update()
	
	def rWide(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp
		
		for x in range(1, 3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].x()
		self.cube_array[0][1][1].x()
		
		self.update()
	
	def rPrimeWide(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp
		
		for x in range(1, 3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xPrime()
		self.cube_array[0][1][1].xPrime()

		self.update()
	
	def rDoubleWide(self):
		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		for x in range(1, 3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xDouble()
		self.cube_array[0][1][1].xDouble()
		
		self.update()

	def d(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		self.cube_array[0][2][0].yPrime()
		self.cube_array[0][2][1].yPrime()
		self.cube_array[0][2][2].yPrime()
		self.cube_array[1][2][0].yPrime()
		self.cube_array[1][2][2].yPrime()
		self.cube_array[2][2][0].yPrime()
		self.cube_array[2][2][1].yPrime()
		self.cube_array[2][2][2].yPrime()

		self.update()

	def dPrime(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		self.cube_array[0][2][0].y()
		self.cube_array[0][2][1].y()
		self.cube_array[0][2][2].y()
		self.cube_array[1][2][0].y()
		self.cube_array[1][2][2].y()
		self.cube_array[2][2][0].y()
		self.cube_array[2][2][1].y()
		self.cube_array[2][2][2].y()

		self.update()

	def dDouble(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp
		
		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		self.cube_array[0][2][0].yDouble()
		self.cube_array[0][2][1].yDouble()
		self.cube_array[0][2][2].yDouble()
		self.cube_array[1][2][0].yDouble()
		self.cube_array[1][2][2].yDouble()
		self.cube_array[2][2][0].yDouble()
		self.cube_array[2][2][1].yDouble()
		self.cube_array[2][2][2].yDouble()

		self.update()
	
	def dWide(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(1, 3):
				for z in range(3):
					self.cube_array[x][y][z].yPrime()
		self.cube_array[1][0][1].yPrime()
		
		self.update()
	
	def dPrimeWide(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(1, 3):
				for z in range(3):
					self.cube_array[x][y][z].y()
		self.cube_array[1][0][1].y()
		
		self.update()
	
	def dDoubleWide(self):
		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] =tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(1, 3):
				for z in range(3):
					self.cube_array[x][y][z].yDouble()
		self.cube_array[1][0][1].yDouble()
		
		self.update()

	def b(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		self.cube_array[0][0][0].zPrime()
		self.cube_array[0][1][0].zPrime()
		self.cube_array[0][2][0].zPrime()
		self.cube_array[1][0][0].zPrime()
		self.cube_array[1][2][0].zPrime()
		self.cube_array[2][0][0].zPrime()
		self.cube_array[2][1][0].zPrime()
		self.cube_array[2][2][0].zPrime()

		self.update()

	def bPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		self.cube_array[0][0][0].z()
		self.cube_array[0][1][0].z()
		self.cube_array[0][2][0].z()
		self.cube_array[1][0][0].z()
		self.cube_array[1][2][0].z()
		self.cube_array[2][0][0].z()
		self.cube_array[2][1][0].z()
		self.cube_array[2][2][0].z()

		self.update()

	def bDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		self.cube_array[0][0][0].zDouble()
		self.cube_array[0][1][0].zDouble()
		self.cube_array[0][2][0].zDouble()
		self.cube_array[1][0][0].zDouble()
		self.cube_array[1][2][0].zDouble()
		self.cube_array[2][0][0].zDouble()
		self.cube_array[2][1][0].zDouble()
		self.cube_array[2][2][0].zDouble()

		self.update()
	
	def bWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(2):
					self.cube_array[x][y][z].zPrime()
		self.cube_array[1][1][2].zPrime()
		
		self.update()
	
	def bPrimeWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(2):
					self.cube_array[x][y][z].z()
		self.cube_array[1][1][2].z()
		
		self.update()
	
	def bDoubleWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(2):
					self.cube_array[x][y][z].zDouble()
		self.cube_array[1][1][2].zDouble()
		
		self.update()

	def l(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		self.cube_array[0][0][0].xPrime()
		self.cube_array[0][0][1].xPrime()
		self.cube_array[0][0][2].xPrime()
		self.cube_array[0][1][0].xPrime()
		self.cube_array[0][1][2].xPrime()
		self.cube_array[0][2][0].xPrime()
		self.cube_array[0][2][1].xPrime()
		self.cube_array[0][2][2].xPrime()

		self.update()

	def lPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		self.cube_array[0][0][0].x()
		self.cube_array[0][0][1].x()
		self.cube_array[0][0][2].x()
		self.cube_array[0][1][0].x()
		self.cube_array[0][1][2].x()
		self.cube_array[0][2][0].x()
		self.cube_array[0][2][1].x()
		self.cube_array[0][2][2].x()

		self.update()

	def lDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp
		
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		self.cube_array[0][0][0].xDouble()
		self.cube_array[0][0][1].xDouble()
		self.cube_array[0][0][2].xDouble()
		self.cube_array[0][1][0].xDouble()
		self.cube_array[0][1][2].xDouble()
		self.cube_array[0][2][0].xDouble()
		self.cube_array[0][2][1].xDouble()
		self.cube_array[0][2][2].xDouble()

		self.update()
	
	def lWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp
		
		for x in range(2):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xPrime()
		self.cube_array[2][1][1].xPrime()

		self.update()
	
	def lPrimeWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp
		
		for x in range(2):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].x()
		self.cube_array[2][1][1].x()
		
		self.update()
	
	def lDoubleWide(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		for x in range(2):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xDouble()
		self.cube_array[2][1][1].xDouble()
		
		self.update()

	def m(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[0][1][1].x()
		self.cube_array[1][0][0].x()
		self.cube_array[1][0][1].x()
		self.cube_array[1][0][2].x()
		self.cube_array[1][1][0].x()
		self.cube_array[1][1][1].x()
		self.cube_array[1][1][2].x()
		self.cube_array[1][2][0].x()
		self.cube_array[1][2][1].x()
		self.cube_array[1][2][2].x()
		self.cube_array[2][1][1].x()

		self.update()

	def mPrime(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		self.cube_array[0][1][1].xPrime()
		self.cube_array[1][0][0].xPrime()
		self.cube_array[1][0][1].xPrime()
		self.cube_array[1][0][2].xPrime()
		self.cube_array[1][1][0].xPrime()
		self.cube_array[1][1][1].xPrime()
		self.cube_array[1][1][2].xPrime()
		self.cube_array[1][2][0].xPrime()
		self.cube_array[1][2][1].xPrime()
		self.cube_array[1][2][2].xPrime()
		self.cube_array[2][1][1].xPrime()

		self.update()

	def mDouble(self):
		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		self.cube_array[0][1][1].xDouble()
		self.cube_array[1][0][0].xDouble()
		self.cube_array[1][0][1].xDouble()
		self.cube_array[1][0][2].xDouble()
		self.cube_array[1][1][0].xDouble()
		self.cube_array[1][1][1].xDouble()
		self.cube_array[1][1][2].xDouble()
		self.cube_array[1][2][0].xDouble()
		self.cube_array[1][2][1].xDouble()
		self.cube_array[1][2][2].xDouble()
		self.cube_array[2][1][1].xDouble()

		self.update()

	def e(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp

		self.cube_array[1][0][1].y()
		self.cube_array[0][1][0].y()
		self.cube_array[0][1][1].y()
		self.cube_array[0][1][2].y()
		self.cube_array[1][1][0].y()
		self.cube_array[1][1][1].y()
		self.cube_array[1][1][2].y()
		self.cube_array[2][1][0].y()
		self.cube_array[2][1][1].y()
		self.cube_array[2][1][2].y()
		self.cube_array[1][2][1].y()

		self.update()

	def ePrime(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		self.cube_array[1][0][1].yPrime()
		self.cube_array[0][1][0].yPrime()
		self.cube_array[0][1][1].yPrime()
		self.cube_array[0][1][2].yPrime()
		self.cube_array[1][1][0].yPrime()
		self.cube_array[1][1][1].yPrime()
		self.cube_array[1][1][2].yPrime()
		self.cube_array[2][1][0].yPrime()
		self.cube_array[2][1][1].yPrime()
		self.cube_array[2][1][2].yPrime()
		self.cube_array[1][2][1].yPrime()

		self.update()

	def eDouble(self):
		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		self.cube_array[1][0][1].yDouble()
		self.cube_array[0][1][0].yDouble()
		self.cube_array[0][1][1].yDouble()
		self.cube_array[0][1][2].yDouble()
		self.cube_array[1][1][0].yDouble()
		self.cube_array[1][1][1].yDouble()
		self.cube_array[1][1][2].yDouble()
		self.cube_array[2][1][0].yDouble()
		self.cube_array[2][1][1].yDouble()
		self.cube_array[2][1][2].yDouble()
		self.cube_array[1][2][1].yDouble()

		self.update()

	def s(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		self.cube_array[1][1][0].z()
		self.cube_array[0][0][1].z()
		self.cube_array[0][1][1].z()
		self.cube_array[0][2][1].z()
		self.cube_array[1][0][1].z()
		self.cube_array[1][1][1].z()
		self.cube_array[1][2][1].z()
		self.cube_array[2][0][1].z()
		self.cube_array[2][1][1].z()
		self.cube_array[2][2][1].z()
		self.cube_array[1][1][2].z()

		self.update()

	def sPrime(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		self.cube_array[1][1][0].zPrime()
		self.cube_array[0][0][1].zPrime()
		self.cube_array[0][1][1].zPrime()
		self.cube_array[0][2][1].zPrime()
		self.cube_array[1][0][1].zPrime()
		self.cube_array[1][1][1].zPrime()
		self.cube_array[1][2][1].zPrime()
		self.cube_array[2][0][1].zPrime()
		self.cube_array[2][1][1].zPrime()
		self.cube_array[2][2][1].zPrime()
		self.cube_array[1][1][2].zPrime()

		self.update()

	def sDouble(self):
		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		self.cube_array[1][1][0].zDouble()
		self.cube_array[0][0][1].zDouble()
		self.cube_array[0][1][1].zDouble()
		self.cube_array[0][2][1].zDouble()
		self.cube_array[1][0][1].zDouble()
		self.cube_array[1][1][1].zDouble()
		self.cube_array[1][2][1].zDouble()
		self.cube_array[2][0][1].zDouble()
		self.cube_array[2][1][1].zDouble()
		self.cube_array[2][2][1].zDouble()
		self.cube_array[1][1][2].zDouble()

		self.update()

	def x(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = tmp
		
		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].x()
		
		self.update()

	def xPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp
		
		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xPrime()

		self.update()

	def xDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].xDouble()
		
		self.update()

	def y(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].y()
		
		self.update()

	def yPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].yPrime()
		
		self.update()

	def yDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] =tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][1][0]
		self.cube_array[1][1][0] = self.cube_array[1][1][2]
		self.cube_array[1][1][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].yDouble()
		
		self.update()

	def z(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].z()
		
		self.update()

	def zPrime(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].zPrime()
		
		self.update()

	def zDouble(self):
		tmp = self.cube_array[0][0][0]
		self.cube_array[0][0][0] = self.cube_array[2][2][0]
		self.cube_array[2][2][0] = tmp

		tmp = self.cube_array[0][2][0]
		self.cube_array[0][2][0] = self.cube_array[2][0][0]
		self.cube_array[2][0][0] = tmp

		tmp = self.cube_array[0][0][2]
		self.cube_array[0][0][2] = self.cube_array[2][2][2]
		self.cube_array[2][2][2] = tmp

		tmp = self.cube_array[0][2][2]
		self.cube_array[0][2][2] = self.cube_array[2][0][2]
		self.cube_array[2][0][2] = tmp

		tmp = self.cube_array[0][1][0]
		self.cube_array[0][1][0] = self.cube_array[2][1][0]
		self.cube_array[2][1][0] = tmp

		tmp = self.cube_array[1][0][0]
		self.cube_array[1][0][0] = self.cube_array[1][2][0]
		self.cube_array[1][2][0] = tmp

		tmp = self.cube_array[0][0][1]
		self.cube_array[0][0][1] = self.cube_array[2][2][1]
		self.cube_array[2][2][1] = tmp

		tmp = self.cube_array[0][2][1]
		self.cube_array[0][2][1] = self.cube_array[2][0][1]
		self.cube_array[2][0][1] = tmp

		tmp = self.cube_array[0][1][2]
		self.cube_array[0][1][2] = self.cube_array[2][1][2]
		self.cube_array[2][1][2] = tmp

		tmp = self.cube_array[1][0][2]
		self.cube_array[1][0][2] = self.cube_array[1][2][2]
		self.cube_array[1][2][2] = tmp

		tmp = self.cube_array[0][1][1]
		self.cube_array[0][1][1] = self.cube_array[2][1][1]
		self.cube_array[2][1][1] = tmp

		tmp = self.cube_array[1][0][1]
		self.cube_array[1][0][1] = self.cube_array[1][2][1]
		self.cube_array[1][2][1] = tmp

		for x in range(3):
			for y in range(3):
				for z in range(3):
					self.cube_array[x][y][z].zDouble()
		
		self.update()
	
	def update(self):
		self.cube["U"][0][0] = self.cube_array[0][0][0].sides["U"]
		self.cube["U"][1][0] = self.cube_array[1][0][0].sides["U"]
		self.cube["U"][2][0] = self.cube_array[2][0][0].sides["U"]
		self.cube["U"][0][1] = self.cube_array[0][0][1].sides["U"]
		self.cube["U"][1][1] = self.cube_array[1][0][1].sides["U"]
		self.cube["U"][2][1] = self.cube_array[2][0][1].sides["U"]
		self.cube["U"][0][2] = self.cube_array[0][0][2].sides["U"]
		self.cube["U"][1][2] = self.cube_array[1][0][2].sides["U"]
		self.cube["U"][2][2] = self.cube_array[2][0][2].sides["U"]

		self.cube["F"][0][0] = self.cube_array[0][0][2].sides["F"]
		self.cube["F"][1][0] = self.cube_array[1][0][2].sides["F"]
		self.cube["F"][2][0] = self.cube_array[2][0][2].sides["F"]
		self.cube["F"][0][1] = self.cube_array[0][1][2].sides["F"]
		self.cube["F"][1][1] = self.cube_array[1][1][2].sides["F"]
		self.cube["F"][2][1] = self.cube_array[2][1][2].sides["F"]
		self.cube["F"][0][2] = self.cube_array[0][2][2].sides["F"]
		self.cube["F"][1][2] = self.cube_array[1][2][2].sides["F"]
		self.cube["F"][2][2] = self.cube_array[2][2][2].sides["F"]

		self.cube["R"][0][0] = self.cube_array[2][0][2].sides["R"]
		self.cube["R"][1][0] = self.cube_array[2][0][1].sides["R"]
		self.cube["R"][2][0] = self.cube_array[2][0][0].sides["R"]
		self.cube["R"][0][1] = self.cube_array[2][1][2].sides["R"]
		self.cube["R"][1][1] = self.cube_array[2][1][1].sides["R"]
		self.cube["R"][2][1] = self.cube_array[2][1][0].sides["R"]
		self.cube["R"][0][2] = self.cube_array[2][2][2].sides["R"]
		self.cube["R"][1][2] = self.cube_array[2][2][1].sides["R"]
		self.cube["R"][2][2] = self.cube_array[2][2][0].sides["R"]

		self.cube["D"][0][0] = self.cube_array[0][2][0].sides["D"]
		self.cube["D"][1][0] = self.cube_array[1][2][0].sides["D"]
		self.cube["D"][2][0] = self.cube_array[2][2][0].sides["D"]
		self.cube["D"][0][1] = self.cube_array[0][2][1].sides["D"]
		self.cube["D"][1][1] = self.cube_array[1][2][1].sides["D"]
		self.cube["D"][2][1] = self.cube_array[2][2][1].sides["D"]
		self.cube["D"][0][2] = self.cube_array[0][2][2].sides["D"]
		self.cube["D"][1][2] = self.cube_array[1][2][2].sides["D"]
		self.cube["D"][2][2] = self.cube_array[2][2][2].sides["D"]

		self.cube["B"][0][0] = self.cube_array[0][0][0].sides["B"]
		self.cube["B"][1][0] = self.cube_array[1][0][0].sides["B"]
		self.cube["B"][2][0] = self.cube_array[2][0][0].sides["B"]
		self.cube["B"][0][1] = self.cube_array[0][1][0].sides["B"]
		self.cube["B"][1][1] = self.cube_array[1][1][0].sides["B"]
		self.cube["B"][2][1] = self.cube_array[2][1][0].sides["B"]
		self.cube["B"][0][2] = self.cube_array[0][2][0].sides["B"]
		self.cube["B"][1][2] = self.cube_array[1][2][0].sides["B"]
		self.cube["B"][2][2] = self.cube_array[2][2][0].sides["B"]

		self.cube["L"][0][0] = self.cube_array[0][0][0].sides["L"]
		self.cube["L"][1][0] = self.cube_array[0][0][1].sides["L"]
		self.cube["L"][2][0] = self.cube_array[0][0][2].sides["L"]
		self.cube["L"][0][1] = self.cube_array[0][1][0].sides["L"]
		self.cube["L"][1][1] = self.cube_array[0][1][1].sides["L"]
		self.cube["L"][2][1] = self.cube_array[0][1][2].sides["L"]
		self.cube["L"][0][2] = self.cube_array[0][2][0].sides["L"]
		self.cube["L"][1][2] = self.cube_array[0][2][1].sides["L"]
		self.cube["L"][2][2] = self.cube_array[0][2][2].sides["L"]

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

		display_pointer[0].pixel_data[(padx + 2, pady + 5)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 3, pady + 5)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 1, pady + 6)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 2, pady + 6)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 3, pady + 6)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 4, pady + 6)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 2, pady + 7)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 3, pady + 7)] = self.color_dict[self.cube["U"][0][2]]

		display_pointer[0].pixel_data[(padx + 8, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 7, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 7)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 7)] = self.color_dict[self.cube["U"][1][1]]

		display_pointer[0].pixel_data[(padx + 14, pady + 5)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 15, pady + 5)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 13, pady + 6)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 14, pady + 6)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 15, pady + 6)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 16, pady + 6)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 14, pady + 7)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 15, pady + 7)] = self.color_dict[self.cube["U"][2][0]]

		display_pointer[0].pixel_data[(padx + 5, pady + 7)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 6, pady + 7)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 4, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 5, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 6, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 7, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 5, pady + 9)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 6, pady + 9)] = self.color_dict[self.cube["U"][1][2]]

		display_pointer[0].pixel_data[(padx + 11, pady + 7)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 12, pady + 7)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 8)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 11, pady + 8)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 12, pady + 8)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 13, pady + 8)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 11, pady + 9)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 12, pady + 9)] = self.color_dict[self.cube["U"][2][1]]

		display_pointer[0].pixel_data[(padx + 8, pady + 9)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 9, pady + 9)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 7, pady + 10)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 10)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 9, pady + 10)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 10, pady + 10)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 11)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 9, pady + 11)] = self.color_dict[self.cube["U"][2][2]]

		display_pointer[0].pixel_data[(padx + 1, pady + 7)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 1, pady + 8)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 8)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 9)] = self.color_dict[self.cube["F"][0][0]]

		display_pointer[0].pixel_data[(padx + 1, pady + 10)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 1, pady + 11)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 2, pady + 11)] = self.color_dict[self.cube["F"][0][1]]
		display_pointer[0].pixel_data[(padx + 2, pady + 12)] = self.color_dict[self.cube["F"][0][1]]

		display_pointer[0].pixel_data[(padx + 1, pady + 13)] = self.color_dict[self.cube["F"][0][2]]
		display_pointer[0].pixel_data[(padx + 1, pady + 14)] = self.color_dict[self.cube["F"][0][2]]
		display_pointer[0].pixel_data[(padx + 2, pady + 14)] = self.color_dict[self.cube["F"][0][2]]
		display_pointer[0].pixel_data[(padx + 2, pady + 15)] = self.color_dict[self.cube["F"][0][2]]

		display_pointer[0].pixel_data[(padx + 4, pady + 9)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 11)] = self.color_dict[self.cube["F"][1][0]]

		display_pointer[0].pixel_data[(padx + 4, pady + 12)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 4, pady + 13)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 13)] = self.color_dict[self.cube["F"][1][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 14)] = self.color_dict[self.cube["F"][1][1]]

		display_pointer[0].pixel_data[(padx + 4, pady + 15)] = self.color_dict[self.cube["F"][1][2]]
		display_pointer[0].pixel_data[(padx + 4, pady + 16)] = self.color_dict[self.cube["F"][1][2]]
		display_pointer[0].pixel_data[(padx + 5, pady + 16)] = self.color_dict[self.cube["F"][1][2]]
		display_pointer[0].pixel_data[(padx + 5, pady + 17)] = self.color_dict[self.cube["F"][1][2]]

		display_pointer[0].pixel_data[(padx + 7, pady + 11)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 7, pady + 12)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 12)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 13)] = self.color_dict[self.cube["F"][2][0]]

		display_pointer[0].pixel_data[(padx + 7, pady + 14)] = self.color_dict[self.cube["F"][2][1]]
		display_pointer[0].pixel_data[(padx + 7, pady + 15)] = self.color_dict[self.cube["F"][2][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 15)] = self.color_dict[self.cube["F"][2][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 16)] = self.color_dict[self.cube["F"][2][1]]

		display_pointer[0].pixel_data[(padx + 7, pady + 17)] = self.color_dict[self.cube["F"][2][2]]
		display_pointer[0].pixel_data[(padx + 7, pady + 18)] = self.color_dict[self.cube["F"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 18)] = self.color_dict[self.cube["F"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 19)] = self.color_dict[self.cube["F"][2][2]]

		display_pointer[0].pixel_data[(padx + 16, pady + 7)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 16, pady + 8)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 15, pady + 8)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 15, pady + 9)] = self.color_dict[self.cube["R"][2][0]]

		display_pointer[0].pixel_data[(padx + 16, pady + 10)] = self.color_dict[self.cube["R"][2][1]]
		display_pointer[0].pixel_data[(padx + 16, pady + 11)] = self.color_dict[self.cube["R"][2][1]]
		display_pointer[0].pixel_data[(padx + 15, pady + 11)] = self.color_dict[self.cube["R"][2][1]]
		display_pointer[0].pixel_data[(padx + 15, pady + 12)] = self.color_dict[self.cube["R"][2][1]]

		display_pointer[0].pixel_data[(padx + 16, pady + 13)] = self.color_dict[self.cube["R"][2][2]]
		display_pointer[0].pixel_data[(padx + 16, pady + 14)] = self.color_dict[self.cube["R"][2][2]]
		display_pointer[0].pixel_data[(padx + 15, pady + 14)] = self.color_dict[self.cube["R"][2][2]]
		display_pointer[0].pixel_data[(padx + 15, pady + 15)] = self.color_dict[self.cube["R"][2][2]]

		display_pointer[0].pixel_data[(padx + 13, pady + 9)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 13, pady + 10)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 10)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 12, pady + 11)] = self.color_dict[self.cube["R"][1][0]]

		display_pointer[0].pixel_data[(padx + 13, pady + 12)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 13, pady + 13)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 12, pady + 13)] = self.color_dict[self.cube["R"][1][1]]
		display_pointer[0].pixel_data[(padx + 12, pady + 14)] = self.color_dict[self.cube["R"][1][1]]

		display_pointer[0].pixel_data[(padx + 13, pady + 15)] = self.color_dict[self.cube["R"][1][2]]
		display_pointer[0].pixel_data[(padx + 13, pady + 16)] = self.color_dict[self.cube["R"][1][2]]
		display_pointer[0].pixel_data[(padx + 12, pady + 16)] = self.color_dict[self.cube["R"][1][2]]
		display_pointer[0].pixel_data[(padx + 12, pady + 17)] = self.color_dict[self.cube["R"][1][2]]

		display_pointer[0].pixel_data[(padx + 10, pady + 11)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 12)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 12)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 13)] = self.color_dict[self.cube["R"][0][0]]

		display_pointer[0].pixel_data[(padx + 10, pady + 14)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 10, pady + 15)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 15)] = self.color_dict[self.cube["R"][0][1]]
		display_pointer[0].pixel_data[(padx + 9, pady + 16)] = self.color_dict[self.cube["R"][0][1]]

		display_pointer[0].pixel_data[(padx + 10, pady + 17)] = self.color_dict[self.cube["R"][0][2]]
		display_pointer[0].pixel_data[(padx + 10, pady + 18)] = self.color_dict[self.cube["R"][0][2]]
		display_pointer[0].pixel_data[(padx + 9, pady + 18)] = self.color_dict[self.cube["R"][0][2]]
		display_pointer[0].pixel_data[(padx + 9, pady + 19)] = self.color_dict[self.cube["R"][0][2]]

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
	
	def drawTopdown(self, display_pointer, padx=0, pady=0, init=False):
		display_pointer[0].pixel_data[(padx + 1, pady + 3)] = self.color_dict[self.cube["L"][0][0]]
		display_pointer[0].pixel_data[(padx + 1, pady + 4)] = self.color_dict[self.cube["L"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 3)] = self.color_dict[self.cube["L"][0][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 4)] = self.color_dict[self.cube["L"][0][0]]
		
		display_pointer[0].pixel_data[(padx + 1, pady + 5)] = self.color_dict[self.cube["L"][1][0]]
		display_pointer[0].pixel_data[(padx + 1, pady + 6)] = self.color_dict[self.cube["L"][1][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 5)] = self.color_dict[self.cube["L"][1][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 6)] = self.color_dict[self.cube["L"][1][0]]
		
		display_pointer[0].pixel_data[(padx + 1, pady + 7)] = self.color_dict[self.cube["L"][2][0]]
		display_pointer[0].pixel_data[(padx + 1, pady + 8)] = self.color_dict[self.cube["L"][2][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 7)] = self.color_dict[self.cube["L"][2][0]]
		display_pointer[0].pixel_data[(padx + 2, pady + 8)] = self.color_dict[self.cube["L"][2][0]]
		
		display_pointer[0].pixel_data[(padx + 3, pady + 1)] = self.color_dict[self.cube["B"][0][0]]
		display_pointer[0].pixel_data[(padx + 3, pady + 2)] = self.color_dict[self.cube["B"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 1)] = self.color_dict[self.cube["B"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 2)] = self.color_dict[self.cube["B"][0][0]]
		
		display_pointer[0].pixel_data[(padx + 3, pady + 3)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 3, pady + 4)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 3)] = self.color_dict[self.cube["U"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 4)] = self.color_dict[self.cube["U"][0][0]]
		
		display_pointer[0].pixel_data[(padx + 3, pady + 5)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 3, pady + 6)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 4, pady + 5)] = self.color_dict[self.cube["U"][0][1]]
		display_pointer[0].pixel_data[(padx + 4, pady + 6)] = self.color_dict[self.cube["U"][0][1]]
		
		display_pointer[0].pixel_data[(padx + 3, pady + 7)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 3, pady + 8)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 4, pady + 7)] = self.color_dict[self.cube["U"][0][2]]
		display_pointer[0].pixel_data[(padx + 4, pady + 8)] = self.color_dict[self.cube["U"][0][2]]
		
		display_pointer[0].pixel_data[(padx + 3, pady + 9)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 3, pady + 10)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 9)] = self.color_dict[self.cube["F"][0][0]]
		display_pointer[0].pixel_data[(padx + 4, pady + 10)] = self.color_dict[self.cube["F"][0][0]]
		
		display_pointer[0].pixel_data[(padx + 5, pady + 1)] = self.color_dict[self.cube["B"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 2)] = self.color_dict[self.cube["B"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 1)] = self.color_dict[self.cube["B"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 2)] = self.color_dict[self.cube["B"][1][0]]
		
		display_pointer[0].pixel_data[(padx + 5, pady + 3)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 3)] = self.color_dict[self.cube["U"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 4)] = self.color_dict[self.cube["U"][1][0]]
		
		display_pointer[0].pixel_data[(padx + 5, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 5, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 6, pady + 5)] = self.color_dict[self.cube["U"][1][1]]
		display_pointer[0].pixel_data[(padx + 6, pady + 6)] = self.color_dict[self.cube["U"][1][1]]
		
		display_pointer[0].pixel_data[(padx + 5, pady + 7)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 5, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 6, pady + 7)] = self.color_dict[self.cube["U"][1][2]]
		display_pointer[0].pixel_data[(padx + 6, pady + 8)] = self.color_dict[self.cube["U"][1][2]]
		
		display_pointer[0].pixel_data[(padx + 5, pady + 9)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 5, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 9)] = self.color_dict[self.cube["F"][1][0]]
		display_pointer[0].pixel_data[(padx + 6, pady + 10)] = self.color_dict[self.cube["F"][1][0]]
		
		display_pointer[0].pixel_data[(padx + 7, pady + 1)] = self.color_dict[self.cube["B"][2][0]]
		display_pointer[0].pixel_data[(padx + 7, pady + 2)] = self.color_dict[self.cube["B"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 1)] = self.color_dict[self.cube["B"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 2)] = self.color_dict[self.cube["B"][2][0]]
		
		display_pointer[0].pixel_data[(padx + 7, pady + 3)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 7, pady + 4)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 3)] = self.color_dict[self.cube["U"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 4)] = self.color_dict[self.cube["U"][2][0]]
		
		display_pointer[0].pixel_data[(padx + 7, pady + 5)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 7, pady + 6)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 5)] = self.color_dict[self.cube["U"][2][1]]
		display_pointer[0].pixel_data[(padx + 8, pady + 6)] = self.color_dict[self.cube["U"][2][1]]
		
		display_pointer[0].pixel_data[(padx + 7, pady + 7)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 7, pady + 8)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 7)] = self.color_dict[self.cube["U"][2][2]]
		display_pointer[0].pixel_data[(padx + 8, pady + 8)] = self.color_dict[self.cube["U"][2][2]]
		
		display_pointer[0].pixel_data[(padx + 7, pady + 9)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 7, pady + 10)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 9)] = self.color_dict[self.cube["F"][2][0]]
		display_pointer[0].pixel_data[(padx + 8, pady + 10)] = self.color_dict[self.cube["F"][2][0]]
		
		display_pointer[0].pixel_data[(padx + 9, pady + 3)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 4)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 3)] = self.color_dict[self.cube["R"][2][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 4)] = self.color_dict[self.cube["R"][2][0]]
		
		display_pointer[0].pixel_data[(padx + 9, pady + 5)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 6)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 5)] = self.color_dict[self.cube["R"][1][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 6)] = self.color_dict[self.cube["R"][1][0]]
		
		display_pointer[0].pixel_data[(padx + 9, pady + 7)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 9, pady + 8)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 7)] = self.color_dict[self.cube["R"][0][0]]
		display_pointer[0].pixel_data[(padx + 10, pady + 8)] = self.color_dict[self.cube["R"][0][0]]