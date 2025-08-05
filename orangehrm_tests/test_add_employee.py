from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login, ir_a_pim

def test_agregar_empleado_exitoso(driver):
    login(driver)
    ir_a_pim(driver)

    # Ir a "Add Employee"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))
    ).click()

    # Llenar datos
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    ).send_keys("Juan")
    driver.find_element(By.NAME, "lastName").send_keys("Perez")

    # Guardar
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Esperar que aparezca el título "Personal Details"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
    )

    # Validar que estamos en la página de detalles del empleado
    titulo = driver.find_element(By.XPATH, "//h6[text()='Personal Details']").text
    assert titulo == "Personal Details"


def test_agregar_empleado_sin_datos(driver):
    login(driver)
    ir_a_pim(driver)

    # Ir a Add Employee
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))
    ).click()

    # Hacer clic en Guardar sin llenar datos
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Verificar que aparecen mensajes de error
    errores = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-input-field-error-message"))
    )
    assert len(errores) > 0
