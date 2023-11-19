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
| Código requerimiento | R-003 |
| --- | --- |
| Codigo interfaz |  I-003 |
| Imagen interfaz  |

![Alt texasdt](Recuperarcuenta.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Restaurar contraseña:**  |
|**SELECT Id_usuario, Correo_uni FROM Usuario WHERE Correo_uni = <1>;**|

## 4
| Código requerimiento | R-004 |
| --- | --- |
| Codigo interfaz |  I-004 |
| Imagen interfaz  |

![Alt texasdt](Recuperarcontraseña.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Restablecer tu contraseña:** Se realiza una actualizacion en la columna "Contrasena" de la tabla usuario. |
	UPDATE Usuario
	SET Contraseña = <1>
	WHERE id_usuario = 'identificador_del_usuario';


## 5
| Código requerimiento | R-005 |
| --- | --- |
| Codigo interfaz |  I-005 |
| Imagen interfaz  |

![Alt texasdt](PerfilUsuario.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar pagina:** Se muestra un reporte de las tablas alquiler, ventas y prestamos en el perfil personal del usuario. Se muestra un conteo de los servicios realizados por el usuario y un conteo total de los servicio utilizados. Se extrae información de la tabla usuario y persona para que aparezca en el perfil de usuario. |

	SELECT  
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    A.Fecha_alquiler AS Fecha_operacion,
	    A.Hora_inicio,
	    A.Hora_fin,
		NULL AS Fecha_devolucion,
		A.Monto,
	    A.Estado_alquiler AS Estado_operacion
	FROM
	    Alquiler A
	INNER JOIN
		 Usuario U ON A.Id_usuario = U.Id_usuario
	INNER JOIN
	    Articulo Ar ON A.Id_articulo = Ar.Id_articulo
	WHERE
	    U.Id_usuario = '1'
	
	UNION
	
	SELECT
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    P.Fecha_prestamo AS Fecha_operacion,
	    P.Hora_prestamo AS Hora_inicio, 
		P.Hora_devolucion  As Hora_fin,
	    P.Fecha_devolucion, 
		NULL AS Monto,
	    P.Estado_prestamo AS Estado_operacion
	FROM
	    Prestamo P
	INNER JOIN
	    Usuario U ON P.Id_usuario = U.Id_usuario
	INNER JOIN
	    Articulo Ar ON P.Id_articulo = Ar.Id_articulo
	WHERE
	    U.Id_usuario = '1'
		
	UNION
	
	SELECT
	    A.Nombre_articulo AS Nombre_producto,
	    A.Tipo_articulo AS Tipo_servicio,
	    V.Fecha_venta AS Fecha_operacion,
		NULL AS Hora_inicio,
		NULL AS Hora_fin,
		NULL AS Fecha_devolucion,
	    A.Precio_unitario AS Monto,
	    V.Estado_pago AS Estado_operacion
	FROM
	    Detalle_venta DV
	INNER JOIN
	    Venta V ON DV.Id_venta = V.Id_venta
	INNER JOIN
	    Articulo A ON DV.Id_articulo = A.Id_articulo
	INNER JOIN
	    Usuario U ON V.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';


|**CONTAR CANTIDAD DE PRESTAMOS DEL USUARIO**|

	SELECT
	    COUNT(P.Id_prestamo) AS Cantidad_prestamos
	FROM
	    Prestamo P
	INNER JOIN
	    Usuario U ON P.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';
	
|**CONTAR CANTIDAD DE VENTAS DEL USUARIO**|

	SELECT
	    COUNT(V.Id_venta) AS Cantidad_ventas
	FROM
	    Venta V
	INNER JOIN
	    Usuario U ON V.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';
	
|**CONTAR CANTIDAD DE ALQUILER DEL USUARIO**|

	SELECT
	    COUNT(A.Id_alquiler) AS Cantidad_ventas
	FROM
	    Alquiler A
	INNER JOIN
	    Usuario U ON A.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';	

|**TOTAL DE SERVICIOS UTILIZADOS POR EL USUARIO**|

	SELECT
	    U.Id_usuario,
	    U.DNI,
	    (
	        -- Subconsulta para contar registros de préstamos
	        COALESCE((SELECT COUNT(*) FROM Prestamo P WHERE P.Id_usuario = U.Id_usuario), 0) +
	        -- Subconsulta para contar registros de ventas
	        COALESCE((SELECT COUNT(*) FROM Venta V WHERE V.Id_usuario = U.Id_usuario), 0) +
	        -- Subconsulta para contar registros de alquileres
	        COALESCE((SELECT COUNT(*) FROM Alquiler A WHERE A.Id_usuario = U.Id_usuario), 0)
	    ) AS Total_registros
	FROM
	    Usuario U
	WHERE
	    U.Id_usuario = '1';	 

## 6
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](Historialdelusuario.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar pagina:** Se muestra un reporte de las tablas alquiler, ventas y prestamos en el perfil personal del usuario, y se realiza una busqueda por fecha. |

	SELECT  
	
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    A.Fecha_alquiler AS Fecha_operacion,
	    A.Hora_inicio,
	    A.Hora_fin,
		NULL AS Fecha_devolucion,
		A.Monto,
	    A.Estado_alquiler AS Estado_operacion
	FROM
	    Alquiler A
	INNER JOIN
		 Usuario U ON A.Id_usuario = U.Id_usuario
	INNER JOIN
	    Articulo Ar ON A.Id_articulo = Ar.Id_articulo
	WHERE
	    U.Id_usuario = '1'
		 AND A.Fecha_alquiler = '2023-11-13'
		
	UNION
	
	SELECT
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    P.Fecha_prestamo AS Fecha_operacion,
	    P.Hora_prestamo AS Hora_inicio, 
		P.Hora_devolucion  As Hora_fin,
	    P.Fecha_devolucion, 
		NULL AS Monto,
	    P.Estado_prestamo AS Estado_operacion
	FROM
	    Prestamo P
	INNER JOIN
	    Usuario U ON P.Id_usuario = U.Id_usuario
	INNER JOIN
	    Articulo Ar ON P.Id_articulo = Ar.Id_articulo
	WHERE
	    U.Id_usuario = '1'
		 AND P.Fecha_prestamo = '2023-11-13'
		
	UNION
	
	SELECT
	    A.Nombre_articulo AS Nombre_producto,
	    A.Tipo_articulo AS Tipo_servicio,
	    V.Fecha_venta AS Fecha_operacion,
		NULL AS Hora_inicio,
		NULL AS Hora_fin,
		NULL AS Fecha_devolucion,
	    A.Precio_unitario AS Monto,
	    V.Estado_pago AS Estado_operacion
	FROM
	    Detalle_venta DV
	INNER JOIN
	    Venta V ON DV.Id_venta = V.Id_venta
	INNER JOIN
	    Articulo A ON DV.Id_articulo = A.Id_articulo
	INNER JOIN
	    Usuario U ON V.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1'
		AND V.Fecha_venta = '2023-11-13';

## 7
| Código requerimiento | R-005 |
| --- | --- |
| Codigo interfaz |  I-005 |
| Imagen interfaz  |

![Alt texasdt](ConfiguraciondePerfilUsuario.png) 

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cambiar la contraseña:** Se realiza una actualización de la columna "Contraseña" de la tabla "Usuario". |

	UPDATE Usuario
	SET Contraseña = <1>
	WHERE IdUsuario = 'id_del_usuario' AND Contraseña = <2>;


## 8
| Código requerimiento | R-005 |
| --- | --- |
| Codigo interfaz |  I-005 |
| Imagen interfaz  |

![Alt texasdt](PerfilAdministrador.png) 

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar Pagina:** Se muestra un reporte de las tablas alquiler, ventas y prestamos generales en el perfil del administrador. Se muestra un conteo de cada 
tipo de servicios realizado por el Ceiis y un conteo total de los servicio prestados por mes. Se extrae información de la tabla usuario y persona para que aparezca en el perfil de usuario. |

	SELECT  
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    A.Fecha_alquiler AS Fecha_operacion,
	    A.Hora_inicio,
	    A.Hora_fin,
		NULL AS Fecha_devolucion,
		A.Monto,
	    A.Estado_alquiler AS Estado_operacion,
		A.Medio_pago
	FROM
	    Alquiler A
	INNER JOIN
	    Articulo Ar ON A.Id_articulo = Ar.Id_articulo
	
	UNION

	SELECT
	    Ar.Nombre_articulo AS Nombre_producto,
	    Ar.Tipo_articulo AS Tipo_servicio,
	    P.Fecha_prestamo AS Fecha_operacion,
	    P.Hora_prestamo AS Hora_inicio, 
		P.Hora_devolucion  As Hora_fin,
	    P.Fecha_devolucion, 
		NULL AS Monto,
	    P.Estado_prestamo AS Estado_operacion,
		NULL AS Medio_pago
	FROM
	    Prestamo P
	INNER JOIN
	    Articulo Ar ON P.Id_articulo = Ar.Id_articulo
		
	UNION
	
	SELECT
	    A.Nombre_articulo AS Nombre_producto,
	    A.Tipo_articulo AS Tipo_servicio,
	    V.Fecha_venta AS Fecha_operacion,
		NULL AS Hora_inicio,
		NULL AS Hora_fin,
		NULL AS Fecha_devolucion,
	    A.Precio_unitario AS Monto,
	    V.Estado_pago AS Estado_operacion,
		DV.Medio_pago
	FROM
	    Detalle_venta DV
	INNER JOIN
	    Venta V ON DV.Id_venta = V.Id_venta
	INNER JOIN
	    Articulo A ON DV.Id_articulo = A.Id_articulo;
		
 |**Contar la cantidad de Ventas**|
 
	SELECT
	    COUNT(V.Id_venta) AS Cantidad_ventas
	FROM
	    Venta V;
		
		
|**Contar la cantidad de prestamos**|

	SELECT
	    COUNT(P.Id_prestamo) AS Cantidad_prestamos
	FROM
	    Prestamo P;
		
|**contar la cantidad de Alquiler**|

	SELECT
	    COUNT(A.Id_alquiler) AS Cantidad_ventas
	FROM
	    Alquiler A;
**Suma de registros totales DE LA PAGINA DEL CEIIS**

	SELECT
	    (
	        -- Subconsulta para contar registros de préstamos
	        COALESCE((SELECT COUNT(*) FROM Prestamo P ), 0) +
	        -- Subconsulta para contar registros de ventas
	        COALESCE((SELECT COUNT(*) FROM Venta V ), 0) +
	        -- Subconsulta para contar registros de alquileres
	        COALESCE((SELECT COUNT(*) FROM Alquiler A ), 0)
	    ) AS Total_registros ;	

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


## nn
| Código requerimiento | R-00 |
| --- | --- |
| Codigo interfaz |  I-00 |
| Imagen interfaz  |

![Alt texasdt](Vistas_Noticias/Mostrar_Noticias.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Noticia:** Se mostrará el contenido de la noticia |
|**SELECT Fecha, Titulo, Descricion FROM Noticia;**|
