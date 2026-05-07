from utils.display import Display
import time

def run():
	try:
		width = 16
		height = 16
		scale = 2
		ratio = (2, 1)
		refresh_rate = 60

		display_pointer = [Display(width, height, scale, ratio, refresh_rate)]

		i = 0
		decrease = False
		while True:
			# if i % 256 == 0:
			# 	i = 0
			if i == 0:
				decrease = False
			elif i == 256:
				decrease = True
			for y in range(height):
				for x in range(width):
					r = x * (i // width) % 256
					g = y * (i // height) % 256
					b = max(i - (r + g), 0)
					display_pointer[0].updatePixel(x, y, r, g, b)
			if decrease:
				i -= 1
			else:
				i += 1
			time.sleep(1/120)
	except KeyboardInterrupt:
		pass