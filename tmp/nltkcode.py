from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def fetchsynonyms():
	input_positive_words=["happy"]

	positive_words = {}

	for word in input_positive_words:
		for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				word = l.name().strip()
				if word not in positive_words:
					positive_words[word] = 1

	return positive_words.keys()

if __name__ == '__main__':
	print fetchsynonyms()