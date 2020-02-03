'''import seleniumbot
seleniumbot.whatsappWebConnection('C:\\Users\\Wesle\\Desktop\\chromedriver')
a=seleniumbot.readAllMessages('Amor Tim', textDirection)
print(a)'''

'''from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))
print(driver.find_element_by_class_name("P6z4j")).text

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
input('Enter anything after scanning QR code')
Nomes=['Mãe']
for nome in Nomes:
	pessoas=driver.find_element_by_xpath('//span[@title= "{}"]'.format(nome))
	pessoas.click()
	for i in range(1,3):
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	msg_got=driver.find_element_by_css_selector('spain.selectable-text.invisible-space.copyable-text').text
	msg=[message.text for message in msg_got]

	print(msg)