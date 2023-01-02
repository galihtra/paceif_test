from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='Home:\Documents\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://localhost/paceif/auth')
time.sleep(1) 

admin = "4342201028"
adminPass = "123456"

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

# Invalid Buat Ajuan
driver.get('http://localhost/paceif/dashboard')
time.sleep(1) 

createSubmission = driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div/div/form/div/button[2]')
createSubmission.click() 
time.sleep(0.5)     

driver.get('http://localhost/paceif/pengajuan/upload_file/139')
time.sleep(1) 

upload = driver.find_element("xpath",'//*[@id="2"]')
upload.click() 