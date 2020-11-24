import schedule
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

print("running")

geo = "https://meet.google.com/lookup/****"
chemija = "https://meet.google.com/lookup/****"
lt = "https://meet.google.com/lookup/****"
bio = "https://meet.google.com/lookup/****"
mat = "https://meet.google.com/lookup/****"
rus = "https://meet.google.com/lookup/****"
ist = "https://meet.google.com/lookup/****"
info = "https://meet.google.com/lookup/****"
eng = "https://meet.google.com/lookup/****"
fiz = "https://meet.google.com/lookup/****"


def go(link):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    path = r"C:\Users\otoma\Desktop\python project\chromedriver\chromedriver.exe"
    browser = webdriver.Chrome(options=opt, executable_path=path)
    browser.get("https://gmail.com")
    browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys("****@gmail.com")
    browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("****")
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(3)
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()


schedule.every().monday.at("08:29").do(go, ist)
schedule.every().monday.at("09:49").do(go, eng)
schedule.every().monday.at("10:09").do(go, mat)
schedule.every().monday.at("12:19").do(go, geo)
schedule.every().monday.at("13:14").do(go, chemija)

schedule.every().tuesday.at("08:54").do(go, bio)
schedule.every().tuesday.at("10:09").do(go, info)
schedule.every().tuesday.at("13:14").do(go, lt)

schedule.every().wednesday.at("07:59").do(go, geo)
schedule.every().wednesday.at("08:54").do(go, fiz)
schedule.every().wednesday.at("12:19").do(go, mat)
schedule.every().wednesday.at("13:14").do(go, eng)

schedule.every().thursday.at("08:54").do(go, ist)
schedule.every().thursday.at("10:09").do(go, rus)
schedule.every().thursday.at("13:14").do(go, lt)

schedule.every().friday.at("07:59").do(go, lt)
schedule.every().friday.at("08:54").do(go, mat)
schedule.every().friday.at("10:09").do(go, fiz)
schedule.every().friday.at("12:19").do(go, eng)


while 1:
    schedule.run_pending()
    time.sleep(1)
