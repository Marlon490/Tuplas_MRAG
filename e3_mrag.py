# Marlon Astun
import pyfiglet
from colorama import Fore, Style
titulo = pyfiglet.figlet_format("Marlon")
print(Fore.RED + titulo + Style.RESET_ALL)
# Tupla que contiene los salarios de los empleados
salarios = (5500, 6200, 4800, 7100, 5900)
# Inicializamos la suma total
total = 0
# Recorrer la tupla y sumamos cada salario
for salario in salarios:
    total += salario
# Mostramos el total acumulado
print("\n📃 Total ded salarios a pagar este mes: Q", total)