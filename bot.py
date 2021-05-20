from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import itertools
import random

x = 0

while(x == 0):
  
   # gera emails aleatorios 
   letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n", "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
   all_combos = list(itertools.combinations(letters,7)) 
   all_combos = [''.join(combo) for combo in all_combos] 
   email = random.sample(all_combos,1)[0]+'@gmail.com' 
   
   password = "senhasdash"

   # emulador de celular pq a pagina so funciona em modo mobile 
   mobile_emulation = {

      "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

      "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

   chrome_options = Options()

   #chrome_options.add_argument('headless')

   chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

   driver = webdriver.Chrome(chrome_options = chrome_options)
   
   seu_link = 'https://a.aliexpress.com/_m0aGUvF'

   driver.get(seu_link)

   time.sleep(2)
   driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[4]/div/a/span').click()

   time.sleep(2)
   driver.find_element_by_xpath('//*[@id="msite-login"]/div/div[2]/div[1]/div/ul/li[1]/div').click()

   time.sleep(2)
   driver.find_element_by_xpath('//*[@id="msite-login"]/div/div[2]/div[1]/div/ul/li[1]/div').click()
                                                     
   time.sleep(3)
   driver.find_element_by_xpath('//*[@id="msite-login"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/input').send_keys(email)
   driver.find_element_by_xpath('//*[@id="msite-login"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/input').send_keys(password)
   driver.find_element_by_xpath('//*[@id="msite-login"]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[5]/a').click()
   time.sleep(3)
   driver.get(seu_link)

   time.sleep(2)
   driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[4]/div/a/span').click()
   time.sleep(2)
   driver.find_element_by_link_text("Continuar").click()
   time.sleep(2)
  
   driver.close()

