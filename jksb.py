import random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

settings_file = open("settings.txt", "r+")

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://yqtb.hust.edu.cn/infoplus/form/BKS/start')
username = browser.find_element_by_name("un")
username.send_keys(settings_file.readline())
password = browser.find_element_by_name("pd")
#password.send_keys(settings_file.readline())
password.send_keys("Hxp66513138/")
settings_file.close()
#password.send_keys(Keys.TAB)

while True:
	try:
		option_button = browser.find_element_by_name("fieldHidden1")
		option_button.click()
		break
	except:
		pass

while True:
	try:
		next_step_button = browser.find_element_by_class_name("command_button_content")
		next_step_button.click()
		break
	except:
		pass
		
while True:
	try:
		next_step_button = browser.find_element_by_class_name("command_button_content")
		next_step_button.click()
		break
	except:
		pass

while True:
	try:
		temp_student = browser.find_element_by_name("fieldXSZLB")
		temp_student.send_keys(str(36.5+random.randint(-3,3)/10))
		temp_family = browser.find_element_by_name("fieldJSTW_0")
		temp_family.send_keys(str(36.5+random.randint(-3,3)/10))
		break
	except:
		pass
#time.sleep(3)
submit_button = browser.find_element_by_xpath("//*[contains(text(), '提交')]")
submit_button.click()
while True:
	try:
		ok_button = browser.find_element_by_css_selector(".dialog_button.default.fr")
		ok_button.click()
		break
	except:
		pass
time.sleep(1)
while True:
	try:
		ok_button = browser.find_element_by_css_selector(".dialog_button.default.fr")
		ok_button.click()
		break
	except:
		pass
print("All Done. Have a nice day!")
exit()
