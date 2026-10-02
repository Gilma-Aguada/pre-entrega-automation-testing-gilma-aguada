from selenium.webdriver.common.by import By
from utils.helpers import iniciar_sesion

def test_01_login_exitoso(driver):
    iniciar_sesion(driver)
    assert "/inventory.html" in driver.current_url
    
    titulo_pagina = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in titulo_pagina
    print("Test 01: Login OK")

def test_02_verificar_catalogo(driver):
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_producto != ""
    assert precio_producto != ""
    print(f"Primer producto: {nombre_producto} - {precio_producto}")
    print("Test 02: Catálogo OK")