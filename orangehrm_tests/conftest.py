import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Crear carpeta de capturas si no existe
os.makedirs("screenshots", exist_ok=True)

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver  # Aquí se ejecuta el test

    # Tomar captura antes de cerrar el navegador
    test_name = request.node.name
    status = "PASSED" if request.node.rep_call.passed else "FAILED"
    file_name = os.path.join("screenshots", f"{test_name}_{status}.png")
    driver.save_screenshot(file_name)

    driver.quit()

# Guardar el resultado del test para usarlo en el fixture
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
