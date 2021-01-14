from tkinter import *
import schedule
import sqlite3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import threading

window = Tk()
window.title("class_meet3.0")
window.geometry("800x600")
window.resizable(0, 0)
window.configure(background="#36393e")

j = 0

its_ok_to_press = True

connection = sqlite3.connect("class_meet.db")

cursor = connection.cursor()


def login():

    gmail = gmail_entry.get()
    password = password_entry.get()
    cursor.execute("INSERT INTO logins VALUES (?, ?)", (gmail, password), )
    connection.commit()


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

gmail_text = Label(window, text="if this is your first time please login with your gmail and password", bg="#36393e",
                   fg="white", font="none 12 bold")
gmail_text.place(anchor='center', relx=.34, rely=.05)

gmail_text_2 = Label(window, text="gmail:", bg="#36393e", fg="white", font="none 12 bold")
gmail_text_2.place(anchor='center', relx=.1, rely=.1)

gmail_entry = Entry(window, width=20, bg="#434d56")
gmail_entry.place(anchor='center', relx=.1, rely=.15)

password_text = Label(window, text="password:", bg="#36393e", fg="white", font="none 12 bold")
password_text.place(anchor='center', relx=.26, rely=.1)

password_entry = Entry(window, width=20, bg="#434d56")
password_entry.place(anchor='center', relx=.26, rely=.15)

gmail_button = Button(window, text="Login", width=6, command=login, bg="#586674")
gmail_button.place(anchor='center', relx=.18, rely=.2)

add_text = Label(window, text="enter a day like this m or t or w or th or f:", bg="#36393e", fg="white",
                 font="none 12 bold")
add_text.place(anchor='center', relx=.78, rely=.15)

day_text = Label(window, text="day:", bg="#36393e", fg="white", font="none 12 bold")
day_text.place(anchor='center', relx=.61, rely=.2)

day_entry = Entry(window, width=20, bg="#434d56")
day_entry.place(anchor='center', relx=.72, rely=.2)

time_text = Label(window, text="time:", bg="#36393e", fg="white", font="none 12 bold")
time_text.place(anchor='center', relx=.612, rely=.25)

time_entry = Entry(window, width=10, bg="#434d56")
time_entry.place(anchor='center', relx=.7, rely=.25)

link_text = Label(window, text="link:", bg="#36393e", fg="white", font="none 12 bold")
link_text.place(anchor='center', relx=.609, rely=.3)

link_entry = Entry(window, width=40, bg="#434d56")
link_entry.place(anchor='center', relx=.8, rely=.3)


def add():

    day = day_entry.get()
    time_e = time_entry.get()
    link = link_entry.get()

    if day == "m":
        cursor.execute("INSERT INTO mon VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "t":
        cursor.execute("INSERT INTO tue VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "w":
        cursor.execute("INSERT INTO wed VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "th":
        cursor.execute("INSERT INTO thu VALUES (?, ?)", (time_e, link), )
        connection.commit()
    if day == "f":
        cursor.execute("INSERT INTO fri VALUES (?, ?)", (time_e, link), )
        connection.commit()


def del_l():

    day = del_l_day_entry.get()
    time_e = del_l_time_entry.get()
    link = del_l_link_entry.get()
    if day == "m":
        cursor.execute("DELETE FROM mon Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM mon Where link = ?", (link,))
        connection.commit()

    if day == "t":
        cursor.execute("DELETE FROM tue Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM tue Where link = ?", (link,))
        connection.commit()

    if day == "w":
        cursor.execute("DELETE FROM wed Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM wed Where link = ?", (link,))
        connection.commit()

    if day == "th":
        cursor.execute("DELETE FROM thu Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM thu Where link = ?", (link,))
        connection.commit()

    if day == "f":
        cursor.execute("DELETE FROM fri Where time_e = ?", (time_e,))
        cursor.execute("DELETE FROM fri Where link = ?", (link,))
        connection.commit()


def logout():

    connection.execute("DELETE FROM logins;")
    connection.commit()


add_button = Button(window, text="Add", width=14, command=add, bg="#586674")
add_button.place(anchor='center', relx=.75, rely=.38)

del_l_text = Label(window, text="to delete enter a day like this m or t or w or th or f :", bg="#36393e", fg="white",
                   font="none 12 bold")
del_l_text.place(anchor='center', relx=.75, rely=.44)

del_l_day_text = Label(window, text="day:", bg="#36393e", fg="white", font="none 12 bold")
del_l_day_text.place(anchor='center', relx=.6, rely=.49)

del_l_day_entry = Entry(window, width=10, bg="#434d56")
del_l_day_entry.place(anchor='center', relx=.68, rely=.49)

del_l_time_text = Label(window, text="time:", bg="#36393e", fg="white", font="none 12 bold")
del_l_time_text.place(anchor='center', relx=.6, rely=.55)

del_l_time_entry = Entry(window, width=10, bg="#434d56")
del_l_time_entry.place(anchor='center', relx=.68, rely=.55)

del_l_link_text = Label(window, text="link:", bg="#36393e", fg="white", font="none 12 bold")
del_l_link_text.place(anchor='center', relx=.6, rely=.6)

del_l_link_entry = Entry(window, width=40, bg="#434d56")
del_l_link_entry.place(anchor='center', relx=.79, rely=.6)

del_l_button = Button(window, text="Delete", width=14, command=del_l, bg="#586674")
del_l_button.place(anchor='center', relx=.748, rely=.7)

logout_button = Button(window, text="Logout", width=14, command=logout, bg="#586674")
logout_button.place(anchor='center', relx=.18, rely=.25)


def text_box_insert():

    text_box.delete(0.0, END)

    day = text_box_entry.get()

    if day == "logins":
        rows = cursor.execute("SELECT gmail FROM logins ").fetchone()
        line = "--------------------\n"
        text_box.insert(END, rows)
        text_box.insert(END, '\n')
        text_box.insert(END, line)

    if day == "m":
        rows1 = cursor.execute("SELECT time_e FROM mon ").fetchall()
        rows2 = cursor.execute("SELECT link FROM mon ").fetchall()
        rows_output1 = [i_m_t[0] for i_m_t in rows1]
        rows_output2 = [i_m_l[0] for i_m_l in rows2]

        z = 0
        line = "--------------------\n"

        for i in rows_output1:

            text_box.insert(END, i + '\n')
            text_box.insert(END, rows_output2[z] + '\n')
            text_box.insert(END, line)
            z += 1

    if day == "t":
        rows1 = cursor.execute("SELECT time_e FROM tue ").fetchall()
        rows2 = cursor.execute("SELECT link FROM tue ").fetchall()
        rows_output1 = [i_m_t[0] for i_m_t in rows1]
        rows_output2 = [i_m_l[0] for i_m_l in rows2]

        z = 0
        line = "--------------------\n"

        for i in rows_output1:
            text_box.insert(END, i + '\n')
            text_box.insert(END, rows_output2[z] + '\n')
            text_box.insert(END, line)
            z += 1

    if day == "w":
        rows1 = cursor.execute("SELECT time_e FROM wed ").fetchall()
        rows2 = cursor.execute("SELECT link FROM wed ").fetchall()
        rows_output1 = [i_m_t[0] for i_m_t in rows1]
        rows_output2 = [i_m_l[0] for i_m_l in rows2]

        z = 0
        line = "--------------------\n"

        for i in rows_output1:
            text_box.insert(END, i + '\n')
            text_box.insert(END, rows_output2[z] + '\n')
            text_box.insert(END, line)
            z += 1

    if day == "th":
        rows1 = cursor.execute("SELECT time_e FROM thu ").fetchall()
        rows2 = cursor.execute("SELECT link FROM thu ").fetchall()
        rows_output1 = [i_m_t[0] for i_m_t in rows1]
        rows_output2 = [i_m_l[0] for i_m_l in rows2]

        z = 0
        line = "--------------------\n"

        for i in rows_output1:
            text_box.insert(END, i + '\n')
            text_box.insert(END, rows_output2[z] + '\n')
            text_box.insert(END, line)
            z += 1

    if day == "f":
        rows1 = cursor.execute("SELECT time_e FROM fri ").fetchall()
        rows2 = cursor.execute("SELECT link FROM fri ").fetchall()
        rows_output1 = [i_m_t[0] for i_m_t in rows1]
        rows_output2 = [i_m_l[0] for i_m_l in rows2]

        z = 0
        line = "--------------------\n"

        for i in rows_output1:
            text_box.insert(END, i + '\n')
            text_box.insert(END, rows_output2[z] + '\n')
            text_box.insert(END, line)
            z += 1


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


def end():

    global j
    j += 1
    window.destroy()
    exit()


def start_program():

    m_t = 0

    t_t = 0

    w_t = 0

    th_t = 0

    f_t = 0

    connection = sqlite3.connect("class_meet.db")

    cursor = connection.cursor()

    start_button.config(text="started")

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

    global j
    j = 0

    while j == 0:
        schedule.run_pending()
        time.sleep(1)


exit_1 = Label(window, text="click to exit:", bg="#36393e", fg="white", font="none 12 bold")
exit_1.place(anchor='center', relx=.08, rely=.9)

exit_button = Button(window, text="Exit", width=14, command=end, bg="#586674")
exit_button.place(anchor='center', relx=.08, rely=.96)

text_box = Text(window, width=50, height=18, wrap=WORD, background="#434d56")
text_box.place(anchor='center', relx=.255, rely=.63)

text_text = Label(window, text="enter the 1st letter of a day to show the times you set:", bg="#36393e", fg="white",
                  font="none 12 bold")
text_text.place(anchor='center', relx=.26, rely=.31)

text_box_entry = Entry(window, width=10, bg="#434d56")
text_box_entry.place(anchor='center', relx=.045, rely=.355)

text_box_button = Button(window, text="show", width=10, command=text_box_insert, bg="#586674")
text_box_button.place(anchor='center', relx=.15, rely=.355)

start_button = Button(window, text="start", width=15, command=threading.Thread(target=start_program).start,
                      bg="#586674")
start_button.place(anchor='center', relx=.92, rely=.95)

start_text = Label(window, text="when you press start you wont be able to add or delete anything", bg="#36393e",
                   fg="white", font="none 12 bold")
start_text.place(anchor='center', relx=.54, rely=.95)

window.protocol("WM_DELETE_WINDOW", end)
window.mainloop()
connection.close()
