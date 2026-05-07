from utils.package_installer import installRequiredPackages
installRequiredPackages()

from utils.selectionWindow import SelectionWindow
from utils.program_library import library

import subprocess
import os
from os import listdir
from os.path import isfile, join

base_folder = "./programs"
program_name_list = []
program_path_list = []
program_cmd_list = []
for program in library.keys():
	program_name_list.append(program)
	program_path_list.append(library[program]["path"])
	program_cmd_list.append(library[program]["cmd"])

done = False
while not done:
	try:
		window = SelectionWindow(program_name_list, "Select program to launch")
		window.mainloop()
		if not window.canceled:
			program_name = window.selection_listbox.get(window.selection_listbox.curselection()[0])
			window.destroy()
			window = None
		else:
			done = True
			window.destroy()
			continue

		program_path = program_path_list[program_name_list.index(program_name)]
		cmd = program_cmd_list[program_name_list.index(program_name)]

		if not len(program_path) <= 0:
			os.system(f"python program_launcher.py {cmd} {program_path}")
	except KeyboardInterrupt:
		pass