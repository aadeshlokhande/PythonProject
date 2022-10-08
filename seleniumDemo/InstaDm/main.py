from selenium import webdriver
import time
import random
from ids import username,password
from Msg import msg
from selenium.webdriver.common.keys import Keys


print("# usernames ")


file = open("users.txt","r")
username_list = file.read().split("\n")
file.close()




driver = webdriver.Chrome('/home/diamond/Documents/MyProjects/PythonData/seleniumDemo/CD/chromedriver')
driver.get("https://www.instagram.com")
time.sleep(3)
for i in range(len(username)):
    driver.find_element_by_css_selector("input[name='username']").send_keys(username[i]) 
    print("#for sending username")
    
    driver.find_element_by_css_selector("input[name='password']").send_keys(password[i])  
    print("#for sending password")
    
    driver.find_element_by_xpath("//button[@type='submit']").click() 
    print("#login button")
    
    time.sleep(8)
    driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click() 
    print("#message icon press")
    
    time.sleep(random.randrange(2,3))
    try:
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click() 
        print("#not now button")
        
        time.sleep(random.randrange(1,2))
    except:
        pass 
    
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click() 
    print("#send messages button")
    
    for i in range(2):
        user = username_list[0]
        time.sleep(random.randrange(1,2))
        driver.find_element_by_name('queryBox').send_keys(user) 
        print("#username to msg")
        
        time.sleep(random.randrange(2,3))
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click() 
        print("#selecting user")
        
        time.sleep(random.randrange(2,3))
        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click() 
        print("#next button")
        
        time.sleep(random.randrange(3,4))
        text_area = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') 
        print("#textbox area slection")
        
        text_area.send_keys(msg) 
        print("#typing msg")
        
        time.sleep(1)
        text_area.send_keys(Keys.ENTER) 
        username_list.pop(0)
        time.sleep(random.randrange(3,4))
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click() 
        print("#search for next user to msg")
        
        time.sleep(random.randrange(1,2))
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[1]/div/button').click() 
    print("#cancel button")
    
    time.sleep(random.randrange(1,2))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[6]').click() 
    print("#user icon click")
    
    time.sleep(random.randrange(1,2))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div').click() 
    print("#log out button")
    
    time.sleep(random.randrange(5,6))

file = open("users.txt","w")
for i in range(len(username_list)):
    file.write(f"{username_list[i]}\n")    
file.close()

            

