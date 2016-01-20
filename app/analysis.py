from nltk.corpus import wordnet
import collections
from nltk.tokenize import PunktSentenceTokenizer
import nltk.data


class NLTKanalysis():

	def __init__(self):
		self.sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		self.tagdict = nltk.data.load("help/tagsets/" + "upenn_tagset" + ".pickle")

	def analysis(self, text):
		paragraphs = text.split('\n')

		result = []

		for paragraph in paragraphs:
			result.append(self.pos(paragraph))

		return result
		
	def pos(self, paragraph):

		wordsdict = collections.OrderedDict()
		sent_tokenizer = PunktSentenceTokenizer()

		for sentence in self.sent_detector.tokenize(paragraph):
			tokens = sent_tokenizer.tokenize(sentence)

			for token in tokens:
				words = nltk.word_tokenize(token)
				tagged = nltk.pos_tag(words)
				for word in tagged:
					if word[1] in self.tagdict:
						wordsdict[word[0]] = self.tagdict[word[1]][0]

		return wordsdict
