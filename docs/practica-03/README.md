    # Práctica 3 - Primer programa de Python para representar información de dispositivos

## 1. Propósito

El propósito de esta práctica fue desarrollar un programa en Python capaz de representar y mostrar información de los dispositivos utilizados en la infraestructura de red construida previamente en GNS3.

Se utilizaron los datos de los dispositivos R1, R2 y S1 de la Práctica 2, incluyendo sus direcciones IP, estado, fabricante, plataforma y protocolo de enrutamiento. Además, se utilizaron diferentes elementos de Python para organizar y procesar la información de los dispositivos.

## 2. Conceptos utilizados

### Variables
Las variables permiten almacenar información dentro de un programa. Durante la práctica se utilizaron inicialmente para representar datos como el nombre, tipo, dirección IP, interfaz y estado de un dispositivo.

### Tipos de datos
Los datos utilizados principalmente fueron cadenas de texto (`str`), ya que la información de los dispositivos, como sus nombres, direcciones IP y estados, fue almacenada como texto.

### print()
La función `print()` se utilizó para mostrar en la terminal la información almacenada de cada dispositivo.

### Diccionarios
Los diccionarios permitieron agrupar la información relacionada con cada dispositivo mediante claves como `nombre`, `tipo`, `ip` y `estado`.

### Listas
Se utilizó una lista para almacenar los diccionarios correspondientes a R1, R2 y S1, permitiendo representar varios dispositivos dentro de una misma estructura.

### Ciclo for
El ciclo `for` permitió recorrer la lista de dispositivos y procesar cada uno de ellos sin tener que repetir manualmente el mismo código.

### Condicional if
La estructura `if` se utilizó para comprobar el estado de cada dispositivo. Si su estado era `Activo`, el programa indicaba que se encontraba disponible; de lo contrario, indicaba que requería atención.

### Funciones
Se creó la función `mostrar_dispositivo()` para mostrar de manera organizada la información de cada dispositivo. Esto permitió reutilizar el mismo código para R1, R2 y S1.

## 3. Dispositivos representados

Los dispositivos representados en el programa corresponden a la segunda topología desarrollada en GNS3 durante la Práctica 2.

| Dispositivo | Tipo | Dirección IP | Estado | Función |
|---|---|---|---|---|
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento mediante OSPF |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento mediante OSPF |
| S1 | Switch | 10.1.1.3 | Activo | Conectividad entre dispositivos |

## Pruebas realizadas

| Prueba | Resultado esperado | Resultado obtenido |
|---|---|---|
| Mostrar dispositivos | Se muestran todos los dispositivos | Se mostraron correctamente R1, R2 y S1 |
| Mostrar IP | Aparece la IP de cada dispositivo | Se mostraron correctamente las direcciones IP |
| Verificar estado | Se identifica el estado | Se identificó correctamente el estado de cada dispositivo |
| Modificar IP | Se muestra el nuevo valor | R1 mostró temporalmente la dirección IP 10.1.1.100 |
| Restaurar información | Se recupera el valor correcto | La dirección IP de R1 se restauró correctamente a 10.1.1.1 |

## 4. Evidencias

Durante el desarrollo de la práctica se realizaron capturas de pantalla para comprobar cada una de las etapas del programa.

Las evidencias incluyen:

- Estructura actual del repositorio.
- Código inicial desarrollado en Python.
- Ejecución correcta del programa.
- Representación de los dispositivos R1 y R2.
- Uso de listas y diccionarios para representar R1, R2 y S1.
- Ejecución del ciclo `for`.
- Uso de la estructura condicional `if`.
- Uso de la función `mostrar_dispositivo()`.
- Prueba de modificación temporal de la dirección IP de R1.
- Restauración de la información original.
- Ejecución final del programa.

## 5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| No se presentaron problemas durante el desarrollo de la práctica. | No aplica. | No aplica. |

## 6. Conclusión

Durante esta práctica se utilizaron diferentes conceptos de Python para representar la información de los dispositivos de una red. Se emplearon variables, diccionarios y listas para almacenar y organizar los datos de los routers y el switch utilizados previamente en GNS3. También se utilizaron ciclos `for` para recorrer los dispositivos, estructuras condicionales `if` para verificar su estado y funciones para reutilizar código y mantener el programa organizado.

Las pruebas realizadas permitieron comprobar que el programa puede mostrar y procesar correctamente la información de R1, R2 y S1. Con esta práctica se estableció una base para las siguientes etapas del proyecto integrador, en las que Python podrá utilizarse para obtener información directamente de los dispositivos y realizar tareas de automatización sobre la infraestructura de red.