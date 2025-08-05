from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

def test_login_exitoso(driver):
    login(driver)
    assert "dashboard" in driver.current_url.lower()

def test_login_incorrecto(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("usuario_fake")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    mensaje = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
    ).text
    assert "Invalid credentials" in mensaje

def test_login_campos_vacios(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Esperar que el botón de login sea clickeable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()
    
    # Esperar mensajes de error en campos vacíos
    mensajes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-input-field-error-message"))
    )
    
    assert len(mensajes) > 0
