# Import Modules
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
import time

# Phone Number
phne = input("Enter Phone Number\n")

# pwd generator
a_dash= random.randint(2,5)
i_dash=1
pwd1 =''
while i_dash<=a_dash:
	bbb=random.randint(1,999)
	i_dash=i_dash+1
	randomLetter = random.choice(string.ascii_letters)
	ddddd = randomLetter + str(bbb)
	appl = ddddd
	pwd1 = pwd1+appl

# user name generator
a= random.randint(6,30)
i=1
usr =''
while i<=a:
	i=i+1
	randomLetter = random.choice(string.ascii_letters)
	app = randomLetter
	usr = usr+app

driver= webdriver.Chrome()

# Script
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
fn=driver.find_element('id','firstName')
ln=driver.find_element('id','lastName')
uuu=driver.find_element('id','username')
pwd=driver.find_element('xpath','//*[@id="passwd"]/div[1]/div/div[1]/input')
cpwd=driver.find_element('xpath','//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
fn.send_keys('AUTO')
ln.send_keys('GEN')
uuu.send_keys(usr)
pwd.send_keys(pwd1)
cpwd.send_keys(pwd1)
cpwd.send_keys(Keys.TAB,Keys.TAB,Keys.RETURN)
time.sleep(3)
pid= driver.find_element('id','phoneNumberId')
pid.click()
pid.send_keys(phne,Keys.RETURN)
otp = input("Enter The OTP:")