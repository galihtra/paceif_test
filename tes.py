from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='Home:\Documents\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://localhost/paceif/auth')
time.sleep(1) 

admin = "admin"
adminPass = "admin"

inputAdmin = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[1]/input')
for i in admin:
    inputAdmin.send_keys(i)
    time.sleep(0.05)

inputPassAdmin = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[2]/input')
for i in adminPass:
    inputPassAdmin.send_keys(i)
    time.sleep(0.05)

submit = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/button')
submit.click() 
time.sleep(0.5)  

driver.get('http://localhost/paceif/master/persyaratan')
time.sleep(1) 

# added
driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[1]/a').click()
time.sleep(1)

select = driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[2]/div/div[1]/div/span/span[1]/span')
select.send_keys('Surat Keterangan Beasiswa')
select.click()
time.sleep(0.5)

requirement = "Dokumen Pendukung"
inputRequire = driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[2]/div/div[2]/input')
for i in requirement:
    inputRequire.send_keys(i)
    time.sleep(0.05)    

driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[3]/button[2]').click()
time.sleep(1)