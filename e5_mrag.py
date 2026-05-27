# Marlon Astun
import pyfiglet
from colorama import Fore, Style
titulo = pyfiglet.figlet_format("Marlon")
print(Fore.RED + titulo + Style.RESET_ALL)
# Tupla que contiene las opciones del menu como pares (codigo, descripcion)
menu_soporte =(
    ("1", "Ver tickets abiertos"),
    ("2", "Registrar nuevos tickets"),
    ("3", "Cerrar tickets"),
    ("4", "Salir del sistema")
)
# Titulo del sistema
print("\n📋 Menu de soporte Tecnico")
# Mostramos cada opcion usando un ciclo
for codigo, descripcion in menu_soporte:
    print(f"{codigo}, {descripcion}")
# Inicializamos un bucle para que el usuario interactue
while True:
    # Solicitamos una opcion
    opcion = input("Seleccione una opcion (1-4): ")
    # Evaluamos cada opcion usando condicionales
    if opcion == "1":
        print("📖 Mostrando tickets abiertos...")
    elif opcion == "2":
        print("📝 Iniciando tickets abiertos...")
    elif opcion == "3":
        print("✅ Ticket cerrado correctametne")
    elif opcion == "4":
        print("🙇‍♀️ Saliendo del sistema. ¿Gracias!")
        break # Salimos del bucle
    else:
        print("✖️ Opcion invalida. Intente nuevamente.")