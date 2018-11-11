"""
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())

print("Number of words in the file : ",word_count("file1.txt"))


"""
from __future__ import print_function
import sys

def LastNLines(f,n):
	with open(f) as file:
		print('Last ',n,'Lines from File:', f)
		for line in (file.readlines()[-n:]):
			print(line, end = '')




n = int(input('No of last lines to be read'))
try:
	LastNLines("file1.txt",n)
except:
	print('File Error')


