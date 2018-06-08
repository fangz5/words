import os.path
import urllib.request
from django.core.exceptions import ValidationError

from pygame import mixer

class SoundManager(object):
	def __init__(object):		
		mixer.init()

	def soundExists(self, word):
		return os.path.isfile('sound/' + word + '.mp3')

	def download(self, word):
		if not word: return
		url = 'https://ssl.gstatic.com/dictionary/static/sounds/oxford/' + word + '--_gb_1.mp3'
		try:
			urllib.request.urlretrieve(url, 'sound/' + word + '.mp3')
		except (urllib.error.HTTPError, urllib.error.URLError) as e:
			pass

	def downloadList(self, words):
		for word in words:
			if not self.soundExists(word):
				self.download(word)

	def play(self, word):
		if self.soundExists(word):
			mixer.music.load('sound/' + word + '.mp3')
			mixer.music.play()

