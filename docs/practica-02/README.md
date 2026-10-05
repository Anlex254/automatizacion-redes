# Práctica 2 - Construcción de la red simulada en GNS3

## Descripción

En esta práctica se construyeron y configuraron dos topologías de red utilizando GNS3. El objetivo fue comprobar el funcionamiento de los dispositivos, realizar pruebas de conectividad y configurar el protocolo OSPF para establecer comunicación entre los routers.

## Topología 1

La primera topología está formada por dos equipos VPCS conectados mediante un switch Ethernet.

Direcciones utilizadas:

- PC1: 10.1.1.1/24
- PC2: 10.1.1.2/24

Se realizaron pruebas de ping entre PC1 y PC2 en ambos sentidos para comprobar la conectividad.

La información de esta topología se encuentra en:

`topologia-01/`

## Topología 2

La segunda topología está formada por dos routers Cisco IOSv y un switch Cisco IOSvL2.

Direcciones utilizadas:

- R1 GigabitEthernet0/0: 10.1.1.1/24
- R1 Loopback0: 1.1.1.1/32
- R2 GigabitEthernet0/0: 10.1.1.2/24
- R2 Loopback0: 2.2.2.2/32
- S1 VLAN 1: 10.1.1.3/24

En R1 y R2 se configuró OSPF utilizando el proceso 1 y el área 0. Posteriormente se verificó la relación de vecinos OSPF y las rutas aprendidas mediante los comandos:

```text
show ip ospf neighbor
show ip route
```

Las pruebas realizadas mostraron que los routers establecieron correctamente la relación de vecinos OSPF y aprendieron las rutas hacia las interfaces Loopback.

La información de esta topología se encuentra en:

`topologia-02/`

## Evidencias

Las capturas de las topologías, configuraciones y pruebas realizadas se encuentran dentro de las carpetas `evidencias` correspondientes a cada topología.

## Resultado

Las dos topologías fueron construidas y configuradas correctamente. Se comprobó la comunicación entre los dispositivos mediante pruebas de ping y se verificó el funcionamiento de OSPF en la segunda topología.

## Bitácora de problemas y soluciones

| Problema encontrado | Posible causa | Solución aplicada | Resultado |
|---|---|---|---|
| Al configurar el switch S1 apareció un mensaje de comando inválido. | Algunos comandos se ingresaron juntos y el dispositivo no pudo interpretarlos correctamente. | Se ingresaron nuevamente los comandos de configuración de la interfaz VLAN 1 de forma correcta y por separado. | La interfaz VLAN 1 quedó configurada con la dirección 10.1.1.3 y en funcionamiento. |
| En la primera prueba de ping desde S1 no se obtuvo respuesta en todos los paquetes. | El dispositivo necesitaba resolver inicialmente las direcciones de los equipos de la red. | Se repitió la prueba de conectividad después de esperar unos segundos. | La segunda prueba de ping se completó correctamente con 100% de respuesta. |

## Integración con el proyecto

### a ¿Qué elementos de la red construida podrían ser automatizados posteriormente mediante Python?

Se podrían automatizar tareas como la configuración de direcciones IP, interfaces, rutas y protocolos de enrutamiento como OSPF.

### b ¿Qué información de los dispositivos podría obtenerse mediante un script?

Se podría obtener información como las direcciones IP, el estado de las interfaces, las tablas de enrutamiento y los vecinos OSPF.

### c ¿Qué configuraciones podrían modificarse automáticamente?

Se podrían modificar las direcciones IP, activar o desactivar interfaces y realizar cambios en la configuración de OSPF.

### d ¿Por qué es importante contar con una red de laboratorio antes de automatizar dispositivos reales?

Porque permite realizar pruebas y detectar errores sin afectar una red real ni los dispositivos que se encuentran en funcionamiento.

### e ¿Cómo podría utilizarse esta infraestructura para probar los programas desarrollados durante las siguientes prácticas?

Se puede utilizar como un entorno de prueba para ejecutar los programas de automatización, comprobar los cambios realizados y verificar que funcionen correctamente antes de utilizarlos en una red real.