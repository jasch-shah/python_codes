import re

sentence = "A, very very; irregular sentence"
desired_output = "A very very irregular sentence"

print("Sentence:\n", sentence)
print('Desired Output : \n', desired_output)

l = re.split('[^a-zA-Z]', sentence)

s = ''
for i in range(len(l)):
	if l[i] != '':
		s += l[i] + '  '

print("Output:\n", s)		