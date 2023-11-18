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

## N
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](Preguntas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar pagina: Se llenará la fecha de las encuestas a mostrar**  |
| **SELECT Id_encuesta FROM Encuesta E WHERE E.Fecha_apertura = '<1>'**;|
| **2. Cargar pagina: Muestra las encuestas activas**  |
|	**SELECT Id_encuesta FROM Encuesta E WHERE E.Estado_encuesta = 'activo'; <2>  **|

## n
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](reservasyalquileres.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los reservas y alquileres   |
|**SELECT Nombre_articulo, Precio_unitario FROM Articulo WHERE Tipo_articulo = 'reservas y alquileres';** |

## n1
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](productos_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los productos para venta  |
|**SELECT Nombre_articulo, Precio_unitario FROM Articulo WHERE Tipo_articulo = 'reservas y alquileres';** |

## n2
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](productos_prestamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los productos para prestamo   |
|**SELECT Nombre_articulo FROM Articulo WHERE Tipo_articulo = 'prestamo';**|
