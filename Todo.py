import time

import utils

class Todo:
	def __init__(self, content: str) -> None:
		self.content = content
		self.ts = time.strftime("%H:%M:%S", time.localtime())
		self.done = False
		self.id = utils.get_id()

	def mark_done(self):
		self.done = True
	
