import sys
def encrypt(strng, key):
	encrypted = ''
	for x in strng:
		indx = (ord(x) + key) % 256
		if indx > 126:
			indx -= 95
		encrypted += chr(indx)
	return encrypted


def decrypt(strng, key):
	decrypted = ''
	for x in strng:
		indx = (ord(x) - key) % 256
		if indx < 32:
			indx += 95
		decrypted += chr(indx)
	return decrypted


def brute_force(strng):
	key = 1
	decrypted = ''
	while key <= 94:
		for x in strng:
			indx = (ord(x) - key) % 256
			if indx < 32:
				indx += 95
			decrypted += chr(indx)
		print("key: {}\t| Message: {}".format(key, decrypted))
		decrypted = ''
	return None


def main():
	while True:
		print('-' * 10 + "\n ** Menu **\n" + '-' * 10)
		print("1:Encrypt")
		print("2:Decrypt")
		print("3:BruteForce")
		print("4:Quit")

		choice = str(input("What do u like to do ?"))
		if choice not in ['1', '2', '3', '4']:
			print("Invalid choice")
		elif choice == '1':
			strng = raw_input("Please enter the strng to be decrypted")
			key = int(raw_input("Please enter off set between 1-94"))
			if key in range(1,95):
				print(encrypt(strng.lower(), key))
		elif choice == '2':
			strng = raw_input("Please enter string to be decrypted")
			key = int(raw_input("Please neter offset betweeen 1-94"))
			if key > 0 and key <= 94:
				print(decrypt(strng, key))
		elif choice == '3':
			strng = raw_input("Please enter string to be decrypted")
			brute_force(strng)
			main()
		elif choice == '4':
			print("Goodbye..")
			break
main()															

