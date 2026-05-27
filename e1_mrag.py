# Marlon Astun
import pyfiglet
from colorama import Fore, Style
titulo = pyfiglet.figlet_format("Marlon")
print(Fore.RED + titulo + Style.RESET_ALL)

empleados_autorizados = ("Ana", "Carlos", "Luis", "Marta", "Sofia",
            "Carlitos", "Navarrin", "Angelito", "Luisito", "Angel")

print("🔓Verificación de acceso al sistema")
nombre = input("Ingrese su nombre: ")

if nombre in empleados_autorizados:
    print(f"🔑Acceso concedido a {nombre}")
else:
    print("🔏Acceso denegado. Usuario no autorizado.")