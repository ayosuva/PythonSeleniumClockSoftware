import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome(
        "C:\\Yosuva\Python Workspace\\SeleniumPython\\booking\\libs\\chromedriver.exe")  # Optional argument, if not specified will search path.
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get("https://www.instagram.com/instagram/");
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Allow essential and optional cookies']").click();
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[text()='Log in']").click();
    driver.find_element(By.NAME, "username").send_keys('username')
    driver.find_element(By.NAME, "password").send_keys('password')
    driver.find_element(By.XPATH, "//div[text()='Log In']").click();
    driver.find_element(By.XPATH, "//button[text()='Not now']").click();

    driver.find_element(By.XPATH, "//button[text()='Not Now']").click();
    # it open Instagram page and clicks 1st post and then it will click next post button for the specified range
    driver.get("https://www.instagram.com/instagram/");
    driver.find_element(By.XPATH, "//div[@class='v1Nh3 kIKUG  _bz0w']").click();

    for page in range(1, 10):
        driver.find_element(By.XPATH, "//button[@class='wpO6b  ']//*[@aria-label='Next']").click();
        time.sleep(2)
    driver.quit()