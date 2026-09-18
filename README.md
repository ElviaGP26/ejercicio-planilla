# Planilla de Consumo Eléctrico — CNEL EP

Este es un programa que hice en Python para simular la generación de planillas de consumo eléctrico de la empresa CNEL EP. Lo desarrollé como parte de la materia Tecnologías Disruptivas.

## Qué hace el programa

El programa pide por consola el nombre del cliente, el número de suministro y la cantidad de energía consumida en kWh. 
Con esos datos calcula el subtotal (multiplicando el consumo por 0,10 dólares, que es el precio fijo por kWh), luego le aplica el IVA del 15 % y finalmente muestra el total a pagar. 
Todo se presenta en una planilla ordenada, con títulos, separadores y los valores monetarios con dos decimales, tal como pedía la actividad.

.

## Mejoras que le añadí

Además de lo básico, fui añadiendo algunos detalles para que el programa quedara más completo y se viera más profesional:

- **Colores en la consola**: usé la librería colorama para que los títulos salgan en cian, las preguntas en amarillo, los totales en verde y el mensaje final en magenta. Esto hace que la planilla sea mucho más llamativa y fácil de leer.
- **Numeración automática**: cada vez que se genera una planilla, el número va aumentando (000001, 000002...). El último número se guarda en un archivo, así la numeración sigue aunque cierre el programa y lo vuelva a abrir. 
- **Varios clientes por ejecución**: el programa pregunta si quiero registrar otro cliente, así puedo generar varias planillas seguidas sin tener que ejecutarlo de nuevo.
.

- **Validación de datos**: si escribo algo que no es un número o pongo un consumo negativo, el programa me avisa con un mensaje y me pide el dato de nuevo, en vez de fallar. 
- **Guardado de planillas**: cada planilla generada se guarda también en un archivo de texto (`planillas_generadas.txt`), así puedo revisarlas después o mostrarlas como respaldo. 
- **Resumen final**: al terminar, el programa muestra cuántos clientes se atendieron, el total de kWh consumidos y el monto total facturado. 
- **Fecha automática**: cada planilla incluye la fecha del día en que se generó. 

## Cómo ejecutarlo

Solo necesitas Python 3 y la librería colorama, que se instala con el comando `pip install colorama`. Abres el archivo `Planilla_cnel.py` en Visual Studio Code, lo ejecutas y sigues las instrucciones que aparecen en pantalla. Al final, puedes revisar las planillas guardadas en `planillas_generadas.txt`.
