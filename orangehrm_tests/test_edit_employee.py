from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from utils import login

def test_editar_empleado(driver):
    login(driver)

    # Ir a PIM
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()

    # Seleccionar primer empleado
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "oxd-table-card"))
    ).click()

    # Editar nombre
    campo_nombre = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    )
    # Borrar usando teclas para asegurar campo vacío
    campo_nombre.send_keys(Keys.CONTROL + "a")
    campo_nombre.send_keys(Keys.DELETE)
    campo_nombre.send_keys("CarlosEditado")

    # Guardar cambios
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Esperar que el cambio se refleje
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.NAME, "firstName"), "CarlosEditado")
    )

    # Validar valor exacto
    valor_actual = driver.find_element(By.NAME, "firstName").get_attribute("value").strip()
    assert valor_actual == "CarlosEditado"
