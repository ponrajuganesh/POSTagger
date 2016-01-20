import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import nltk.data
import nltk.help

def buildhtml(tokenized_sentence, sentence_count):
	html = ""
	starting_div = "<div class=\"panel panel-primary\"> <div class=\"panel-heading\"> Sentence "+ str(sentence_count) +"</div><div class=\"panel-body\">"
	ending_div = "</div></div>"
	html += starting_div
	try:
	    for token in tokenized_sentence:
	    	words = nltk.word_tokenize(token)
	    	tagged = nltk.pos_tag(words)
	    	for word in tagged:
	    		if word[1] in tagdict:
	    			html += "<a href=\"#\" data-toggle=\"tooltip\" title=\""+tagdict[word[1]][0]+"\">"+word[0]+"</a>"
	    	html += ending_div

	    	return html
	except Exception as e:
		print(str(e))

text = state_union.raw("/Users/ponrajuganesh/Desktop/data.txt") 
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

tagdict = nltk.data.load("help/tagsets/" + "upenn_tagset" + ".pickle")
count = 0
fulldiv = ""
for sentence in sent_detector.tokenize(text):
	count += 1
	custom_sent_tokenizer = PunktSentenceTokenizer()
	fulldiv += buildhtml(custom_sent_tokenizer.tokenize(sentence), count)

print fulldiv