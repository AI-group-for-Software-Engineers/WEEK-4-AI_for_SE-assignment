from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

def full_page_screenshot(driver, file_name):
    # Adjust window size to full height
    page_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, page_height)
    driver.save_screenshot(file_name)
    print(f"✅ Full page screenshot saved: {file_name}")


def test_valid_login():
    print("🔹 Running VALID login test...")

    options = Options()
    service = Service(r"msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    full_page_screenshot(driver, "valid_login_fullpage.png")

    input("Press ENTER to close (valid test)...")
    driver.quit()


def test_invalid_login():
    print("🔹 Running INVALID login test...")

    options = Options()
    service = Service(r"msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    full_page_screenshot(driver, "invalid_login_fullpage.png")

    input("Press ENTER to close (invalid test)...")
    driver.quit()


# Run both tests
test_valid_login()
test_invalid_login()
















