import zipfile 
import sys

if len(sys.argv) == 3:
	try:
		file = sys.argv[1]
		z = zipfile.ZipFile(file)
		passwd = sys.argv[2]
		print("[+] Extracting process started...")
		z.extractall(pwd=passwd)
		print("Success")
	except Exception as e:
		print("Unable to access file"+"\n")
		print("try : python zipFileCracker3 'file path' 'password'")
		print(e)
