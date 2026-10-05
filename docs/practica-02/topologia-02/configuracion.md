# Configuración de la Topología 2

## R1

Se configuró la interfaz GigabitEthernet0/0 con la dirección IP 10.1.1.1/24 y una interfaz Loopback con la dirección 1.1.1.1/32.

```text
interface GigabitEthernet0/0
ip address 10.1.1.1 255.255.255.0
no shutdown

interface Loopback0
ip address 1.1.1.1 255.255.255.255
```

También se configuró el protocolo OSPF con el proceso 1 y el área 0.

```text
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
```

## R2

Se configuró la interfaz GigabitEthernet0/0 con la dirección IP 10.1.1.2/24 y una interfaz Loopback con la dirección 2.2.2.2/32.

```text
interface GigabitEthernet0/0
ip address 10.1.1.2 255.255.255.0
no shutdown

interface Loopback0
ip address 2.2.2.2 255.255.255.255
```

También se configuró OSPF con el proceso 1 y el área 0.

```text
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
```

## S1

Se configuró la interfaz VLAN 1 del switch con la dirección IP 10.1.1.3/24.

```text
interface vlan 1
ip address 10.1.1.3 255.255.255.0
no shutdown
```

## Pruebas de conectividad

Desde R1 se realizó ping hacia R2:

```text
ping 10.1.1.2
```

Desde R2 se realizó ping hacia R1:

```text
ping 10.1.1.1
```

Las pruebas obtuvieron un resultado exitoso del 100%.

## Verificación de OSPF

Para comprobar la relación de vecinos OSPF se utilizó:

```text
show ip ospf neighbor
```

Los routers establecieron correctamente la relación de vecinos, mostrando el estado FULL.

Para comprobar las rutas aprendidas se utilizó:

```text
show ip route
```

R1 aprendió mediante OSPF la ruta hacia 2.2.2.2 y R2 aprendió mediante OSPF la ruta hacia 1.1.1.1.

Finalmente, las configuraciones de los dispositivos fueron guardadas utilizando:

```text
write memory
```