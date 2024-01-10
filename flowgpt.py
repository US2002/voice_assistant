from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
import warnings

# from clap import MainClapExe
# MainClapExe()

warnings.simplefilter('ignore')

ScriptDir = pathlib.Path().absolute()

# sleep(500)
ChatNumber = 3


def Checker():
    # print("Checking Chat Number")
    global ChatNumber
    for i in range(1, 1000):
        if i % 2 != 0:
            try:
                ChatNumber = str(i)
                Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div"
                driver.find_element(by=By.XPATH, value=Xpath)

            except:
                # print(f"The next chatnumber is : {i}")
                ChatNumber = str(i)
                break


def Websiteopener():
    global driver
    url = "https://flowgpt.com/chat"
    chrome_option = Options()
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
    chrome_option.add_argument(f"user-agent={user_agent}")
    chrome_option.add_argument('--profile-directory=Default')
    chrome_option.add_argument("--headless=new")
    chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_option)
    driver.maximize_window()
    driver.get(url=url)

    while True:
        try:
            xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/textarea'
            driver.find_element(by=By.XPATH, value=xPATH)
            Checker()
            break
        except:
            sleep(5)
            pass


def SendMessage(Query):
    # print("Sending message")
    xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/textarea'
    driver.find_element(by=By.XPATH, value=xPATH).send_keys(Query)
    sleep(1)
    Xpath2 = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(by=By.XPATH, value=Xpath2).click()


def Resultscrapper():
    # print("Getting Result")
    global ChatNumber
    ChatNumber = str(ChatNumber)
    sleep(4)
    Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div"
    Text = driver.find_element(by=By.XPATH, value=Xpath).text
    ChatNumberNew = int(ChatNumber) + 2
    ChatNumber = ChatNumberNew
    return Text


def waitfortheanswer():
    # print("waiting for answer")
    Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button'
    while True:
        try:
            driver.find_element(by=By.XPATH, value=Xpath)
        except:
            break
