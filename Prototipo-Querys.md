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

| Código requerimiento | R-019-021 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Vista_de_inventario_de_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostrarán los artículos y las cantidades que se han vendido en dicho día |
|**SELECT SUM(dv.cantidad) FROM detalle_venta dv INNER JOIN venta v ON dv.id_venta = v.id_venta AND dv.id_articulo = <ID_ARTICULO> AND v.fecha_venta = <FECHA>;**|
| **2. Cargar página:** Se mostrarán todos los artículos, su precio unitario y el stock restante para la venta |
|**SELECT Id_articulo, nombre_articulo, precio_unitario, cantidad FROM Articulo WHERE tipo_articulo = 'venta';**|

| Código requerimiento | R-021 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Editar_artículo_del_inventario_de_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Check:** Se modifica el precio y/o stock de un artículo |
|**UPDATE Articulo SET cantidad = <CANTIDAD> , precio_unitario = <PRECIO> WHERE Id_articulo = <ID_ARTICULO>;**|

| Código requerimiento | R-020 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Agregar_artículo_al_inventario_de_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Check:** Se agrega un nuevo artículo al inventario de ventas |
|**INSERT INTO Articulo(Id_articulo, Nombre_articulo, Tipo_articulo, Cantidad, Descripcion, Precio_unitario, Disponibilidad) VALUES (<1>, <2>, <3>, <4>, <5>, <6>, <7>);**|

| Código requerimiento | R-019 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Quitar_artículo_del_inventario_de_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón de papelera:** Se elimina dicho artículo del inventario de ventas |
|**DELETE FROM Articulo WHERE Id_articulo = <ID_ARTICULO>;**|


| Código requerimiento | R-022-024 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Vista_de_inventario_de_préstamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostrarán los artículos y las cantidades que se han prestado en dicho día |
|**SELECT COUNT(*) FROM Prestamo WHERE Estado_prestamo = 'No devuelto' AND Fecha_prestamo = <FECHA_PRESTAMO>;**|
| **2. Cargar página:** Se mostrarán todos los artículos y el stock restante para el préstamo |
|**SELECT Id_articulo, nombre_articulo, cantidad FROM Articulo WHERE tipo_articulo = 'prestamo';**|

| Código requerimiento | R-024 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Editar_artículo_del_inventario_de_préstamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Check:** Se modificará la cantidad en stock de un artículo en el inventario de préstamos |
|**UPDATE Articulo SET cantidad = <CANTIDAD> WHERE Id_articulo = <ID_ARTICULO>;**|

| Código requerimiento | R-023 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Agregar_artículo_al_inventario_de_préstamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Check:** Se modificará la cantidad en stock de un artículo en el inventario de préstamos |
|**INSERT INTO Articulo(Id_articulo, Nombre_articulo, Tipo_articulo, Cantidad, Descripcion, Precio_unitario, Disponibilidad) VALUES (<1>, <2>, <3>, <4>, <5>, null, <7>);**|

| Código requerimiento | R-022 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Quitar_artículo_del_inventario_de_préstamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón de papelera:** Se elimina dicho artículo del inventario de préstamos |
|**DELETE FROM Articulo WHERE Id_articulo = <ID_ARTICULO>;**|

| Código requerimiento | R-018 |
| --- | --- |
| Codigo interfaz |  I-001 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Vista_de_alquiler_de_losas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostrarán los horarios de las losas durante la semana |
|**SELECT * FROM Calendario ORDER BY <FECHA>, <ID_HORA>;**|

| Código requerimiento | R-018 |
| --- | --- |
| Codigo interfaz |  I-002 |
| Imagen interfaz  |

![Alt texasdt](Vistas_del_inventario_de_ventas_y_préstamos_y_calendario_de_alquileres_y_reservas/Editar_disponibilidad_de_losas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Aceptar:** Cambiar la disponibilidad de cierto día y hora del horario de la semana (Pueden ser varios cambios en diferentes días en simultáneo)  |
|**UPDATE calendario SET estado = CASE WHEN estado = 'Ocupado' THEN 'Disponible' WHEN estado = 'Disponible' THEN 'Ocupado' END WHERE id_hora = <ID_HORA> AND Fecha = <FECHA>;**|
