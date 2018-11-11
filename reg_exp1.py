import re
emails = ["jasch.shah20@gmail.com", "htlshah4@rediffmail.com", "ishan34@yahoo.com"]
desired_outputs=[]

for i in range(len(emails)):
	new=re.split('\W', emails[i])
	desired_outputs.append(new)

print(desired_outputs)	