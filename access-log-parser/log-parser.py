#!/usr/bin/python3

import sys

def readFile(filename):
	try:
		with open(filename, 'r') as file:
			return file.read()
	except IndexError:
		print("ERROR: empty argument list, no text file was provided")

def printReturnCodes(log):
    print("200: " + str(log.count(" 200 ")))
    print("404: " + str(log.count(" 404 ")))
    print("400: " + str(log.count(" 400 ")))
    print("302: " + str(log.count(" 302 ")))
    print("202: " + str(log.count(" 202 ")))
    print("500: " + str(log.count(" 500 ")))
document = readFile(sys.argv[1])
printReturnCodes(document)
