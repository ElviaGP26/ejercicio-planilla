# ============================================================
# PROGRAMA: Planilla de consumo eléctrico - CNEL EP
# Materia: Tecnologías disruptivas
# ============================================================

import os
from colorama import init, Fore, Style
from datetime import datetime

# Inicializar colorama 
init(autoreset=True)

# --- CONFIGURACIÓN ---
precio_kwh = 0.10
iva_porcentaje = 0.15
archivo_numero = "numero_planilla.txt"
archivo_planillas = "planillas_generadas.txt"

# --- NÚMERO DE PLANILLA AUTOMÁTICO ---
if os.path.exists(archivo_numero):
    with open(archivo_numero, "r", encoding="utf-8") as archivo:
        numero_planilla = int(archivo.read().strip())
else:
    numero_planilla = 0

# --- BIENVENIDA ---
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
print(Fore.CYAN + Style.BRIGHT + "   BIENVENIDO AL SISTEMA DE PLANILLAS CNEL EP")
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
print()

# --- LISTAS PARA EL RESUMEN FINAL ---
clientes = []
consumos = []
totales = []

continuar = "s"

while continuar.lower() == "s":
    numero_planilla += 1
    numero_planilla_texto = f"{numero_planilla:06d}"

    # ENTRADA DE DATOS CON VALIDACIÓN
    nombre = input(Fore.YELLOW + "Ingrese el nombre del cliente: ")
    suministro = input(Fore.YELLOW + "Ingrese el número de suministro: ")

    while True:
        try:
            consumo_kwh = float(input(Fore.YELLOW + "Ingrese la cantidad de energía consumida en kWh: "))
            if consumo_kwh < 0:
                print(Fore.RED + "El consumo no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Eso no es un número válido. Intente de nuevo.")

    # CÁLCULOS
    subtotal = consumo_kwh * precio_kwh
    iva = subtotal * iva_porcentaje
    total = subtotal + iva
    fecha = datetime.now().strftime("%d/%m/%Y")

    # GUARDAR DATOS PARA EL RESUMEN
    clientes.append(nombre)
    consumos.append(consumo_kwh)
    totales.append(total)

    # --- IMPRIMIR PLANILLA ---
    print()
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print(Fore.CYAN + Style.BRIGHT + "                 CNEL EP - UNIDAD DE NEGOCIO")
    print(Fore.CYAN + Style.BRIGHT + "                PLANILLA DE ENERGÍA ELÉCTRICA")
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print(Fore.WHITE + f"Planilla N.º: {numero_planilla_texto}        Fecha: {fecha}")
    print(Fore.WHITE + f"Cliente:       {nombre.upper()}")
    print(Fore.WHITE + f"Suministro:    {suministro}")
    print(Fore.WHITE + "-" * 62)
    print(Fore.WHITE + "N.º  DESCRIPCIÓN            CONSUMO   V. UNITARIO    TOTAL")
    print(Fore.WHITE + "-" * 62)
    print(Fore.WHITE + f"1    Energía eléctrica       {consumo_kwh:.0f} kWh    USD {precio_kwh:.2f}    USD {subtotal:.2f}")
    print(Fore.WHITE + "-" * 62)
    print(Fore.GREEN + f"                                      SUBTOTAL:     USD {subtotal:.2f}")
    print(Fore.GREEN + f"                                      IVA 15 %:     USD {iva:.2f}")
    print(Fore.GREEN + Style.BRIGHT + f"                                      TOTAL:        USD {total:.2f}")
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print(Fore.MAGENTA + Style.BRIGHT + "              GRACIAS POR REALIZAR SU PAGO")
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print()

    # GUARDAR LA PLANILLA EN EL ARCHIVO
    with open(archivo_planillas, "a", encoding="utf-8") as archivo:
        archivo.write("=" * 62 + "\n")
        archivo.write("                 CNEL EP - UNIDAD DE NEGOCIO\n")
        archivo.write("                PLANILLA DE ENERGÍA ELÉCTRICA\n")
        archivo.write("=" * 62 + "\n")
        archivo.write(f"Planilla N.º: {numero_planilla_texto}        Fecha: {fecha}\n")
        archivo.write(f"Cliente:       {nombre.upper()}\n")
        archivo.write(f"Suministro:    {suministro}\n")
        archivo.write("-" * 62 + "\n")
        archivo.write("N.º  DESCRIPCIÓN            CONSUMO   V. UNITARIO    TOTAL\n")
        archivo.write("-" * 62 + "\n")
        archivo.write(f"1    Energía eléctrica       {consumo_kwh:.0f} kWh    USD {precio_kwh:.2f}    USD {subtotal:.2f}\n")
        archivo.write("-" * 62 + "\n")
        archivo.write(f"                                      SUBTOTAL:     USD {subtotal:.2f}\n")
        archivo.write(f"                                      IVA 15 %:     USD {iva:.2f}\n")
        archivo.write(f"                                      TOTAL:        USD {total:.2f}\n")
        archivo.write("=" * 62 + "\n")
        archivo.write("              GRACIAS POR REALIZAR SU PAGO\n")
        archivo.write("=" * 62 + "\n\n")

    continuar = input(Fore.YELLOW + "¿Desea registrar otro cliente? (s/n): ")

# GUARDAR EL NÚMERO DE PLANILLA ACTUALIZADO
with open(archivo_numero, "w", encoding="utf-8") as archivo:
    archivo.write(str(numero_planilla))

# --- RESUMEN FINAL DE LA JORNADA ---
print()
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
print(Fore.CYAN + Style.BRIGHT + "                 RESUMEN DE LA JORNADA")
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
total_kwh = sum(consumos)
total_dinero = sum(totales)
print(Fore.WHITE + f"Clientes atendidos:  {len(clientes)}")
print(Fore.WHITE + f"Energía total:       {total_kwh:.2f} kWh")
print(Fore.GREEN + Style.BRIGHT + f"Monto total:         USD {total_dinero:.2f}")
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
print(Fore.MAGENTA + Style.BRIGHT + "Las planillas se guardaron en: " + archivo_planillas)
print(Fore.CYAN + Style.BRIGHT + "=" * 62)
