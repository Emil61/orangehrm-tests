from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, usuario="Admin", clave="admin123"):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Esperar campo usuario
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys(usuario)

    driver.find_element(By.NAME, "password").send_keys(clave)

    # Click en login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Esperar a que aparezca el menú lateral con PIM
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "PIM"))
    )

def ir_a_pim(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()

