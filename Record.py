import random

class Record(object):
	def __init__(self):
		allWords = self._loadAll_()

	def _save_(self, words, fileName):
		with open(fileName, 'w') as file:
			for word in words:
				file.write(word +',' + str(words[word]) + '\n')

	def save(self, words):
		self._save_(words, 'save')

	def _load_(self, fileName):
		words = []
		with open(fileName, 'r') as file:
			for line in file:
				word, weight = line.split(',')
				words.append([word, int(weight)])
		return words

	def _loadAll_(self):
		self.allWords = self._load_('save')

	def loadWords(self):
		if not self.allWords: return []
		weights = list(map(lambda word_weight: word_weight[1], self.allWords))
		return random.choices(self.allWords, weights=weights, k=min(20, len(weights)))
			
	def saveUpdate(self, wordList):
		words = {}
		for word, weight in wordList:
			words[word] = weight
		self.save(words)



if __name__ == '__main__':
	print("test-record")

	record = Record()
	words = {'hello':5, 'apple':10}
	record._save_(words, 'testSave')

	words = record._load_('testSave')
	print(words)
	
	import os
	os.system('rm testSave')

	print(record.allWords)
