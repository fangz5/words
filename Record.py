import random

class Record(object):
	def __init__(self):
		self.allWords = self._load_('save.csv')
		self.numWordsReview = 20

	def _save_(self, words, fileName):
		with open(fileName, 'w') as file:
			for word in words:
				file.write(word +',' + str(words[word]) + '\n')

	def _load_(self, fileName):
		words = {}
		with open(fileName, 'r') as file:
			for line in file:
				word, weight = line.split(',')
				words[word] = int(weight)
		return words

	def loadWords(self):
		if not self.allWords: return []
		population = list(self.allWords.items())
		weights = list(map(lambda word_weight: word_weight[1], population))
		samplesWithReplacement = random.choices(population, weights=weights, k=self.numWordsReview)
		return list(map(lambda pair: list(pair), set(samplesWithReplacement)))
			
	def saveUpdate(self, wordList):
		for word, weight in wordList:
			self.allWords[word] = weight
		self._save_(self.allWords, 'save.csv')



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
