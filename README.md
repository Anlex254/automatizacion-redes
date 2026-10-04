# Mi estación de automatización de redes

## 1. Datos del equipo

**Asignatura:** Automatización de Infraestructura Digital I

**Práctica:** 01 - Mi estación de automatización de redes

**Grupo:** 3IRI2V

**Fecha:** 4/10/2026

**Integrantes:**
- Angel Guadalupe Flores Cuellar
- Coral Guadalupe Garcia Camacho
- Paola Berenice Vega Montemayor
- Yatana Alexandra Nieto

---

## 2. Propósito de la práctica

El propósito de esta práctica fue preparar una estación de trabajo para la automatización de redes mediante la instalación, configuración y verificación de diferentes herramientas de desarrollo, control de versiones, pruebas de servicios, virtualización y laboratorio de redes.

La práctica permitió preparar el entorno necesario para desarrollar posteriormente scripts y realizar actividades de automatización de infraestructura digital.

---

## 3. Herramientas instaladas

Durante la práctica se instalaron y configuraron las siguientes herramientas:

- Python
- Visual Studio Code
- Extensión de Python para Visual Studio Code
- Entorno virtual de Python
- Git
- GitHub
- Postman
- OpenConnect
- Docker Desktop
- WSL 2
- Ubuntu
- GNS3 GUI
- GNS3 VM
- VMware Workstation

---

## 4. Configuración realizada

Durante la práctica se realizaron las siguientes actividades:

### Entorno de programación

- Se instaló Python 3.
- Se verificó la versión de Python desde la terminal.
- Se instaló Visual Studio Code.
- Se instaló la extensión de Python para Visual Studio Code.
- Se seleccionó el intérprete de Python.
- Se creó la carpeta de trabajo del proyecto.
- Se creó y configuró un entorno virtual de Python.
- Se creó el archivo `hola_mundo.py`.
- Se ejecutó el programa "Hola Mundo" desde Visual Studio Code.

### Herramientas de desarrollo colaborativo

- Se instaló Git.
- Se configuró la identidad de Git mediante nombre de usuario y correo electrónico.
- Se creó el repositorio del proyecto en GitHub.
- Se instaló Postman para realizar pruebas de APIs.
- Se instaló OpenConnect.
- Se instaló Docker Desktop.

### Docker y WSL

- Se comprobó la instalación de Docker mediante el comando `docker --version`.
- Se habilitaron los componentes necesarios de Windows para utilizar WSL y Virtual Machine Platform.
- Se instaló una distribución Ubuntu mediante WSL 2.
- Se realizaron las configuraciones necesarias para utilizar Docker.

### Laboratorio virtual de redes

- Se instaló GNS3.
- Se descargó la GNS3 VM.
- Se instaló VMware Workstation.
- Se importó la GNS3 VM en VMware Workstation.
- Se configuró GNS3 GUI para utilizar la GNS3 VM.
- Se verificó que la GNS3 VM iniciara correctamente.
- Se comprobó la integración entre GNS3 GUI y la GNS3 VM.

---

## 5. Verificación del entorno

Se realizaron diferentes pruebas para comprobar que las herramientas instaladas funcionaran correctamente.

Entre las verificaciones realizadas se encuentran:

- Comprobación de la versión de Python.
- Inicio de Visual Studio Code.
- Verificación del intérprete de Python en Visual Studio Code.
- Activación y funcionamiento del entorno virtual.
- Ejecución del programa `hola_mundo.py`.
- Comprobación de la versión de Git.
- Comprobación de la identidad configurada en Git.
- Creación y disponibilidad del repositorio en GitHub.
- Verificación de Postman.
- Verificación de OpenConnect.
- Comprobación de la instalación de Docker.
- Configuración de WSL 2.
- Inicio de GNS3.
- Inicio de la GNS3 VM.
- Funcionamiento de VMware Workstation.
- Importación de la GNS3 VM en VMware Workstation.
- Integración de GNS3 GUI con la GNS3 VM.

Las evidencias de estas comprobaciones se encuentran en:

`docs/practica-01/evidencias/`

---

## 6. Estructura del proyecto

El proyecto se organizó de la siguiente manera:

```text
automatizacion-redes/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── hola_mundo.py
│
├── tests/
│
├── data/
│
└── docs/
    └── practica-01/
        └── evidencias/
            ├── 01-python.png
            ├── 02-vscode.png
            ├── 03-python-vscode.png
            ├── 04-entorno-virtual.png
            ├── 05-hola-mundo.png
            ├── 06-git.png
            ├── 07-git-identidad.png
            ├── 08-github.png
            ├── 09-postman.png
            ├── 10-openconnect.png
            ├── 11-docker.png
            ├── 12-gns3.png
            ├── 13-gns3-vm.png
            ├── 14-vmware.png
            ├── 15-importacion-gns3-vm.png
            └── 16-integracion-gns3.png
```

## 7. Problemas encontrados y soluciones

Durante la instalación y configuración de la estación de automatización se presentaron los siguientes problemas:

- **Docker Desktop no podía iniciar:** Aunque `docker --version` reconocía correctamente Docker, al ejecutar `docker run hello-world` se presentó un error indicando que no era posible conectarse al motor de Docker. Docker Desktop mostraba el mensaje **"Virtualization support not detected"**.

  **Solución:** Se verificó que la virtualización del procesador estuviera habilitada desde el Administrador de tareas. Posteriormente se identificó un problema con WSL, por lo que se habilitaron los componentes **Windows Subsystem for Linux** y **Virtual Machine Platform** mediante PowerShell. Después de reiniciar el equipo, se instaló Ubuntu mediante WSL 2 y se inició nuevamente Docker Desktop. Finalmente, se ejecutó `docker run hello-world` y se comprobó que Docker podía ejecutar correctamente un contenedor.

- **GNS3 VM no podía iniciar en VMware:** Se presentó un error relacionado con la virtualización anidada y VT-x/EPT.

  **Solución:** Se revisó la configuración de virtualización del equipo y de VMware Workstation. También se verificó que la virtualización estuviera habilitada en el firmware del equipo.

- **Error de contadores de rendimiento virtualizados (VPMC):** VMware mostró un error relacionado con los contadores de rendimiento virtualizados.

  **Solución:** Se deshabilitó la opción **Virtualize CPU performance counters** en la configuración de la máquina virtual de GNS3.

- **Seguridad basada en virtualización (VBS):** Windows tenía habilitada la seguridad basada en virtualización, lo que impedía que VMware utilizara correctamente la virtualización.

  **Solución:** Se deshabilitó la seguridad basada en virtualización y se reinició el equipo. Posteriormente, se verificó que VBS apareciera como **No habilitado**.

- **`vmrun.exe` era bloqueado por Windows Defender:** GNS3 no podía comunicarse correctamente con VMware porque Windows Defender bloqueaba `vmrun.exe`.

  **Solución:** Se permitió `vmrun.exe` mediante la opción de aplicaciones permitidas en el acceso controlado a carpetas de Windows Defender.

- **Integración de GNS3 con VMware:** Después de solucionar los problemas anteriores, se verificó que la GNS3 VM pudiera iniciarse correctamente y que GNS3 reconociera tanto la GNS3 VM como el servidor local.

## 8. Conclusiones

La práctica nos permitió preparar y configurar una estación de trabajo para realizar actividades de automatización de redes. Se instalaron y verificaron herramientas como Python, Visual Studio Code, Git, GitHub, Postman, OpenConnect, Docker y GNS3.

Durante el proceso se presentaron problemas relacionados principalmente con Docker, la virtualización de Windows y la integración entre GNS3 y VMware. La solución de estos problemas permitió comprender mejor la relación entre las diferentes herramientas y los requisitos de virtualización necesarios para su funcionamiento.

Finalmente, se logró configurar correctamente el entorno de trabajo y comprobar la integración de GNS3 con la GNS3 VM mediante VMware Workstation, dejando la estación preparada para futuras prácticas de automatización de infraestructura digital.