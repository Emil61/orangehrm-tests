from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

def test_listar_empleados(driver):
    login(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()
    filas = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-table-card"))
    )
    assert len(filas) > 0


def test_buscar_empleado_inexistente(driver):
    login(driver)

    # Ir a PIM
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))
    ).click()

    # Esperar que la tabla esté lista antes de buscar
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-table-card"))
    )

    # Usar placeholder para encontrar el campo
    campo_busqueda = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Type for hints...']"))
    )
    campo_busqueda.clear()
    campo_busqueda.send_keys("EmpleadoInexistente")

    # Click en botón buscar
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Verificar mensaje "No Records Found"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='No Records Found']"))
    )
    assert "No Records Found" in driver.page_source