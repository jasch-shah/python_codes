'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and 
will check them according to the above criteria. Passwords that match 
the criteria are to be printed, each separated by a comma.


'''

import re
value = []
items = [x for x in raw_input().split(',')]
for p in items:
	if len(p) < 6 or len(p) > 20:
		continue
	else:
		pass
	if not re.search("[a-z]",p):
		continue
	elif not re.search("[0-9]",p):
		continue
	elif not re.search("[A-Z]",p):
		continue
	elif not re.search("[$#@]",p):
		continue
	elif re.search("\s",p):
		continue
	else:
		pass
	value.append(p)
print ",".join(value)									