# DBD-Grupo-3
# "Implementación de un software ..."

## 1. Descripción de la Empresa, del Proceso de Negocio Elegido y Motivación
### 1.1 Descripción de la empresa
**1.1.1 Datos generales:**

**- Nombre de la empresa:** Centro de Estudiantes de Ingeniería Industrial y de Sistemas (CEIIS).

**-Tipo empresa:** Organización sin fines de lucro.

**-Función:** El CEIIS es el máximo órgano representativo de todos los estudiantes de la Facultad de Ingeniería Industrial, Sistemas y Software.

**Pagina de facebook:** [Facebook CEIIS](https://www.facebook.com/ceiis.oficial)
### 1.2 Procesos internos de la empresa
1.2.1 Proceso de alquiler
1.2.2 Proceso de préstamo
1.2.3 Proceso de reserva de lozas
    
   

### 1.3 Diagrama de Procesos

![Alt texasdt](alquiler.jpeg)
![Alt texasdt](prestamo.jpeg)
### 1.4 Descripcion del tema

Nuestro proyecto para este curso se enfoca en el desarrollo de un software para el Centro de estudiantes de la FIIS que permita optimizar y automatizar los procesos de préstamos, alquileres de objetos o juegos de mesa y reservas de las lozas deportivas de nuestra facultad. Este sistema proporcionará una plataforma eficiente para que los estudiantes de la facultad podamos acceder a estos recrsos de manera sencilla, mejoran la disponibilidad y facilitando la coordinación de actividades dentro de la comunidad FIIS.

### 1.5 Motivación del trabajo

La motivación para realizar este trabajo se basa en el deseo de desarrollar un software que mejora la experiencia de los estudiantes de la facultad, a la misma vez de ayudar al CEIIS a automatizar y optimizar sus procesos, para un mejor aprovechamiento de los recursos que ofrece y beneficiar directamente a los estudiantes al hacer que estos recursos y servicios sean más accesibles y eficientes,

**- Objetivo:** Mejorar la experiencia de los estudiantes de la FIIS, a la vez de optimizar la gestion de los recursos del CEIIS y asi mismo aumentar la eficiencia del personal aministrativo del centro de estudiantes de la FIIS.


## 2. Requerimientos

### 2.1 Requerimientos funcionales
**Caso de uso N°1: Registro de usuario**
- El usuario puede registrarse proporcionando informacion personal, como nombre, correo institucional, código universitario, contraseña, y datos de contacto.
- El sistema debe verificar en la base de datos la validez de la información registrada por el usuario.
- El sistema debe enviar un correo de confirmación despues del registro.

  
| Objetivo | <p align="left">Permitir que los usuarios se registren proporcionando información personal y validar su registro.</p> | 
|:--------------:|--------------|
| Descripción | Proceso de registro de usuarios en la aplicación, incluyendo la verificación de la información proporcionada y el envío de un correo de confirmación.  | 
| Actor primario   | Alumno FIIS  | 
|Actor secundario| - |
|Precondiciones | - |
| Paso | <p align="center"> Acción </p> |
| 1 | El usuario accede a la página de registro de la aplicación |
| 2	| El usuario proporciona información personal, incluyendo nombre, correo institucional, código universitario, contraseña y datos de contacto. |
| 3	| El sistema verifica la validez de la información proporcionada, incluyendo la comprobación del formato del correo electrónico y la fortaleza de la contraseña. |
| 4	| El sistema registra al usuario en la base de datos. |
| 5	| El sistema genera un correo electrónico de confirmación y lo envía a la dirección proporcionada por el usuario. |
| 6 | El usuario recibe el correo de confirmación y sigue las instrucciones para activar su cuenta. |
| 7 | El usuario hace clic en el enlace de confirmación en el correo electrónico. |
| 8 | El sistema verifica el enlace y, si es válido, activa la cuenta del usuario. |
| 9 | El usuario recibe una notificación de éxito y puede comenzar a utilizar la aplicación con su cuenta activa. |
| 10 | El caso termina |
  
**Caso de uso N°2: Login de usuario**
- El usuario registrado podrá iniciar secion con su correo institucional y contraseña.
- El sistema debe tener una opción para recuperar contraseña en caso de olvido
- El sistema debe autentificar las credenciales y redirigir al usuario a su perfil.
- Dependiendo del rol de usuario (administrador, alumno) , podrá acceder a las pestañas establecidas por funcionalidad para cada usuario


| Objetivo | <p align="left">Permitir que los usuarios registrados inicien sesión en la aplicación y accedan a sus perfiles. </p> | 
|:--------------:|--------------|
| Descripción | Proceso de registro de usuarios en la aplicación, incluyendo la verificación de la información proporcionada y el envío de un correo de confirmación.  | 
| Actor primario   | Alumno FIIS o Administrador | 
|Actor secundario| - |
|Precondiciones | El usuario debe estar registrado en la aplicación. |
| Paso | <p align="center"> Acción </p> |
| 1 | El usuario accede a la página de inicio de sesión de la aplicación. |
| 2	| El usuario proporciona su correo institucional y contraseña en los campos de usuario correspondientes. |
| 3	| El sistema verifica las credenciales del usuario para asegurarse de que sean válidas y coincidan en la base de datos. |
| 4	| El sistema redirige al usuario a su perfil con las funcionalidades correspondientes a su rol. |
| 5	| Si las credenciales son incorrectas, el sistema ofrece la opción de "Recuperar Contraseña".|
| 6 | El usuario puede hacer clic en "Recuperar Contraseña" para iniciar el proceso de recuperación. |
| 7 | El sistema envía un correo electrónico al usuario con instrucciones para restablecer su contraseña. |
| 8 | El usuario sigue las instrucciones del correo electrónico y crea una nueva contraseña. |
| 9 | Una vez que la contraseña se ha restablecido con éxito, el usuario puede volver a intentar iniciar sesión. |
| 10 | El caso termina |

**Caso de uso N°3: Visualizador de noticias**
- La pagina mostrará noticias relevantes, como eventos deportivos organizados por el CEIIS, ecentos culturales y actividades del CEIIS. 
- El sistema debe hacer posible filtrar por fecha, categoria o palabra clave.
- Los administradores deben tener la capacidad de agregar, editar y eliminar noticias.

  
| Objetivo    | Mostrar al estudiante las noticias más recientes que suceden en la FIIS |
| ------------- | ------------- |
| Descripción  | Visualización actualizada de las últimas noticias que hay en la FIIS  |
| Actor primario  | Alumno FIIS  |
| Actores secundarios  | -  |
| Precondiciones  | Content Cell  |
| Paso  | Acción |
| 1  | El usuario accede a la página de inicio de sesión de la aplicación.  |
| 2  | El alumno ingresa su correo y su contraseña  |
| 3  | El sistema verifica las credenciales del usuario para asegurarse de que sean válidas y coincidan en la base de datos.  |
| 4  | El alumno hace clic sobre Ver noticias  |
| 5  | El sistema muestra las noticias más recientes  |
| 6  | El caso termina  |

**Caso de uso N°4: Reserva de lozas deportivas** 
- El sistema debe permitir que los usuarios registrados puedan ver la disponibilidad de las lozas deportivas en tiempo real. 
- El usuario debe poder seleccionar la fecha y hora deseada para la reserva.
- El sistema debe mostrar la disponibilidad de lozas y perimtir a los usuarios reservas una loza especifica.
- El usuario debe notificar al usuario la confirmacióon de reserva.
- El sistema debe mostrar una opción para cancelar reservas.

| Objetivo | <p align="left">Realizar la reserva de una loza deportiva</p> | 
|:--------------:|--------------|
| Descripción | Proceso para reservar una loza deportiva que este diponible en la FIIS  | 
| Actor primario   | Alumno FIIS | 
|Actor secundario| - |
|Precondiciones | El usuario debe estar registrado en la aplicación y la loza debe de estar desocupada |
| Paso | <p align="center"> Acción </p> |
| 1 | El alumno accede a la página de inicio de sesión de la aplicación. |
| 2	| El alumno ingresa su correo y su contraseña |
| 3	| El sistema verifica las credenciales del usuario para asegurarse de que sean válidas y coincidan en la base de datos. |
| 4 | El alumno ingresa a la opcion de servicios|
| 5 | El sistema muestra la pantalla de servicios |
| 6 | Una vez que la contraseña se ha restablecido con éxito, el usuario puede volver a intentar iniciar sesión |
| 7 | El caso termina |

**Caso de uso N°5: Prestamos de objetos y materiales**
- El usuario registrado debe poder ver un catalogo de objetos diisponibles para prestamo.
- El sistema debe permitir al usuario solicitar prestamos de objetos seleccionando el articulo desea y proporcionando detalles del prestamo, como la duracion del prestamo.
- El sistema debe mostrar una confirmación del prestamo.
- El sistema debe mostrar cuando un objeto no está disponible por falta de stock.
- Debe existir un registro de prestamos y devoluciones.

| Objetivo | <p align="left">Permitir que los usuarios registrados puedan solicitar y realizar préstamos de objetos y materiales disponibles en el CEIIS</p> | 
|:--------------:|--------------|
| Descripción |  Proceso de préstamo de objetos y materiales, incluyendo la visualización del catálogo, la solicitud de préstamo, la confirmación del préstamo, la gestión de objetos no disponibles y el registro de préstamos y devoluciones. | 
| Actor primario   | Alumno FIIS | 
|Actor secundario| - |
|Precondiciones | El usuario debe haber iniciado sesión en la aplicación. |
| Paso | <p align="center"> Acción </p> |
| 1 | El usuario acceda a la sección de prestamos en la aplicación |
| 2	| El sistema muestra una lista de objetos y materiales disponibles para préstamo  |
| 3	| El usuario selecciona el objeto que desea solicitar para préstamo |
| 4 | El sistema muestra las opciones de confirmar o cancelar el prestamo  |
| 5 | El usuario confirma la solicitud de préstamo |
| 6 |  El sistema registra la solicitud y muestra una confirmación de préstamo |
| 7 | El caso termina |

**Caso de uso N°6: Observar disponibilidad en tiempo real**

**Caso de uso N°7: Visualizador de historial**
- El usuario registrado debe poder acceder a un historial de sus actividades, incluyendo prestamos pasados, reservas anteriores y noticias visualziadas.

| Objetivo | <p align="left"> Permitir que los usuarios registrados accedan a un historial de sus actividades en la aplicación, incluyendo préstamos pasados, reservas anteriores y compras realizadas </p> | 
|:--------------:|--------------|
| Descripción |  Visualización del historial del usuario | 
| Actor primario   | Alumno FIIS | 
|Actor secundario| - |
|Precondiciones | El usuario debe haber iniciado sesión en la aplicación |
| Paso | <p align="center"> Acción </p> |
| 1 | El usuario accede a su perfil |
| 2 | El usuario accede a la sección de historial de actividades |
| 3 | El sistema permite al usuario filtrar por fechas el historial de sus actividades |
| 4	| El sistema muestra una lista de actividades pasadas, incluyendo préstamos, reservas y compras especificando el tipo de servicio, la fecha , el costo y el estado actual |
| 5	| El caso termina  |

**Caso de uso N°8: Visualizar paginas "Acerca de nosotros"**
- La pagina debe tener una seccion "Acerca de Nosotros" que proprocione información sobre el CEIIS, la junta directiva y la misión del CEIIS.

| Objetivo | <p align="left"> Permitir que los usuarios accedan y visualicen la página "Acerca de Nosotros", la cual proporciona información sobre el CEIIS, su junta directiva y su misión </p> | 
|:--------------:|--------------|
| Descripción |  Visualización de informacion relevante del CEIIS | 
| Actor primario   | Alumno FIIS | 
|Actor secundario| - |
|Precondiciones | - |
| Paso | <p align="center"> Acción </p> |
| 1 | El usuario inicia sesión en la aplicación o accede a la aplicación como visitante |
| 2 | El usuario navega a la sección de la página principal del sitio web |
| 3 | El usuario busca y selecciona la opción "Acerca de Nosotros" en el menú de navegación o en la página principal |
| 4	| El sistema carga la página "Acerca de Nosotros" y muestra la información relacionada con el CEIIS |
| 5	| El usuario tiene la opción de regresar a la página principal de la aplicación o continuar explorando otros contenidos |
| 6 | El caso termina |


**Caso de uso N°9: Visualizar reputacion de usuario**

**Caso de uso N°10: Encuestas a usuarios**
- Los administradores deben tener la capacidad de crear encuenstas dirigidas a los ususarios.
- El usuario debe poder responder a encuestas y proporcionar retroalimentacion sobre la calidad de los servicias y expreciencia del usuario.
- Debe haber un sistema de analisis para resumir los resultados de las encuestas.

**Caso de uso N°11: Visualizar estadisticas**

  
**Caso de uso N°12: Control de horario de lozas deportivas**

**Caso de uso N°13: Actualización de noticias**
### 2.2 Requerimientos de atributos
- Seguridad
- Usabilidad
- Rendimiento
- Automatizacion de procesos
- Accesibilidad
- Retroalimentación y Sugerencias de Usuarios

## 3. Modulos
**- Seguridad**
  - Responsabilidades: Gestionar todo inicio de sesión, registro y recuperación de contraseñas de la pagina asi mismo de la seguridad de la integración de las cuentas, y el acceso a los campos respectivo de cada usuario y contraseña.
    
    **A. Registro**
    
    **Responsabilidades:** Permite que los usuarios de la facultad creen una cuenta personal en el sistema. Su función principal es recopilar la información necesaria para crear una cuenta de usuario, como los nombres, apellidos, codigo UNI, correo institucional, contraseña.   
    **Interacción:** Con el módulo prestamos o alquiler, encuestas.
    
    **B. Login**
    
    **Responsabilidades:** Permite que los usuarios ingresen a su cuenta personal proporcionando sus credenciales de autenticación, en este caso su correo institucional y su contraseña.
    
    **Interaccion:** Con el módulo de prestamos o alquiler, encuestas.
    
    **C. Recuperar cuenta**
    
    **Responsabilidades:** Proporciona a los usuarios una forma de restablecer el acceso a su cuenta personal en caso de que hayan olvidado su contraseña o enfrenten problemas para iniciar sesión.
    
    **Interaccion:** Con el modulo de prestamos o alquiler.
    
    **D. Reestablecer contraseña**
    
    **Responsabilidades:** Permite a los usuarios cambiar su contraseña actual por una nueva en caso de olvido.
    
    **Interaccion:** Con el módulo de prestamos o alquiler.
    
    **E. Perfil del usuario**

    **Responsabilidades:** Permite a los usuarios gestionar y actualizar la información relacionada con su perfil personal en la plataforma.
    **Interaccion:** Con el módulo de prestamos o alquiler.
    
    **F. Cambiar contraseña**

    **Responsabilidades:** Permite a los usuarios cambiar su contraseña actual por una nueva.
    
    **Interaccion:**  Con el módulo de prestamos o alquiler.
    
    **G. Historial del usuario**

    **Responsabilidades:** Muestra a los usuarios un registro detallado de los prestamos, alquileres o reservas que han realizado dentro de la plataforma a lo largo del tiempo. Esta funcionalidad proporciona a los usuarios un resumen histórico de su actividad y les permite realizar un seguimiento de sus interacciones pasadas. 
    **Interaccion:** Con el módulo de prestamos o alquiler.

    **H. Perfil del administrador**
    
**-   Encuestas**

- Responsabilidades: Gestionar las preguntas que se pondran para hacer un cuestionario a los alumnos, para reacuadar información a travez de preguntas concisas, en base a alternativa  y a partir de la información recolectada poder hacer cuadros estadisticos, mostrando las tendencias de respuesta.
    
**A. Administrador encuesta**  
    
**Responsabilidades:** Permite gestionar y administrar todas las encuestas en la plataforma. Crear editar y elimnar las encestas, además de asignar los permisos para que los usuarios puedan acceder a la encuesta. 

**Interaccion:** Con el módulo de seguridad.

**B. Administrador crear encuesta**

**Responsabilidades:** Permite al administrador definir los detalles de la encuesta, diseñar las preguntas, opciones de respuestas y lógica de encuesta. 

**Interaccion:** Con el módulo de seguridad.

**C. Administrador respuestas y estadisticas encuestas**

**Responsabilidades:** Permite acceder y analizar las respuestas de las encuestas y proporcionar información estadistica para la toma de decisiones.

**Interaccion:** Con el módulo de seguridad.

**D. Usuario encuesta**
    
**Responsabilidades:** Permite al usuario participar en las encuestas creadas por los aministradores.

**Interaccion:** Con el módulo de seguridad.
    
**-  Estadisticas:**

- Responsabilidades: A partir de todos los movimientos registrados, como alquileres y prestamos de objetos se puede elaborar, se pueda lograr una visualización de la cantidad de prestamos y alquieleres que se hicieron por día y por hora.
    
**-  Finanzas**
    - Responsabilidades: Registrar y gestionar por parte de los administradores los datos de manera eficiente. Seguimiento del presupuesto asignado y disponible, actualizar de manera automatica el dinero. Generación de informes para auditorias.
    
**-  Prestamo o Alquiler:**

- Responsabilidades: Gestión de inventario, para mantener un registro de cada articulo. Podeer valdiar la disponibilidad de los objetos solicitados asi mismo registrar la fecha de inicio y de la devolución esperada. Permitir a los usuarios poder reservar las lozas deportivas, y que el administrador pueda gestioanr la disponibilidad de estas.
    
**-  Logistica:**

- Responsabilidades: Gestionar y mantener actualizados el inventario de recursos y suministros disponibles. Validar la disponibilidad de los recursos solicitados. Se mantendria un registro detallado de las transacciones de los recursos.



## [Figma](https://www.figma.com/file/600QmGXcDGzgKVtZu9jm7g/DBD-GRUPO3?type=design&node-id=38-6&mode=design&t=0TAzfWjCKlUIWavj-0)

### Requerimientos Funcionales Usuario
- Registro de Usuario
- Login de Usuario
- Visualizador de Noticias
- Reserva de lozas deportivas
- Prestamos de Obejtos y materiales
- Observar disponibilidad en tiempo real
- Visualizador de historial.
- Visualizar paginas "contactanos" y "quienes somos"
- Visualizar reputación

### Requeriminentos Administrador
- Logid de Administrador
- Actualizar sección de noticias y eventos
- Manejar la disponibilidad de reservas
- Gestionar de obejetos y materiales
- Gestionar las finanzas obtenidas por el alquiler
- Visualizar el historial de usuarios
- Visualizar la reputación de cada usuario
- Estadisticas de prestamos y horario
- Gestión de turnos en la oficina

### Modulos por funcionalidad


### Vistas usuario
- Login-
- Registro-
- Recuperación de contraseña-
- Acutalización de datos
- Home-
- Quienes somos?(acerca de)
- Servicios(se visualiza prestamos y alquiler)
- Contactanos(se visualiza correo y celular de contacto)
- Prestamos (se visualizan los objetos, stock, costo)
- Alquiler (se visualizan las lozas, disponibilidad de horarios, costo)
- Historial de Usuario(sus prestamos)
- Reputación
### Vistas admin
- Login-
- Registro-
- Recuperación de contraseña-
- Acutalización de datos
- Home
- Quienes somos?(acerca de)
- Servicios(se visualiza prestamos y alquiler)
- Contactanos
- Prestamos (Usuario) (Administrador)
- Alquiler 
- Historial de Usuario
- Reputación
- Estadisticas

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
