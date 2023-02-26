import string
import random
import time

flag = False
## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Şifre Uzunluğunu Giriniz : "))

	## number of character types
	alphabets_count = int(input("Şifre Kaç Harf İçersin : "))
	digits_count = int(input("Şifre Kaç Rakam İçersin : "))
	special_characters_count = int(input("Şifre Kaç Özel Karakter İçersin : "))
	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("Karakterlerin toplam sayısı şifre uzunluğundan büyük !")
		return


	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))
	new_password_recommend = (input("Yeni Şifre İstiyor musun(Evet/Hayır) :"))
	if (new_password_recommend == "Evet"):
		flag=True
	else:
		flag=False
	if (flag == True):
		generate_random_password()
	else:
		print("Program Kapatılıyor...")
		time.sleep(10)
		quit()



## invoking the function
generate_random_password()