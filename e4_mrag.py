# Marlon Astun
import pyfiglet
from colorama import Fore, Style
titulo = pyfiglet.figlet_format("Marlon")
print(Fore.RED + titulo + Style.RESET_ALL)
# Definimos tuplas con los nombres de empleados presentes por dia
lunes = ("Lucia", "Carlos", "Sofia")
martes = ("Lucia", "Carlos", "Sofia")
miercoles = ("Maria", "Luisito", "Angelito")
jueves = ("Lucia", "Carlos", "Sofia")
viernes = ("Luis", "Marta", "Sofia")
# Solicitamos al usuario el nombre del empleado a revisar
nombre = input("\n📠 Ingrese el nombre del empleado para revisar su asistencia: ")
# Inicializamos el contador de dias presente
presente = 0
# Verificamos si el empleado estuvo presente cada dia
if nombre in lunes:
    presente += 1
if nombre in martes:
    presente += 1
if nombre in miercoles:
    presente += 1
if nombre in jueves:
    presente += 1
if nombre in viernes:
    presente += 1
# Mostramos cuantos dias asistio el empleado
print(f"📝 {nombre} asistio {presente} dias esta semana")