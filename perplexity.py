# Import necessary packages
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re

warnings.simplefilter("ignore")
url = "https://www.perplexity.ai/"
chrome_options = Options()
# chrome_options.add_argument("--headless=new")
chrome_options.add_argument('--log-level=3')
service = Service(ChromeDriverManager().install())
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(5)

File = open("Brain\\ResultNumber.txt", "w")
File.write("3")
File.close()

while True:
    Inputtttt = input("Enter Your Query : ")
    try:
        driver.find_element(
            by=By.XPATH, value="/html/body/div/main/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/textarea").send_keys(Inputtttt)
    except:
        driver.find_element(
            by=By.XPATH, value="/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[1]/div/div/div/div/div/div/textarea").send_keys(Inputtttt)

    sleep(1)
    try:
        driver.find_element(
            by=By.XPATH, value="/html/body/div/main/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div[2]/button[2]").click()
    except:
        driver.find_element(
            by=By.XPATH, value="/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[1]/div/div/div/div/div/div/div[2]/button[2]").click()

    sleep(10)
    File = open("Brain\\ResultNumber.txt", "r")
    Data = File.read()
    Data = str(Data)
    File.close()
    try:
        XpathValue = f'/html/body/div/main/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[{Data}]/div/div[3]/div[2]/div/div/div[1]'
        Text = driver.find_element(by=By.XPATH, value=XpathValue).text
        NewText = re.sub(r'\d+\s*', '', Text)
        print(NewText)
        File = open("Brain\\ResultNumber.txt", "w")
        NewData = int(Data) + 3
        File.write(str(NewData))
        File.close()
    except Exception as e:
        print(e)

#
