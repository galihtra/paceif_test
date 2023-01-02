from selenium import webdriver
import time
import tkinter as tk

window = tk.Tk()
window.geometry('500x110')
window.configure(background='#856ff8')

def fill_form():
    
    recycle = 10
    for x in range(recycle):
        print(x)
        driver = webdriver.Chrome(executable_path='Home:\Documents\chromedriver.exe')
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSePgQF5hBgXRgv3tYfilCuu5TfUUjmuSAw3qflQ3GAX7LGJcw/viewform')
        time.sleep(1) 

        grade = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        grade.click()
        time.sleep(0.5)

        select = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/span')
        select.click()
        time.sleep(0.5)

        name = "Galih Tri Risky Andiko"
        inputName = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        for i in name:
            inputName.send_keys(i)
            time.sleep(0.05)

        nim = "4342201010"
        inputNim = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        for i in nim:
            inputNim.send_keys(i)
            time.sleep(0.05)

        score = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
        score.click() 
        time.sleep(0.5)   

        submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click() 
        time.sleep(0.5) 

        backForm = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        backForm.click() 
        time.sleep(1) 

window.title('Mengisi google form secara otomatis')

label = tk.Label(window, text='Mari mulai pengujian')

button_start = tk.Button(window,text='START', command=fill_form)
button_start.pack(padx=100,pady=1,fill='x',expand=True)

button_quit = tk.Button(window,text='QUIT', command=window.destroy)
button_quit.pack(padx=100,pady=1,fill='x',expand=True)

window.mainloop()
time.sleep(1)