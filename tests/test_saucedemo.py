from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import iniciar_sesion

def test_01_login_exitoso(driver):
    iniciar_sesion(driver)
    assert "/inventory.html" in driver.current_url
    
    titulo_pagina = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in titulo_pagina
    print("Test 01: Login OK")

def test_02_verificar_catalogo(driver):
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos visibles en el inventario"

    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_producto != ""
    assert precio_producto != ""
    print(f"Primer producto: {nombre_producto} - {precio_producto}")
    print("Test 02: Catálogo OK")

def test_03_agregar_producto_al_carrito(driver):
    iniciar_sesion(driver)
    
    wait = WebDriverWait(driver, 10)
    
    # 1. Esperar a que el botón de agregar esté listo y hacer clic
    boton_agregar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
    boton_agregar.click()
    
    print("Test 03: Producto agregado al carrito OK")

def test_04_verificar_detalle_producto(driver):
    iniciar_sesion(driver)
    
    wait = WebDriverWait(driver, 10)
    
    # 1. Esperar a que el nombre del primer producto sea clickeable y hacer clic para ver su detalle
    enlace_producto = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
    nombre_esperado = enlace_producto.text
    enlace_producto.click()
    
    # 2. Esperar a que la URL cambie a la vista de detalle del producto
    wait.until(EC.url_contains("/inventory-item.html?id="))
    assert "/inventory-item.html" in driver.current_url, "No se navegó a la vista de detalle del producto"
    
    # 3. Comprobar que el producto en la vista de detalle coincida
    nombre_en_detalle = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name"))).text
    assert nombre_en_detalle == nombre_esperado, "El nombre del producto en detalle no coincide"
    
    print("Test 04: Verificación de detalle de producto OK")

def test_05_filtrar_productos_por_nombre(driver):
    iniciar_sesion(driver)
    
    wait = WebDriverWait(driver, 10)
    
    # 1. Esperar a que el selector de ordenamiento esté disponible en la página
    elemento_select = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(elemento_select)
    
    # 2. Seleccionar el filtro de ordenamiento alfabético inverso por nombre (de Z a A)
    select.select_by_value("za")
    
    # 3. Verificar que el primer producto de la lista filtrada muestre su nombre correctamente
    primer_producto_filtrado = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    assert primer_producto_filtrado != "", "El producto filtrado no muestra nombre"
    
    print(f"Primer producto filtrado por nombre: {primer_producto_filtrado}")
    print("Test 05: Filtrado de productos por nombre OK")