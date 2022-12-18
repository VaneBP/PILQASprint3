import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service



#Se abre la página asiganda
driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bensimon.com.ar/")

#Busca el botón que despliega los campos a llenar para loguearse y le hace click
searchUsuario =  driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[5]/div/div/button")
searchUsuario.send_keys(Keys.ENTER)
time.sleep(2)

#Elige la opción para ingresar con Usuario y Contraseña
botonLogin =  driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[2]/div/button")
botonLogin.send_keys(Keys.ENTER)
time.sleep(3)

#Busca el campo para ingresar el email y lo escribe
campoEmail = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/label/div/input")
campoEmail.send_keys("vane_bastiap@hotmail.com")
time.sleep(2)

##Busca el campo para ingresar la contraseña y la escribe
campoContraseña = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/label/div/input")
campoContraseña.send_keys("Galuchi123")
time.sleep(2)

#Hace click en el botón "Entrar" para terminar de loguearse
botonEntrar = driver.find_element(
    By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div[2]/button")
botonEntrar.send_keys(Keys.ENTER)
time.sleep(2)

#Escribe el producto "Bermuda" en el campo de búsqueda
campoBusqueda = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/section/div/div/section/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/label/div/input")
campoBusqueda.send_keys("bermuda")
campoBusqueda.send_keys(Keys.ENTER)
time.sleep(5)

#Hace click en el producto "Bermuda Santos Summer" 
bermudaSummer = driver.find_element(
    By.XPATH, "/html/body/div[2]/div/div[1]/div/div[3]/div/div/section/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/section/a")
bermudaSummer.send_keys(Keys.ENTER)
time.sleep(2)

#Elige eltalle 28
talle28 = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]"  
)
talle28.send_keys(Keys.ENTER)
time.sleep(2)

#Agregar al carrito
agregarCarrito = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[6]/div/div/div/button"  
)
agregarCarrito.send_keys(Keys.ENTER)
time.sleep(2)

#Elige eltalle 30
talle30 = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div[2]"  
)
talle30.send_keys(Keys.ENTER)
time.sleep(2)

#Agregar al carrito
agregarCarrito = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[6]/div/div/div/button"  
)
agregarCarrito.send_keys(Keys.ENTER)
time.sleep(2)

#Elige eltalle 32
talle32 = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[2]/div[3]"  
)
talle32.send_keys(Keys.ENTER)
time.sleep(2)

#Agregar al carrito
agregarCarrito = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[2]/div/div[6]/div/div/div/button"  
)
agregarCarrito.send_keys(Keys.ENTER)
time.sleep(2)

#Cerrar pedido
cerrarPedido = driver.find_element(
  By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div/section/div/div[3]/div/div/div/div[2]/a"  
)
cerrarPedido.send_keys(Keys.ENTER)
time.sleep(2)

#Elimina un producto con X
eliminarProducto = driver.find_element(
  By.XPATH, "/html/body/div[4]/div[3]/div[1]/div[1]/div[2]/table/tbody/tr[1]/div/td[7]/a"  
)
eliminarProducto.send_keys(Keys.ENTER)
time.sleep(2)


