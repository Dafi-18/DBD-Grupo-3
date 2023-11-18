# CREACION DE TABLAS


# Sentencias SQL por cada prototipo
## 1
| Código requerimiento | R-001 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Registro.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Registrar:** Se agregará un nuevo registro a la tabla persona y tabla usuario |
|**INSERT INTO Persona (Dni,primer_nombre, primer_apellido, segundo_apellido, Celular) VALUES (<2>, <3>, <4>, <5>);**|
|**INSERT INTO Usuario (Correo_uni, cod_uni, Contrasena, Dni) VALUES (<1>, <6>, <7> , (SELECT Dni FROM persona WHERE Dni = <2>);**|

## 2
| Código requerimiento | R-002 |
| --- | --- |
| Codigo interfaz |  I-002 |
| Imagen interfaz  |

![Alt texasdt](Loginpage.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Iniciar Sesión:** El usuario ingresa a su cuenta |
|**SELECT Id_usuario, Cod_uni FROM Usuario WHERE Correo_uni = <1> AND Contrasena = <2>;**|

## 3
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](Recuperarcuenta.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Restaurar contraseña:**  |
|**SELECT Id_usuario, Correo_uni FROM Usuario WHERE Correo_uni = <1>;**|

## 4
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](Recuperarcontraseña.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Restablecer tu contraseña:**  |
| |

## 5
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](PerfilUsuario.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar pagina:**  |
| |
