import hashlib
pass_hash = input("Enter de hash: ")
flag = 0
wordlist = input("File name: ")

try:
	pass_file = open(wordlist, "r")
except:
	print("No file found")
	quit()

for word in pass_file:
	
	enc_word = word.encode("utf-8")
	digest = hashlib.md5(enc_word.strip()).hexdigest()
	
	if digest == pass_hash:
		print("password found: ", word)
		flag = 1
		break
if flag == 0:
	print("password not found")

