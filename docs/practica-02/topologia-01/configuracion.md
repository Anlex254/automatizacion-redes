# Configuración de la Topología 1

## PC1

Dirección IP configurada:

`10.1.1.1 255.255.255.0`

Comandos utilizados:

```text
ip 10.1.1.1 255.255.255.0
save
```

## PC2

Dirección IP configurada:

`10.1.1.2 255.255.255.0`

Comandos utilizados:

```text
ip 10.1.1.2 255.255.255.0
save
```

## Pruebas de conectividad

Desde PC1 se realizó una prueba de conectividad hacia PC2:

```text
ping 10.1.1.2
```

Desde PC2 se realizó una prueba de conectividad hacia PC1:

```text
ping 10.1.1.1
```

Las pruebas de ping fueron exitosas en ambos sentidos, comprobando la comunicación entre los dos equipos.