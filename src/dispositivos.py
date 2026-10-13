# Lista de dispositivos de la topología
dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "plataforma": "IOSv",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "2.2.2.2",
        "estado": "Activo",
        "fabricante": "Cisco",
        "plataforma": "IOSv",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "Cisco",
        "plataforma": "IOSvL2",
        "protocolo": "No aplica"
    }
]

# Función para mostrar la información de un dispositivo
def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Plataforma:", dispositivo["plataforma"])
    print("Protocolo:", dispositivo["protocolo"])

    if dispositivo["estado"] == "Activo":
        print("El dispositivo está disponible.")
    else:
        print("El dispositivo requiere atención.")

# Mostrar todos los dispositivos
for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("--------------------")






    # Función para buscar un dispositivo por su nombre
def buscar_dispositivo(nombre):
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == nombre.lower():
            return dispositivo
    return None

# Solicitar el nombre del dispositivo
nombre_buscar = input("Ingrese el nombre del dispositivo: ")

resultado = buscar_dispositivo(nombre_buscar)

if resultado:
    print("\nDispositivo encontrado:")
    mostrar_dispositivo(resultado)
else:
    print("\nDispositivo no encontrado.")