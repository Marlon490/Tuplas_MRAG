# Marlon Astun
import pyfiglet
from colorama import Fore, Style
titulo = pyfiglet.figlet_format("Marlon")
print(Fore.RED + titulo + Style.RESET_ALL)
# Creamos una tupla de tuplas cada una con nombre y precio de producto
productos = (("Aspiradora", 600), ("Laptop", 1700), ("Mouse", 300), ("Teclado", 150),
            ("Termometro", 3000), ("Cafetera", 500), ("Freidora", 300), ("Batidora", 500),
             ("Laptop", 6000), ("Rasuradora", 600))

# Mostramos titulo del listado
print("\n🖥️ Lista de productos tecnológicos disponibles. ")

# Recorremos la tupla principal con un ciclo
for producto, precio in productos:
    # Imprimimos cada producto con su precio formateando
    print(f" {producto}: Q {precio}")