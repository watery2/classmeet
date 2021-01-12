import schedule
import sqlite3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

connection = sqlite3.connect("class_meet.db")

cursor = connection.cursor()

end = 0

print("if this is your first time please login with your gmail and password")
print("commands add then m or t or w or th or f. del then m or t or w or th or f \n before starting you can leave with "
      "end ")
print("start to start")


def create_table():

    try:
        cursor.execute("CREATE TABLE logins (gmail TEXT, password TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")

    try:
        cursor.execute("CREATE TABLE mon (time_e TEXT, link TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")

    try:
        cursor.execute("CREATE TABLE tue (time_e TEXT, link TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")

    try:
        cursor.execute("CREATE TABLE wed (time_e TEXT, link TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")

    try:
        cursor.execute("CREATE TABLE thu (time_e TEXT, link TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")

    try:
        cursor.execute("CREATE TABLE fri (time_e TEXT, link TEXT)")
    except sqlite3.OperationalError:
        print("checked if a table was made")


create_table()


def login():
    gmail = input("enter your gmail: ")
    password = input("enter your gmail password: ")
    cursor.execute("INSERT INTO logins VALUES (?, ?)", (gmail, password),)
    connection.commit()


def add():

    day = input("enter a day like m or t or w or th or f: ")

    if day == "m":
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("INSERT INTO mon VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "t":
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("INSERT INTO tue VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "w":
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("INSERT INTO wed VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "th":
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("INSERT INTO thu VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "f":
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("INSERT INTO fri VALUES (?, ?)", (time_e, link), )
        connection.commit()


def del_l():

    day = input("enter a day like m or t or w or th or f: ")

    if day == "login":
        rows_l = cursor.execute("SELECT gmail FROM logins").fetchall()
        rows_output_l = [i_l[0] for i_l in rows_l]
        print(rows_output_l)
        gmail = input("enter your gmail: ")
        password = input("enter your password: ")
        cursor.execute("DELETE FROM logins Where gmail = ?", (gmail,))
        cursor.execute("DELETE FROM logins Where password = ?", (password,))
        connection.commit()

    if day == "m":
        rows_m_t = cursor.execute("SELECT time_e FROM mon ").fetchall()
        rows_m_l = cursor.execute("SELECT link FROM mon ").fetchall()
        rows_output_m_t = [i_m_t[0] for i_m_t in rows_m_t]
        rows_output_m_l = [i_m_l[0] for i_m_l in rows_m_l]
        print(rows_output_m_t)
        print(rows_output_m_l)
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("DELETE FROM mon Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM mon Where link = ?", (link,))
        connection.commit()

    if day == "t":
        rows_t_t = cursor.execute("SELECT time_e FROM tue ").fetchall()
        rows_t_l = cursor.execute("SELECT link FROM tue ").fetchall()
        rows_output_t_t = [i_t_t[0] for i_t_t in rows_t_t]
        rows_output_t_l = [i_t_l[0] for i_t_l in rows_t_l]
        print(rows_output_t_t)
        print(rows_output_t_l)
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("DELETE FROM tue Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM tue Where link = ?", (link,))
        connection.commit()

    if day == "w":
        rows_w_t = cursor.execute("SELECT time_e FROM wed ").fetchall()
        rows_w_l = cursor.execute("SELECT link FROM wed ").fetchall()
        rows_output_w_t = [i_w_t[0] for i_w_t in rows_w_t]
        rows_output_w_l = [i_w_l[0] for i_w_l in rows_w_l]
        print(rows_output_w_t)
        print(rows_output_w_l)
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("DELETE FROM wed Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM wed Where link = ?", (link,))
        connection.commit()

    if day == "th":
        rows_th_t = cursor.execute("SELECT time_e FROM thu ").fetchall()
        rows_th_l = cursor.execute("SELECT link FROM thu ").fetchall()
        rows_output_th_t = [i_th_t[0] for i_th_t in rows_th_t]
        rows_output_th_l = [i_th_l[0] for i_th_l in rows_th_l]
        print(rows_output_th_t)
        print(rows_output_th_l)
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("DELETE FROM thu Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM thu Where link = ?", (link,))
        connection.commit()

    if day == "f":
        rows_f_t = cursor.execute("SELECT time_e FROM fri ").fetchall()
        rows_f_l = cursor.execute("SELECT link FROM fri ").fetchall()
        rows_output_f_t = [i_f_t[0] for i_f_t in rows_f_t]
        rows_output_f_l = [i_f_l[0] for i_f_l in rows_f_l]
        print(rows_output_f_t)
        print(rows_output_f_l)
        time_e = input("enter the time: ")
        link = input("enter the link: ")
        cursor.execute("DELETE FROM fri Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM fri Where link = ?", (link,))
        connection.commit()


def go(link, ju, gm, ps):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", {\
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })
    path = r"C:\Users\otoma\Desktop\python project\chromedriver\chromedriver.exe"
    browser = webdriver.Chrome(options=opt, executable_path=path)
    browser.get("https://gmail.com")
    time.sleep(22)
    browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(gm)
    browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(ps)
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(3)
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(link[ju])
    time.sleep(5)
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/'
        'span/span').click()


def start():

    m_t = 0

    t_t = 0

    w_t = 0

    th_t = 0

    f_t = 0

    rows_m_t = cursor.execute("SELECT time_e FROM mon ").fetchall()
    rows_m_l = cursor.execute("SELECT link FROM mon ").fetchall()

    rows_output_m_t = [i_m_t[0] for i_m_t in rows_m_t]
    rows_output_m_l = [i_m_l[0] for i_m_l in rows_m_l]

    rows_t_t = cursor.execute("SELECT time_e FROM tue ").fetchall()
    rows_t_l = cursor.execute("SELECT link FROM tue ").fetchall()

    rows_output_t_t = [i_t_t[0] for i_t_t in rows_t_t]
    rows_output_t_l = [i_t_l[0] for i_t_l in rows_t_l]

    rows_w_t = cursor.execute("SELECT time_e FROM wed ").fetchall()
    rows_w_l = cursor.execute("SELECT link FROM wed ").fetchall()

    rows_output_w_t = [i_w_t[0] for i_w_t in rows_w_t]
    rows_output_w_l = [i_w_l[0] for i_w_l in rows_w_l]

    rows_th_t = cursor.execute("SELECT time_e FROM thu ").fetchall()
    rows_th_l = cursor.execute("SELECT link FROM thu ").fetchall()

    rows_output_th_t = [i_th_t[0] for i_th_t in rows_th_t]
    rows_output_th_l = [i_th_l[0] for i_th_l in rows_th_l]

    rows_f_t = cursor.execute("SELECT time_e FROM fri ").fetchall()
    rows_f_l = cursor.execute("SELECT link FROM fri ").fetchall()

    rows_output_f_t = [i_f_t[0] for i_f_t in rows_f_t]
    rows_output_f_l = [i_f_l[0] for i_f_l in rows_f_l]

    rows_gmail = cursor.execute("SELECT gmail FROM logins ").fetchone()
    rows_pas = cursor.execute("SELECT password FROM logins ").fetchone()

    try:
        for m_t_t in rows_output_m_t:
            schedule.every().monday.at(m_t_t).do(go, rows_output_m_l, m_t, rows_gmail, rows_pas)
            m_t += 1
    except schedule.ScheduleValueError:
        print("sorry something maybe went wrong maybe you wrote the time wrong")
    try:
        for t_t_t in rows_output_t_t:
            schedule.every().tuesday.at(t_t_t).do(go, rows_output_t_l, t_t, rows_gmail, rows_pas)
            t_t += 1
    except schedule.ScheduleValueError:
        print("sorry something maybe went wrong maybe you wrote the time wrong")
    try:
        for w_t_t in rows_output_w_t:
            schedule.every().wednesday.at(w_t_t).do(go, rows_output_w_l, w_t, rows_gmail, rows_pas)
            w_t += 1
    except schedule.ScheduleValueError:
        print("sorry something maybe went wrong maybe you wrote the time wrong")
    try:
        for th_t_t in rows_output_th_t:
            schedule.every().thursday.at(th_t_t).do(go, rows_output_th_l, th_t, rows_gmail, rows_pas)
            th_t += 1
    except schedule.ScheduleValueError:
        print("sorry something maybe went wrong maybe you wrote the time wrong")
    try:
        for f_t_t in rows_output_f_t:
            schedule.every().friday.at(f_t_t).do(go, rows_output_f_l, f_t, rows_gmail, rows_pas)
            f_t += 1
    except schedule.ScheduleValueError:
        print("sorry something maybe went wrong maybe you wrote the time wrong")

    while 1:
        schedule.run_pending()
        time.sleep(1)


def check():

    enter = input("enter a command: ")

    if enter == "add":
        add()

    if enter == "del":
        del_l()

    global end

    if enter == "end":
        end += 1

    if enter == "login":
        login()

    if enter == "start":
        start()


while end == 0:
    check()

connection.close()
