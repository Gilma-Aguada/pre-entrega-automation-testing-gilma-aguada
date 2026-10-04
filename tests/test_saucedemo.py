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

def test_03_agregar_al_carrito(driver):
    iniciar_sesion(driver)
    
    # 1. Agregar el primer producto al carrito
    boton_agregar = driver.find_element(By.CLASS_NAME, "btn_inventory")
    primer_producto_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    boton_agregar.click()
    
    # 2. Verificar que el contador del carrito se incremente a "1"
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge_carrito.text == "1", "El contador del carrito no se actualizó a 1"
    
    # 3. Navegar al carrito de compras
    badge_carrito.click()
    assert "/cart.html" in driver.current_url, "No se navegó correctamente al carrito"
    
    # 4. Comprobar que el producto añadido aparezca correctamente en el carrito
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_en_carrito == primer_producto_nombre, "El producto en el carrito no coincide"
    
    print("Test 03: Interacción con carrito OK")