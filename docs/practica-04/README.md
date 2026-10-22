# Práctica 4 - Exploración de comunidades, documentación y recursos de colaboración

## Propósito de la práctica

El propósito de esta práctica es aprender a localizar, analizar y utilizar recursos técnicos confiables que puedan ayudarnos a resolver dudas y problemas durante el desarrollo de programas y la automatización de redes. También permite conocer diferentes comunidades de colaboración en las que podemos consultar experiencias y soluciones de otros usuarios.

## Relación con el proyecto integrador

Esta práctica se relaciona con el proyecto integrador porque en las siguientes actividades continuaremos trabajando con Python, GNS3 y herramientas de automatización de redes. Tener identificadas fuentes de información confiables nos permitirá investigar errores, consultar documentación y encontrar posibles soluciones cuando se presente algún problema durante el desarrollo.

## Recursos consultados

Durante la práctica se consultaron diferentes recursos relacionados con Python, GNS3, Netmiko y comunidades de colaboración.

- **Documentación oficial de Python:** se utilizó para conocer la información y los recursos disponibles para aprender y consultar el funcionamiento del lenguaje.
- **Tutorial oficial de Python:** proporciona explicaciones y ejemplos que pueden servir de apoyo durante el desarrollo de programas.
- **Documentación de GNS3:** contiene información sobre instalación, configuración, topologías, dispositivos y solución de problemas.
- **Repositorio de Netmiko:** permite consultar el código, versiones, plataformas compatibles, ejemplos y cambios de la biblioteca.
- **Documentación de Netmiko:** sirve como referencia para conocer el funcionamiento de la biblioteca y su uso con dispositivos de red.
- **Stack Overflow en español:** comunidad de preguntas y respuestas que puede ayudar a investigar problemas de programación.
- **GitHub Discussions:** espacio que permite realizar preguntas, compartir información y participar en conversaciones relacionadas con proyectos.
- **Comunidad de GNS3:** permite consultar discusiones y problemas relacionados con GNS3 y la simulación de redes.

## Evaluación de confiabilidad

| Criterio | Documentación de Python | Documentación de GNS3 | Repositorio de Netmiko |
|---|---|---|---|
| ¿Quién publica o mantiene el recurso? | Python Software Foundation y colaboradores de Python. | Proyecto y equipo de GNS3. | Desarrolladores y colaboradores de Netmiko. |
| ¿La información corresponde al tema investigado? | Sí, contiene información sobre Python y su funcionamiento. | Sí, está enfocada en GNS3, redes y simulación. | Sí, contiene información relacionada con Netmiko y automatización de redes. |
| ¿Incluye ejemplos o instrucciones verificables? | Sí, contiene tutoriales, referencias y ejemplos. | Sí, contiene guías e instrucciones para utilizar GNS3. | Sí, incluye documentación, código y ejemplos. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Sí, la documentación indica la versión de Python. | Sí, el contenido y las versiones de GNS3 pueden identificarse en sus recursos. | Sí, GitHub permite observar versiones, cambios y actualizaciones del proyecto. |
| ¿Es posible comprobar la información con otra fuente? | Sí, puede compararse con tutoriales y otros recursos sobre Python. | Sí, puede compararse con la comunidad y otros recursos de GNS3. | Sí, puede compararse con la documentación de Netmiko y su código. |
| ¿Qué utilidad tiene para el proyecto integrador? | Resolver dudas relacionadas con los programas desarrollados en Python. | Apoyar la configuración y solución de problemas en las topologías de red. | Servir de referencia para futuras tareas de automatización y conexión con dispositivos. |

### Análisis de los recursos

**¿Cuál de los recursos consideras más útil para resolver dudas de Python? ¿Por qué?**

La documentación oficial de Python, porque contiene información directamente relacionada con el lenguaje, además de tutoriales, referencias y ejemplos que podemos consultar cuando tengamos dudas sobre el código.

**¿Cuál consultarías para resolver un problema relacionado con GNS3?**

Consultaría primero la documentación de GNS3 porque contiene información específica sobre el funcionamiento de la herramienta, configuración de topologías, dispositivos y solución de problemas.

**¿Por qué no conviene copiar directamente una solución sin comprobar que funciona en el entorno de trabajo?**

Porque una solución puede haber sido creada para otra versión, configuración o entorno diferente. Es importante entenderla y probarla antes de utilizarla para comprobar que realmente soluciona el problema sin generar nuevos errores.

## Estrategia para resolver un problema técnico

Se planteó la siguiente situación: el programa `dispositivos.py` muestra correctamente la información de R1 y R2, pero al buscar un dispositivo por su nombre no encuentra el equipo solicitado.

| Elemento | Respuesta del equipo |
|---|---|
| **Problema identificado** | El programa no encuentra un dispositivo cuando se busca por su nombre, aunque la información de R1 y R2 sí se muestra correctamente. |
| **Palabras clave para realizar la búsqueda** | Python buscar elemento por nombre, buscar en lista Python, comparar strings Python, buscar dispositivo en diccionario Python. |
| **Documentación o comunidad que consultaríamos primero** | Primero consultaríamos la documentación oficial de Python y, si seguimos teniendo dudas, buscaríamos algún problema parecido en Stack Overflow. |
| **Información que revisaríamos en el código** | Revisaríamos cómo están guardados los nombres de R1 y R2 y cómo se está comparando el nombre que escribe el usuario con los dispositivos registrados. |
| **Tipo de ejemplo o solución que buscaríamos** | Buscaríamos ejemplos sencillos de cómo recorrer una lista o diccionario y comparar un dato ingresado por el usuario con los datos almacenados. |
| **Cómo comprobaríamos que la solución funciona** | Ejecutaríamos nuevamente el programa y haríamos búsquedas con R1 y R2 para comprobar que ambos sean encontrados correctamente. También probaríamos con un nombre que no exista para revisar cómo responde el programa. |
| **Cómo documentaríamos la solución encontrada** | Anotaríamos el problema, la causa y la solución aplicada en el README del repositorio para poder consultarla nuevamente si aparece un error parecido. |

## Aprendizajes obtenidos

Con esta práctica aprendimos que no solo es importante saber programar, sino también saber dónde buscar cuando tenemos alguna duda o problema. Conocimos mejor la documentación oficial de Python y GNS3, además de recursos como Netmiko, GitHub y Stack Overflow. También aprendimos que antes de utilizar una solución encontrada en Internet debemos revisar si es confiable y si realmente funciona en nuestro entorno. Estos recursos nos pueden servir bastante en las siguientes prácticas cuando comencemos a trabajar con más programas y herramientas de automatización.

## Conclusiones individuales

### Angel Guadalupe Flores Cuellar

En esta práctica aprendí que existen diferentes recursos que nos pueden ayudar cuando tenemos algún problema con programación o redes. La documentación oficial es útil porque contiene información directamente relacionada con la herramienta que estamos utilizando, mientras que las comunidades nos permiten conocer soluciones y experiencias de otras personas. Para saber si una fuente es confiable revisaría quién la publica, si está actualizada y si la información realmente corresponde con nuestro problema. En caso de tener algún error en Python, podemos consultar primero la documentación y después buscar casos parecidos en comunidades como Stack Overflow. También aprendí que no debemos copiar cualquier solución sin antes entenderla y comprobar que funcione correctamente. Guardar las soluciones en GitHub nos ayuda a mantener un registro de los problemas que hemos encontrado. De esta manera, todo el equipo puede consultar esa información cuando sea necesario. Creo que estos recursos nos van a servir bastante en las siguientes prácticas de automatización de redes.

### Coral Guadalupe García Camacho

En esta práctica aprendí que la documentación oficial es una de las mejores opciones para empezar a buscar cuando tengo alguna duda, ya que la información viene directamente de los responsables de la herramienta o lenguaje. Las comunidades también son útiles porque podemos encontrar problemas que otras personas ya tuvieron y ver cómo los resolvieron. Considero que para saber si un recurso es confiable hay que revisar quién lo publica, si está actualizado y si la información se puede comprobar. En el caso de Python, una comunidad como Stack Overflow puede ayudar cuando aparece algún error que no sabemos cómo solucionar. También entendí que no es buena idea copiar una solución sin probarla primero, porque puede que no funcione igual en nuestro entorno. Documentar lo que encontramos en GitHub nos ayuda a tener la información organizada y poder volver a consultarla después. Creo que esto será útil en las siguientes prácticas, ya que seguramente tendremos nuevos errores o dudas al trabajar con automatización. Ahora ya conocemos varios lugares donde podemos buscar información antes de quedarnos atorados con algún problema.

### Yatana Alexandra Nieto

Esta práctica me ayudó a conocer diferentes recursos que podemos utilizar cuando tengamos problemas durante el desarrollo del proyecto. La documentación oficial me parece importante porque contiene información más directa sobre cómo funciona una herramienta, mientras que las comunidades muestran experiencias y soluciones de otros usuarios. Para saber si una fuente es confiable revisaría quién la mantiene, cuándo fue actualizada y si la información coincide con otras fuentes. Las comunidades pueden ser de mucha ayuda cuando tenemos un error de Python y queremos saber si alguien más pasó por algo parecido. Aun así, considero importante entender las soluciones antes de utilizarlas y no solamente copiarlas. También es útil guardar en GitHub las soluciones que vayamos encontrando para que todo el equipo pueda consultarlas. Esto puede evitar que tengamos que investigar lo mismo varias veces. En las siguientes prácticas podremos apoyarnos en estos recursos para avanzar de una manera más organizada.

### Paola Berenice Vega Montemayor

Durante esta práctica aprendí que existen diferentes formas de buscar ayuda cuando se presenta un problema en programación o redes. La documentación oficial sirve para consultar información directamente relacionada con una herramienta, mientras que en una comunidad podemos encontrar preguntas y experiencias de otras personas. Pienso que una fuente es más confiable cuando sabemos quién la publica, está relacionada con el tema y presenta información que podemos comprobar. Si tuviéramos un problema con Python, primero podríamos revisar la documentación y después buscar casos similares en alguna comunidad. También aprendí que debemos probar cualquier solución antes de agregarla al proyecto, ya que puede estar hecha para una versión diferente. Guardar las soluciones en GitHub permite mantener un registro de los problemas que ya resolvimos. Esto también puede ayudar a los demás integrantes del equipo si llegan a tener el mismo error. Los recursos que conocimos en esta práctica serán útiles cuando avancemos con la automatización de nuestra red.