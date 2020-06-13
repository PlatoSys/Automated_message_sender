from selenium import webdriver as wd
import time


username = input("Input your username to log in:  ")
passkey = input("Input Your password:  ")
phone_number = input("input phone number:  ")
send_message = input("input text:  ")
count = int(input("input number of sent messages:  "))

driver = wd.Chrome(executable_path='C:/Users/ThinkPad/PycharmProjects/AutomatedMessageSender/Driver/chromedriver')
driver.maximize_window()

driver.get('http://www.magtifun.ge/')

user = driver.find_element_by_xpath('//*[@id="user"]')
user.send_keys(username)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(passkey)

go = driver.find_element_by_xpath('/html/body/div[1]/center/div[1]/div[2]/div[1]/form/table/tbody/tr/td[2]/input')
go.submit()

for i in range(count):
    number = driver.find_element_by_xpath('//*[@id="recipient"]')
    number.send_keys(phone_number)

    text = driver.find_element_by_xpath('//*[@id="message_body"]')
    text.send_keys(send_message)

    send = driver.find_element_by_xpath('//*[@id="sms_form"]/p[6]/input')
    send.submit()
    time.sleep(6)

    back_to_sms = driver.find_element_by_link_text('SMS')
    driver.execute_script("arguments[0].click()", back_to_sms)
driver.quit()
