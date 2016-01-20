from nltk.corpus import wordnet
import collections

class NLTKanalysis():

	def pos(self, text):
		paragraphs = text.split('\n')

		result = []

		for paragraph from paragraphs:
			

		synonymsdict = collections.OrderedDict()
		
		for word in words:
			if len(word) > 3:
				synonymsdict[word] = self.fetchsynonyms(word)
			else:
				synonymsdict[word] = ""

		return synonymsdict

	
	def fetchsynonyms(self, synword):
		syns = {}

		for syn in wordnet.synsets(synword):
			for l in syn.lemmas():
				word = l.name().strip()
				if word not in syns:
					syns[word] = 1

		return " ".join(syns.keys())