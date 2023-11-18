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
|**INSERT INTO Persona (DNI,primer_nombre, primer_apellido, segundo_apellido, Num_celular) VALUES (<2>, <3>, <4>, <5>);**|
|**INSERT INTO Usuario (correo_institucional, cod_uni, contraseña_usuario, DNI) VALUES (<1>, <6>, <7> , (SELECT DNI FROM persona WHERE DNI = <2>);**|

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
|**SELECT id_usuario, correo_institucional FROM usuario WHERE correo_institucional = <1> AND contraseña_usuario = <2>;**|
