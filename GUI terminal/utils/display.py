import os
import threading
import time

os.system("")

class Display:
	def __init__(self, width, height, scale, ratio, refresh_rate):
		os.system("cls")
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
		
		self.close_event = threading.Event()
		
		self.refresh_thread = threading.Thread(target=self.refresh, daemon=True)
		self.refresh_thread.start()
	
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
		while not self.close_event.is_set():
			self.update()
			time.sleep(1 / self.refresh_rate)
	
	def close(self):
		self.close_event.set()

if __name__ == "__main__":
	try:
		width = 16
		height = 16
		scale = 2
		ratio = (2, 1)
		refresh_rate = 60

		display_pointer = [Display(width, height, scale, ratio, refresh_rate)]
		
		i = 0
		while True:
			if i % 256 == 0:
				i = 0
			for y in range(height):
				for x in range(width):
					r = x * (i // width) % 256
					g = y * (i // height) % 256
					b = max(i - (r + g), 0)
					display_pointer[0].updatePixel(x, y, r, g, b)
			i += 1
	except KeyboardInterrupt:
		pass