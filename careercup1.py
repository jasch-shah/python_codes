sentence = raw_input("Enter String")
sentence = sentence.split()
new_sentence = [word[::-1] for word in sentence]
print ' '.join(str(x) for x in new_sentence)
