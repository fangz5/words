from appJar import gui
from collections import deque

from SoundManager import *
from Record import *

app = gui("", "800x600")

sound = SoundManager()
record = Record()

unlearned = deque([])
learned = []

def disable(buttons):
	for b in buttons:
		app.disableButton(b)

def enable(buttons):
	for b in buttons:
		app.enableButton(b)

def refresh():
	print(learned)
	app.setLabel("learned", (" " * 5).join(list(map(lambda l: l[0], learned))))
	app.setLabel("not learned", (" " * 5).join(list(map(lambda l: l[0], unlearned))))
	if not unlearned:
		app.setLabel("word", "Good job, Olivia! All done!")
		record.saveUpdate(learned)
		disable(["Next"])

def add(button):
	words = app.getEntry("Add Words").split()
	self.sound.downloadList(words)
	for word in words:
		unlearned.append([word, 10])
	enable(["Next"])
	refresh()

def next_word(button):
	if unlearned:
		app.setLabel("word", unlearned[0][0])
	enable(["Correct", "Wrong"])


def check(button):
	curr = unlearned.popleft()
	if button == "Correct":
		curr[1] = max(1, curr[1] - 1)
		learned.append(curr)
	elif button == "Wrong":
		curr[1] += 1
		unlearned.append(curr)
	refresh()
	disable(["Correct", "Wrong"])

def play(button):
	word = app.getLabel("word")
	sound.play(word)

def load(button):
	unlearned.extend(record.loadWords())
	enable(["Next"])
	refresh()

app.addButtons(["Load Words"], load)

app.addLabelEntry("Add Words")
app.addButtons(["Add"], add)

app.addLabel("learned", "")
app.setLabelBg("learned", "light green")
app.addLabel("not learned", "")
app.setLabelBg("not learned", "pink")

app.addButtons(["Next"], next_word)

app.addLabel("word", "")
app.getLabelWidget("word").config(font=("Courier", "24", "bold"))
app.setLabelBg("word", "white")

app.addButtons(["Correct", "Wrong"], check)
app.addButtons(["Play sound"], play)
disable(["Next", "Correct", "Wrong"])

app.go()
