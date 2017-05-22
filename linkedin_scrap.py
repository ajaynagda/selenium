from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

myemail = 'ABC@gmail.com'
mypassword = 'password'

chromedriver = webdriver.Chrome(executable_path = r'C:\Python27\Scripts\chromedriver.exe')

def login_linkedin(myemail, mypassword):

	try:

		url = 'https://www.linkedin.com/uas/login?goback=&trk=hb_signin'

		chromedriver.get(url)

		chromedriver.maximize_window()

		# print chromedriver.page_source

		email = chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
		email.send_keys(myemail)

		password = chromedriver.find_element_by_xpath('//*[@id="session_password-login"]')
		password.send_keys(mypassword)

		sign_in = chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')
		sign_in.click()

		time.sleep(10)

		return chromedriver
	
	except Exception as e:
	
		print e.message

def get_public_profile_information(url):

	try:
		chromedriver.get(url)

		chromedriver.execute_script("window.scrollTo(0, 900);")
		

		time.sleep(10)
		
		soup = BeautifulSoup(chromedriver.page_source,'lxml')

		chromedriver.quit()
		
		for span in soup.find_all('span', class_ = 'name actor-name'):
			print span.text

		print '\n'

	except Exception as e:
	
		print e.message

	
login_linkedin( myemail, mypassword )

# sample url for scraping
url = 'https://www.linkedin.com/search/results/index/?keywords=python&origin=GLOBAL_SEARCH_HEADER'



# get name and skill which is endosed
get_public_profile_information(url)

