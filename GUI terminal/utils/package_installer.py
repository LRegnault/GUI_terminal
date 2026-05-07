import sys
import subprocess
import os

def installRequiredPackages():
	required_packages = []
	with open("./utils/required_packages.txt", "r") as file:
		required_packages = file.readlines()

	for package in required_packages:
		subprocess.check_call([sys.executable, "-m", "pip", "install", package.replace("\n", "")])
	os.system("cls")