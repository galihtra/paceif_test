from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome(executable_path='Home:\Documents\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

# Register
driver.get('http://localhost/paceif/auth/register')
time.sleep(1) 

nim = "4342201028"
inputnim = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[1]/input')
for i in nim:
    inputnim.send_keys(i)
    time.sleep(0.05)

password = "123456"
inputPassword = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[2]/input')
for i in password:
    inputPassword.send_keys(i)
    time.sleep(0.05)

submit = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/button')
submit.click() 
time.sleep(0.5)    

# Invalid Register
driver.get('http://localhost/paceif/auth/register')
time.sleep(1) 

inputnim = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[1]/input')
for i in nim:
    inputnim.send_keys(i)
    time.sleep(0.05)

inputPassword = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[2]/input')
for i in password:
    inputPassword.send_keys(i)
    time.sleep(0.05)

submit = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/button')
submit.click() 
time.sleep(0.5)     

# Invalid Login
driver.get('http://localhost/paceif/auth')
time.sleep(1) 

inputnim = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[1]/input')
for i in nim:
    inputnim.send_keys(i)
    time.sleep(0.05)

passwordInvalid = "123455"
inputPassword = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[2]/input')
for i in passwordInvalid:
    inputPassword.send_keys(i)
    time.sleep(0.05)

submit = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/button')
submit.click() 
time.sleep(0.5)     

# Login
driver.get('http://localhost/paceif/auth')
time.sleep(1) 

inputnim = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[1]/input')
for i in nim:
    inputnim.send_keys(i)
    time.sleep(0.05)

inputPassword = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/div[2]/input')
for i in password:
    inputPassword.send_keys(i)
    time.sleep(0.05)

submit = driver.find_element("xpath",'/html/body/div/div/div/div/div/div[3]/div/div/form/button')
submit.click() 
time.sleep(0.5)     

# Invalid Profile Mahasiswa
driver.get('http://localhost/paceif/dashboard/profil_saya')
time.sleep(1) 

submit = driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div/form/div/div[10]/button')
submit.click() 
time.sleep(0.5)   

# Profile Mahasiswa
driver.get('http://localhost/paceif/dashboard/profil_saya')
time.sleep(1) 

fullName = "Galih tra"
inputFullname = driver.find_element("xpath",'//*[@id="nama_lengkap"]')
for i in fullName:
    inputFullname.send_keys(i)
    time.sleep(0.05)

prodi = "TRPL"
inputProdi = driver.find_element("xpath",'//*[@id="program_studi"]')
for i in prodi:
    inputProdi.send_keys(i)
    time.sleep(0.05)

birth = "04-06-2004"
inputBirth = driver.find_element("xpath",'//*[@id="tanggal_lahir"]')
for i in birth:
    inputBirth.send_keys(i)
    time.sleep(0.05)   

gender = driver.find_element("xpath",'//*[@id="jenis_kelamin"]/option[1]')
gender.click() 
time.sleep(0.5)

religi = driver.find_element("xpath",'//*[@id="agama"]/option[1]')
religi.click() 
time.sleep(0.5)   

address = "Istana Negara"
inputAddress = driver.find_element("xpath",'//*[@id="alamat"]')
for i in address:
    inputAddress.send_keys(i)
    time.sleep(0.05)   

submit = driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div/form/div/div[10]/button')
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
time.sleep(0.5)     


# Buat Ajuan
driver.get('http://localhost/paceif/pengajuan/upload_file/139')
time.sleep(1) 

send = driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[2]/div/form/button')
send.click()
time.sleep(1)

# Hapus Pengajuan 
driver.get('http://localhost/paceif/pengajuan_saya')
time.sleep(1) 

delete = driver.find_element("xpath",'//*[@id="dataTable"]/tbody/tr[1]/td[6]/a[2]/i')
delete.click()
time.sleep(1)

driver.find_element("xpath",'//*[@id="page-top"]/div[3]/div/div[3]/button[3]').click()
time.sleep(1)

# Melihat status Pengajuan
driver.get('http://localhost/paceif/pengajuan_saya')
time.sleep(1) 

# Logout to admin
driver.get('http://localhost/paceif/pengajuan_saya')
time.sleep(1) 

user = driver.find_element("xpath",'//*[@id="userDropdown"]/span')
user.click()
time.sleep(1)

logout = driver.find_element("xpath",'//*[@id="content"]/nav/ul/li/div/a')
logout.click()
time.sleep(1)

driver.find_element("xpath",'//*[@id="logoutModal"]/div/div/div[3]/a').click()
time.sleep(1)

# Admin Login
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

# Invalid menambahkan nama dan persyaratan
driver.get('http://localhost/paceif/master/surat')
time.sleep(1) 

driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[1]/a').click()
time.sleep(1)

driver.find_element("xpath",'//*[@id="surat"]/div/div/form/div[3]/button[2]').click()
time.sleep(1)

driver.get('http://localhost/paceif/master/persyaratan')
time.sleep(1) 

driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[1]/a').click()
time.sleep(1)

driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[3]/button[2]').click()
time.sleep(1)

# Menambahkan nama dan persyaratan
driver.get('http://localhost/paceif/master/surat')
time.sleep(1) 

driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[1]/a').click()
time.sleep(1)

nameLetter = "Pengajuan Kartu Mahasiwa"
inputLetter = driver.find_element("xpath",'//*[@id="nama_surat"]')
for i in nameLetter:
    inputLetter.send_keys(i)
    time.sleep(0.05)    

desc = "Pengajuan Kartu Mahasiwa"
inputDesc = driver.find_element("xpath",'//*[@id="keterangan"]')
for i in desc:
    inputDesc.send_keys(i)
    time.sleep(0.05)    

driver.find_element("xpath",'//*[@id="surat"]/div/div/form/div[3]/button[2]').click()
time.sleep(1)

driver.get('http://localhost/paceif/master/persyaratan')
time.sleep(1) 

driver.find_element("xpath",'//*[@id="content"]/div/div[4]/div[1]/a').click()
time.sleep(1)

driver.find_element("xpath",'//*[@id="select2-surat_id-container"]').click()
time.sleep(0.05)    

requirement = "Melampirkan KTM"
inputRequire = driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[2]/div/div[2]/input')
for i in requirement:
    inputRequire.send_keys(i)
    time.sleep(0.05)    

driver.find_element("xpath",'//*[@id="persyaratan"]/div/div/form/div[3]/button[2]').click()
time.sleep(1)
