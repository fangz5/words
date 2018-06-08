from appJar import gui
from collections import deque

from SoundManager import *
from Record import *

class UI(object):
	def __init__(self):
		self.sound = SoundManager()
		self.record = Record()
		self.learned = []
		self.unlearned = deque([])
		self.window = gui("", "800x600")

	def disable(self, buttons):
		for b in buttons:
			self.window.disableButton(b)

	def enable(self, buttons):
		for b in buttons:
			self.window.enableButton(b)

	def refresh(self):
		self.window.setLabel("learned", (" " * 5).join(list(map(lambda l: l[0], self.learned))))
		self.window.setLabel("not learned", (" " * 5).join(list(map(lambda l: l[0], self.unlearned))))
		if not self.unlearned:
			self.window.setLabel("word", "Good job, Olivia! All done!")
			self.record.saveUpdate(self.learned)
			self.disable(["Next"])

	def add(self, button):
		words = self.window.getEntry("Add Words").split()
		self.sound.downloadList(words)
		for word in words:
			self.unlearned.append([word, 10])
		self.enable(["Next"])
		self.refresh()

	def nextWord(self, button):
		if self.unlearned:
			self.window.setLabel("word", self.unlearned[0][0])
			self.enable(["Correct", "Wrong"])

	def check(self, button):
		curr = self.unlearned.popleft()
		if button == "Correct":
			curr[1] = max(1, curr[1] - 1)
			self.learned.append(curr)
		elif button == "Wrong":
			curr[1] += 1
			self.unlearned.append(curr)
		self.refresh()
		self.disable(["Correct", "Wrong"])

	def play(self, button):
		word = self.window.getLabel("word")
		if word:
			self.sound.play(word)

	def load(self, button):
		self.unlearned.extend(self.record.loadWords())
		if self.unlearned:
			self.enable(["Next"])
		self.refresh()

	def run(self):
		self.window.addButtons(["Load Words"], self.load)

		self.window.addLabelEntry("Add Words")
		self.window.addButtons(["Add"], self.add)

		self.window.addLabel("learned", "")
		self.window.setLabelBg("learned", "light green")
		self.window.addLabel("not learned", "")
		self.window.setLabelBg("not learned", "pink")
		
		self.window.addButtons(["Next"], self.nextWord)
		
		self.window.addLabel("word", "")
		self.window.getLabelWidget("word").config(font=("Courier", "24", "bold"))
		self.window.setLabelBg("word", "white")
		
		self.window.addButtons(["Correct", "Wrong"], self.check)
		self.window.addButtons(["Play sound"], self.play)
		self.disable(["Next", "Correct", "Wrong", "Play sound"])
		
		self.window.go()
