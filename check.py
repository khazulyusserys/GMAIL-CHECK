import mechanize, random, os
from bs4 import BeautifulSoup as nub
from faker import Faker

url="https://accounts.google.com/servicelogin"

#set browser
br = mechanize.Browser()
br.set_handle_robots(False)

def get_user_mail(total):
	try:
		os.system('rm -rf emails.txt')
	except IOError:
		pass
	for mail in range(total):
		mail = Faker()
		name = mail.first_name().lower()
		email = name + str(random.randint(0,1000)) + '@gmail.com'
		f = open("emails.txt","a")
		if len(email)==19:
			f.write(email + '\n')
		f.close()

def check_user():
	try:
		os.system('rm -rf aktif.txt')
	except IOError:
		pass

	f = open("emails.txt","r").readlines()
	print("total email: {0}".format(len(f)))
	for emails in f:
		email = emails.replace("\n",'')
		br.open(url)
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form["Email"]=email
		soup = nub(br.submit().read(), features="html5lib")
		try:
			find_error=soup.find("h1")
			file=open("aktif.txt","a")
			if find_error==find_error:
				file.write(email + '\n')
		except:
			pass
	total = open("aktif.txt","r").readlines()
	print("total email aktif: {0}".format(len(total)))

if __name__ == "__main__":
	get_user_mail(100)
	check_user()
