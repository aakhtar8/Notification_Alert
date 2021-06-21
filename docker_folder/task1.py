def headless_driver(path: str):
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=path, options=chrome_options)
    return driver
def get_notifications():
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    import time

    #PATH = "/media/Local Disk/courses/Apps/Notification_Alert/chromedriver"
    driver = headless_driver("/usr/bin/chromedriver")
    #driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("http://www.pu.edu.pk/")
    time.sleep(5)
    #time.sleep(2)
    #print(driver.title)
    # gettings notifications from the website
    notifications = driver.find_elements_by_tag_name("strong")
    with open("./data/notifications_new.txt", 'w') as f:
        for notification in notifications:
            f.write((notification.find_element_by_tag_name('a').text + "\n"))
    driver.quit()

        



