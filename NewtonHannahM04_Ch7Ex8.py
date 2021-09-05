Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
	girlList = []
	boyList = []
	file_vari = open("GirlNames.txt","r")
	for i in file_vari:
		 j = i.rstrip("\n")
		 girlList.append(j)

		 
>>> def main():
	girlList = []
	boyList = []
	import os
	file_vari = open("GirlNames.txt","r")
	for i in file_vari:
		 j = i.rstrip("\n")
		 girlList.append(j)
	file_vari.close()
	import os
	file_vari1 = open("BoyNames.txt","r")
	for i in file_vari1:
		 j = i.rstrip("\n")
		 boyList.append(j)
	file_vari1.close()
	print("Girl List = ",end ="")
	print(girlList)
	print()
	print()
	print("Boy List = ",end ="")
	print(boyList)
	girlName = input("Enter the girl name : ")
	boyName = input("Enter the boy name : ")
	if girlName != "":
		if girlName in girlList:
			print("the girl that you entered is valid in the list")
		else:
			print("the girl that you entered isnot valid in the list")
	else:
		print("you didnot enter the girl name")
	if boyName != "":
		if boyName in boyList:
			print("the boy that you entered is valid in the list")
		else:
			print("the boy that you entered isnot valid in the list")
	else:
		print("you didnot enter the boy name")

		
>>> main()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    main()
  File "<pyshell#48>", line 5, in main
    file_vari = open("GirlNames.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'GirlNames.txt'
>>> 