from collections import Counter
import inspect

def is_anagram(word, _list):

	word = word.lower()
	anagrams = []
	for words in _list:
		if word != words.lower():
			if Counter(word) == Counter(words.lower()):
				anagrams.append(words)
	return anagrams	


def get_code():
	word = str(input())
	_list = ['romor', 'jash', 'falula', 'ababa', 'circus']
	return inspect.getsource(is_anagram(word, _list))			