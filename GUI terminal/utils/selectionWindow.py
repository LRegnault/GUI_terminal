import tkinter as tk

class SelectionWindow(tk.Tk):
	def __init__(self, item_list, querry):
		super().__init__()
		
		self.canceled = False

		self.protocol("WM_DELETE_WINDOW", self.__callback)
		self.geometry("500x225+100+100")

		self.title(querry)

		self.listbox_frame = tk.Frame(self)
		self.listbox_scrollbar = tk.Scrollbar(self.listbox_frame)
		self.selection_listbox = tk.Listbox(self.listbox_frame, selectmode=tk.SINGLE, width=78, yscrollcommand=self.listbox_scrollbar.set)
		
		self.confirm_button = tk.Button(self, text="Launch", command=self.confirmSelection, width=10, height=3)
		self.cancel_button = tk.Button(self, text="Close", command=self.cancel, width=10, height=3)
		
		for item in item_list:
			self.selection_listbox.insert(tk.END, item)
		
		self.listbox_scrollbar.config(command=self.selection_listbox.yview)

		self.listbox_frame.grid(column=0, columnspan=2, row=1, padx=7)
		self.confirm_button.grid(column=1, row=2, pady=3, sticky=tk.E)
		self.cancel_button.grid(column=0, row=2, pady=3, padx=3, sticky=tk.W)

		self.selection_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		self.listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	
	def __callback(self):
		self.cancel()
	
	def confirmSelection(self):
		if len(self.selection_listbox.curselection()) == 0:
			return
		self.quit()
	
	def cancel(self):
		self.canceled = True
		self.quit()