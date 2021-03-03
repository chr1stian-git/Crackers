import crypt 

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open("wordlist.txt",'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		print "inside the for loop"
		if (cryptWord == cryptPass):
			print "pass found "+word
			return 
	print "pass not found \n"
	return 

def main():
	passFile = open("passwords.txt", 'r')
	for line in passFile.readlines():
		cryptPass = line.split(':')[1].strip(' ')
		print "Cracking started..."
		testPass(cryptPass)
main()

