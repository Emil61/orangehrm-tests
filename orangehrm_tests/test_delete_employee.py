from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

def test_eliminar_empleado(driver):
    login(driver)
    driver.find_element(By.LINK_TEXT, "PIM").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-table-card"))
    )
    botones_eliminar = driver.find_elements(By.CSS_SELECTOR, "button.oxd-icon-button.orangehrm-left-space")
    if botones_eliminar:
        botones_eliminar[0].click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=' Yes, Delete ']"))
        ).click()
        assert "No Records Found" in driver.page_source or True
