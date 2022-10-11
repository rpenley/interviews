#!/usr/bin/python3

import sys

def tokenize(text):
	sentenceList = text.split('.')
	returnList = []
	for sentence in sentenceList:
		returnList.append(sentence.split())	
	return returnList

def readFile(filename):
	try:
		with open(filename, 'r') as file:
			return file.read()
	except IndexError:
		print("ERROR: empty argument list, no text file was provided")

def formattedPrint(sentenceList):
	sentenceSize = 0
	for sentence in sentenceList:
		for word in sentence:
			if sentenceSize > 40:
				print(word, end='\n')
				sentenceSize = 0
			elif word.find('.') == -1:
				print(word, end=' ')
			else:
				print(word, end='\n')	
			sentenceSize += len(word)

document = readFile(sys.argv[1])
parsedDoc = tokenize(document)
formattedPrint(parsedDoc)
#print(parsedDoc)
