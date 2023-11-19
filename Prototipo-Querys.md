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
| Código requerimiento | R-005 |
| --- | --- |
| Codigo interfaz |  I-005 |
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

## 9
| Código requerimiento | R-09 |
| --- | --- |
| Codigo interfaz |  I-09 |
| Imagen interfaz  |

![Alt texasdt](Preguntas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar pagina:** Se llenará la fecha de las encuestas a mostrar  |
| **SELECT Id_encuesta FROM Encuesta E WHERE E.Fecha_apertura = '<1>'**;|
| **2. Cargar pagina:** Muestra las encuestas activas  |
|**SELECT Id_encuesta FROM Encuesta E WHERE E.Estado_encuesta = 'activo'; <2>**|

## 10
| Código requerimiento | R-10 |
| --- | --- |
| Codigo interfaz |  I-10 |
| Imagen interfaz  |

![Alt texasdt](preguntas/preguntas2.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón cruz:** Se añadirá una nueva encuesta|
| **INSERT INTO Encuesta (Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta) VALUES ('ENC0011', 'ADM005', '2024-01-13', '2024-01-20', 9, 30, 'inactivo');'<1>'**|
| **2. Cargar pagina:** Muestra las encuestas realizadas**  |
|**SELECT COUNT(E.Id_encuesta) AS "Encuestas Realizadas" FROM Encuesta E; <2>**|
| **3. Botón editar encuesta: Se edita una encuesta activa** |
|**UPDATE Encuesta SET Fecha_apertura = '2023-12-13', Fecha_cierre = '2023-12-23', Cantidad_preguntas = '9', Cantidad_respuestas = '9', Estado_encuesta = 'inactivo' WHERE Id_encuesta = 'ENC002'; <3>** |


## 11
| Código requerimiento | R-11 |
| --- | --- |
| Codigo interfaz |  I-11 |
| Imagen interfaz  |

![Alt texasdt](preguntas/preguntas3.png)

| Sentencias SQL |
| --- |
| Eventos |
|**1. Cargar pagina:** Se llenará la pregunta asociada a una encuesta  |
|**INSERT INTO Pregunta (Id_pregunta, Id_encuesta, Id_administrador, Descripción, Tipo_respuesta) VALUES ('PRE0011', 'ENC004', 'ADM004','¿En qué ciclo relativo se encuentra?', 'opcion multiple'); <1>**| 
|**2. Cargar pagina:** Se escogerá el tipo de pregunta |
|**UPDATE Pregunta SET Tipo_respuesta = 'opcion multiple' WHERE Id_encuesta = 'ENC004' AND Id_pregunta = 'PRE006';<2>  **|
|**2. Botón papelera:** Se borrará la pregunta|
|**DELETE FROM Pregunta WHERE Id_encuesta = 'id_de_tu_encuesta' AND Id_pregunta = 'id_de_tu_pregunta';<3>  **|


## 12
| Código requerimiento | R-12 |
| --- | --- |
| Codigo interfaz |  I-12 |
| Imagen interfaz  |

![Alt texasdt](reservasyalquileres.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los reservas y alquileres   |
|**SELECT Nombre_articulo, Precio_unitario FROM Articulo WHERE Tipo_articulo = 'reservas y alquileres';** |

## 13
| Código requerimiento | R-13 |
| --- | --- |
| Codigo interfaz |  I-13 |
| Imagen interfaz  |

![Alt texasdt](productos_ventas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los productos para venta  |
|**SELECT Nombre_articulo, Precio_unitario FROM Articulo WHERE Tipo_articulo = 'reservas y alquileres';** |

## 14
| Código requerimiento | R-14 |
| --- | --- |
| Codigo interfaz |  I-14 |
| Imagen interfaz  |

![Alt texasdt](productos_prestamos.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Cargar página:** Se mostraran los productos para prestamo   |
|**SELECT Nombre_articulo FROM Articulo WHERE Tipo_articulo = 'prestamo';**|

## 15
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

## 16
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

## 17
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

## 18
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

## 19
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

## 20
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

## 21
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

## 22
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

## 23
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

## 24
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


## 25
| Código requerimiento | R-025 |
| --- | --- |
| Codigo interfaz |  I-25 |
| Imagen interfaz  |

![Alt texasdt](Vistas_Noticias/Mostrar_Noticias.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Noticia:** Se mostrará el contenido de la noticia |
|**SELECT Fecha, Titulo, Descricion FROM Noticia;**|


## 26
| Código requerimiento | R-026 |
| --- | --- |
| Codigo interfaz |  I-26 |
| Imagen interfaz  |

![Alt texasdt](Vistas_Noticias/Agregar_Noticias.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Confirmar:** Se agregarán la fecha, titulo y la descripcion de la noticia |
|**INSERT INTO Noticia (Id_notica, Id_administrador, Fecha, Titulo, Descripcion) VALUES (<Id_noticia>, <Id_administrador>, < fecha >, < titulo >, < desccripcion >);**|

## 27
| Código requerimiento | R-027 |
| --- | --- |
| Codigo interfaz |  I-27 |
| Imagen interfaz  |

![Alt texasdt](Vistas_Noticias/Actualizar_Noticias.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Confirmar:** Se cambiaran lo que desee de la noticia, ya sea fecha, titulo, descripcion  |
|**UPDATE Noticia SET Fecha = < fecha > , < titulo > , <Descripción> WHERE Id_noticia = <Id_noticia>;**|

## 28
| Código requerimiento | R-028 |
| --- | --- |
| Codigo interfaz |  I-28 |
| Imagen interfaz  |

![Alt texasdt](Vistas_Noticias/Quitar_Noticias.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón Confirmar:** Se eliminara la noticia que ya pasó el evento o la informacion colocada  |
|**DELETE FROM Noticia WHERE Id_notica = <ID_NOTICIA>**|

## 29
| Código requerimiento | R-029 |
| --- | --- |
| Codigo interfaz |  I-29 |
| Imagen interfaz  |

![Alt texasdt](vistas_finanzas_estadisticas/estadisticas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón de fecha:** Se carga la pagina mostrnado la información, la fecha del mes soliticado, mostrando tanto las ventas, prestámos y alquileres, desde el número de ventas, préstamos y alquleres, mostrnado asi mismo la mayor cantidad asi como el de menor cantidad, sacando un cuadro estadisticos y asi mismo, mostrando lo recaudado, siendo (1 mes que se quiere conocer y 1.1 año en el que se quiere conocer)|

|**Numero total de alquileres al mes**|

	SELECT COUNT(*) AS Cantidad_Alquileres
		FROM alquiler
	WHERE EXTRACT(MONTH FROM Fecha_alquiler) = <1>
	AND EXTRACT(YEAR FROM Fecha_alquiler) = <1.1>;

|**Numero total de ventas**|

	SELECT COUNT (*) AS Cantidad_venta
	From venta
	WHERE EXTRACT(MONTH FROM fecha_venta) = <1>
	AND EXTRACT(YEAR FROM fecha_venta) = <1.1>;

|**Numero total de prestamos**|

	SELECT COUNT (*) AS Cantidad_prestamos
	FROM prestamo
	WHERE EXTRACT(MONTH FROM fecha_prestamo) = <1>
	AND EXTRACT(YEAR FROM fecha_prestamo) = <1.1>;

|**Total recaudado de ventas y alquileres**|

	SELECT SUM(monto) AS Cantidad_Total_Monto_Recaudado_Alquiler
	FROM alquiler
	WHERE EXTRACT(MONTH FROM Fecha_alquiler) = <1>;

	SELECT SUM(monto_final) AS Cantidad_Total_Monto_Recaudado_Venta
	FROM venta
	WHERE EXTRACT(MONTH FROM fecha_venta) = <1.1>;

|**Total recaudado de ventas y alquileres**|

	SELECT COUNT(*) AS Total
	FROM (
    SELECT 'Alquiler'
    FROM Alquiler
    WHERE EXTRACT(MONTH FROM Fecha_alquiler) = <1>
      AND EXTRACT(YEAR FROM Fecha_alquiler) = <1.1>
    UNION ALL
    SELECT 'Prestamo'
    FROM Prestamo
    WHERE EXTRACT(MONTH FROM Fecha_prestamo) = <1>
      AND EXTRACT(YEAR FROM Fecha_prestamo) = <1.1>
    UNION ALL
    SELECT 'Venta'
    FROM Venta
    WHERE EXTRACT(MONTH FROM Fecha_venta) = <1>
      AND EXTRACT(YEAR FROM Fecha_venta) = <1.1>
	) AS transacciones_semana;

|**Cual es el árticulo más y menos alquilado**|

	SELECT a.Nombre_articulo
	FROM alquiler al
	JOIN articulo a ON al.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM al.Fecha_alquiler) = <1>
		AND EXTRACT(YEAR FROM al.Fecha_alquiler) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) DESC
	LIMIT 1;

	SELECT COUNT(*) AS Cantidad_Alquileres
	FROM alquiler AS al
	JOIN articulo a ON al.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM al.Fecha_alquiler) = <1>
		AND EXTRACT(YEAR FROM al.Fecha_alquiler) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) DESC
	LIMIT 1;

	SELECT a.Nombre_articulo
	FROM alquiler al
	JOIN articulo a ON al.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM al.Fecha_alquiler) = <1>
		AND EXTRACT(YEAR FROM al.Fecha_alquiler) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) ASC
	LIMIT 1;

	SELECT COUNT(*) AS Cantidad_Alquileres
	FROM alquiler AS al
	JOIN articulo a ON al.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM al.Fecha_alquiler) = <1>
		AND EXTRACT(YEAR FROM al.Fecha_alquiler) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) ASC
	LIMIT 1;

|**Cual es el articulo más y menos prestado**|

	SELECT a.Nombre_articulo
	FROM prestamo p
	JOIN articulo a ON p.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM p.Fecha_prestamo) = <1>
		AND EXTRACT(YEAR FROM p.Fecha_prestamo) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) DESC
	LIMIT 1;

	SELECT COUNT(*) AS Cantidad_Prestamos
	FROM prestamo AS p
	JOIN articulo a ON p.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM p.Fecha_prestamo) = <1>
		AND EXTRACT(YEAR FROM p.Fecha_prestamo) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) DESC
	LIMIT 1;

	SELECT a.Nombre_articulo
	FROM prestamo p
	JOIN articulo a ON p.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM p.Fecha_prestamo) = <1>
		AND EXTRACT(YEAR FROM p.Fecha_prestamo) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) ASC
	LIMIT 1;

	SELECT COUNT(*) AS Cantidad_Prestamos
	FROM prestamo AS p
	JOIN articulo a ON p.Id_articulo = a.Id_articulo
	WHERE EXTRACT(MONTH FROM p.Fecha_prestamo) = <1>
		AND EXTRACT(YEAR FROM p.Fecha_prestamo) = <1.1>
	GROUP BY a.Nombre_articulo
	ORDER BY COUNT(*) ASC
	LIMIT 1;

|**Cual es el articulo más y menos vendido**|

	SELECT a.Nombre_articulo AS Articulo_Mas_Vendido
	FROM articulo a
	JOIN (
		SELECT d.Id_articulo, SUM(d.Cantidad) AS Total_Vendido
		FROM detalle_venta d
		GROUP BY d.Id_articulo
		ORDER BY Total_Vendido DESC
		LIMIT 1
	) subquery ON a.Id_articulo = subquery.Id_articulo;

	SELECT  SUM(d.Cantidad) AS Total_Unidades_Vendidas
	FROM articulo a
	JOIN detalle_venta d ON a.Id_articulo = d.Id_articulo
	GROUP BY a.Nombre_articulo
	ORDER BY Total_Unidades_Vendidas DESC
	LIMIT 1;

## 30
| Código requerimiento | R-030 |
| --- | --- |
| Codigo interfaz |  I-30 |
| Imagen interfaz  |

![Alt texasdt](vistas_finanzas_estadisticas/finanzas.png)

| Sentencias SQL |
| --- |
| Eventos |
| **1. Botón de fecha:** Se carga la pagina mostrnado la información, la fecha del mes soliticado, mostrando tanto las ventas, prestámos y alquileres, desde el número de ventas, préstamos y alquleres, mostrnado asi mismo la mayor cantidad asi como el de menor cantidad, sacando un cuadro estadisticos y asi mismo, mostrando lo recaudado, siendo (1 mes que se quiere conocer y 1.1 año en el que se quiere conocer)|

|**Total de Transacciones del mes**|

	SELECT COUNT(*) AS Total
	FROM (
    SELECT 'Alquiler'
    FROM Alquiler
    WHERE EXTRACT(MONTH FROM Fecha_alquiler) = <1>
      AND EXTRACT(YEAR FROM Fecha_alquiler) = <1.1>
    UNION ALL
    SELECT 'Prestamo'
    FROM Prestamo
    WHERE EXTRACT(MONTH FROM Fecha_prestamo) = <1>
      AND EXTRACT(YEAR FROM Fecha_prestamo) = <1.1>
    UNION ALL
    SELECT 'Venta'
    FROM Venta
    WHERE EXTRACT(MONTH FROM Fecha_venta) = <1>
      AND EXTRACT(YEAR FROM Fecha_venta) = <1.1>
	) AS transacciones_semana;

|**Total recaudado de alquiler al mes**|

	SELECT SUM(monto) AS Cantidad_Total_Monto_Recaudado_Alquiler
	FROM alquiler
	WHERE EXTRACT(MONTH FROM Fecha_alquiler) = <1>;

|**Total recaudado de alquiler al mes**|

	SELECT SUM(monto_final) AS Cantidad_Total_Monto_Recaudado_Venta
	FROM venta
	WHERE EXTRACT(MONTH FROM fecha_venta) = <1>;

|**Total recaudado al mes por alquiler y venta**|

	SELECT
    COALESCE(SUM(monto) + SUM(monto_final), 0) AS Monto_Total_General
	FROM (
    SELECT
        monto,
        0 AS monto_final
    FROM Alquiler
    WHERE EXTRACT(MONTH FROM CURRENT_DATE) = <1>

    UNION ALL

    SELECT
        0 AS monto,
        monto_final
    FROM Venta
    WHERE EXTRACT(MONTH FROM CURRENT_DATE) = <1>
	) AS CombinedData;

|**Historial de ventas y alquileres**|

	SELECT  
    Ar.Nombre_articulo AS Nombre_producto,
    Ar.Tipo_articulo AS Tipo_servicio,
    A.Fecha_alquiler AS Fecha_operacion,
    A.Monto,
    A.Estado_alquiler AS Estado_operacion,
    A.Medio_pago
	FROM
		Alquiler A
	INNER JOIN
		Articulo Ar ON A.Id_articulo = Ar.Id_articulo
		
	UNION

	-- Consulta para ventas
	SELECT
		A.Nombre_articulo AS Nombre_producto,
		A.Tipo_articulo AS Tipo_servicio,
		V.Fecha_venta AS Fecha_operacion,
		A.Precio_unitario AS Monto,
		V.Estado_pago AS Estado_operacion,
		DV.Medio_pago
	FROM
		Detalle_venta DV
	INNER JOIN
		Venta V ON DV.Id_venta = V.Id_venta
	INNER JOIN
    Articulo A ON DV.Id_articulo = A.Id_articulo;

# Funcionalidad Primaria Elegida (por módulo)

### 1.Modulo de seguridad
**Flujo de actividades**
1. El usuario ingresa a su cuenta personal proporcionando su correo y su contraseña y se dirige a perfil.
   
![Alt texasdt](Loginpage.png)

2. Una vez en su perfil el usuario visualiza un reporte de los últimos servicios que ha utilizado del CEIIS, y conteos de estos. Se muestra un conteo de cada tipo de servicio por separado y un conteo general de los servicios utilizados.

![Alt texasdt](Loginpage.png)

3. El usuario tiene la opción de presionar “Ver todo” para dirigirse y tener un reporte completo de todos los servicios que ha utilizado, este reporte puede filtrase por fecha.

![Alt texasdt](Historialdelusuario.png)

**Justificacion**

Esta actividad es elegida la funcionalidad principal porque permite que el usuario puede visualizar un historial de los servicios que ha utilizado, además de poder ver el estado (pendiente, devuelto) de los servicios de alquiler que ha realizado. 
Esto proporciona al usuario una visión clara y detallada de los servicios que han utilizado, evaluar su propia actividad y detectar algún uso no reconocido de los servicios. 
El filtro de fecha ofrece a los usuarios la posibilidad de acceder fácilmente a informes detallados sobre su actividad contribuye a una experiencia de usuario mejorada. Los usuarios se benefician al tener un control más claro sobre su propia información y actividad.
Los requerimientos e interfaces elegidos fueron:
| Requerimiento | Interfaz |
| --- | --- |
| R-002 |  I-002 |
| R-005 |  I-005 |
| R-005 |  I-006 |

En esta funcionalidad se requiere información de la tabla Usuario, Articulo, Alquiler, Venta, DetalleVenta y Prestamo.

Las consultas que se pueden realizar son:

**Creacion de las tablas**

	create table Usuario( 
			Id_usuario varchar(8) PRIMARY KEY,
			Dni varchar(8) references Persona(Dni),
			Cod_uni varchar(9) unique,
			Correo_uni varchar(50) unique,  
	 		Contrasena varchar(30)
	);
	create table Articulo(
			Id_articulo varchar(8) PRIMARY KEY,
			Nombre_articulo varchar(25),
			Tipo_articulo varchar(25),
			Cantidad numeric(2),
			Descripcion varchar(50),
			Precio_unitario numeric(3,2),
	 		Disponibilidad varchar(20)
	);
	
	create table Venta( 
			Id_venta varchar(8) PRIMARY KEY,
			Id_usuario varchar(8) references Usuario(Id_usuario),
	 		Fecha_venta date,
	 		Monto_final numeric(4,2),
	 		Estado_pago varchar(10)
	);
	
	create table Detalle_venta( 
			Id_venta varchar(8) references Venta(Id_venta),  
			Id_articulo varchar(8) references Articulo(Id_articulo),
			Medio_pago varchar(25),
			Cantidad numeric(2),
	 		Subtotal numeric(4,2),
	 		PRIMARY KEY(Id_venta, Id_articulo)
	);
	
	create table Alquiler(
			Id_alquiler varchar(8) PRIMARY KEY,
			Id_usuario varchar(8) references Usuario(Id_usuario),
			Id_articulo varchar(8) references Articulo(Id_articulo),
			Fecha_alquiler date,
			Hora_inicio time,
			Hora_fin time,
			Medio_pago varchar(20),
			Monto numeric(3,2),
	 		Estado_alquiler varchar(15)
	);
	
	create table Prestamo(
			Id_prestamo varchar(8) PRIMARY KEY,
			Id_usuario varchar(8) references Usuario(Id_usuario),
			Id_articulo varchar(8) references Articulo(Id_articulo),
			Fecha_prestamo date,
			Hora_prestamo time,
	 		Fecha_devolucion date,
	 		Hora_devolucion time,
	 		Estado_prestamo varchar(15)
	);

**Consultas**

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
	
**CONTAR CANTIDAD DE PRESTAMOS DEL USUARIO**

	SELECT
	    COUNT(P.Id_prestamo) AS Cantidad_prestamos
	FROM
	    Prestamo P
	INNER JOIN
	    Usuario U ON P.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';
		
**CONTAR CANTIDAD DE VENTAS DEL USUARIO**

	SELECT
	    COUNT(V.Id_venta) AS Cantidad_ventas
	FROM
	    Venta V
	INNER JOIN
	    Usuario U ON V.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';
		
	-- CONTAR CANTIDAD DE ALQUILER DEL USUARIO
	SELECT
	    COUNT(A.Id_alquiler) AS Cantidad_ventas
	FROM
	    Alquiler A
	INNER JOIN
	    Usuario U ON A.Id_usuario = U.Id_usuario
	WHERE
	    U.Id_usuario = '1';	

**TOTAL DE SERVICIOS UTILIZADOS POR EL USUARIO**

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
     
**Busqueda por fecha**

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

### 2. Finanzas
**Flujo de actividades**	

![Alt texasdt](vistas_finanzas_estadisticas/finanzas.png)

1. Una vez el administrador, haya ingresado a su cuenta, podra entrar a la sección  de finanzas en la cual podra visualizar las transacciones hehcas al mes y cuanto fue lo recuadado en ese mes y año. Tiene un boton que se visualiza en la imagen <1> el cual es el filtro de fecha que dependiendo el mes y año se podra visualizar la información de total de servicios de mes, y por cada prestamo, el historial total de ventas/ alquileres, si fue pagado en fectivo o en yape y el estado, en caso de alquiler es si fue devuelto o no, y en caso de venta si fue pagado o no. Donde tambien se podra visualizar el total del mes, y el total de cada servicio.

En esta funcionalidad se requiere información de la tabla Articulo, Alquiler, Venta, DetalleVenta y Prestamo.

### 3. Estadísticas
**Flujo de actividades**	

![Alt texasdt](vistas_finanzas_estadisticas/estadisticas.png)

1. Una vez el administrador, haya ingresado a su cuenta, podra ir a la sección de estadísticas, en la cual podra ver por venta, préstamo y alquiler. el Monto total de cada uno, la cantidad y nombre de la mayor cantidad de cada transacción y la cantidad y nombre de la menor cantidad de cada transacción. Tambien podrá visualizar el total de monto recaudado por alquiler y venta, y por ultimo un total de servicios brindados de la semana.

En esta funcionalidad se requiere información de la tabla Articulo, Alquiler, Venta, DetalleVenta y Prestamo.

### 4.Modulo de encuestas
**Flujo de actividades**
1. El administrador después de haber ingresado a su perfil, escogerá la sección encuestas, ahi tendra la opción de añadir una nueva encuesta.
![Alt texasdt](preguntas/preguntas2.png)
2. El administrador tendra la opción de escribir las preguntas, quitar preguntas, añadir título y escoger el tipo de pregunta.
![Alt texasdt](preguntas/preguntas3.png)

Esta funcionalidad requiere información de las tablas encuesta y pregunta.

	create table Encuesta( 
		Id_encuesta varchar(8) primary key,  
		Id_administrador varchar(8) references Administrador(Id_administrador),
		Fecha_apertura date,
		Fecha_cierre date,
		Cantidad_preguntas numeric(2),
		Cantidad_respuestas numeric(2),
		Estado_encuesta varchar(10)
	);

	create table Pregunta(
		Id_pregunta varchar(8) ,  
		Id_encuesta varchar(8) references Encuesta(Id_encuesta),
		Id_administrador varchar(8) references Administrador(Id_administrador),
		Tipo_respuesta varchar(15),
		PRIMARY KEY (Id_encuesta, Id_pregunta)
  	);
Requiere de las siguientes consultas
**CANTIDAD TOTAL DE ENCUESTAS EN LA PAGINA**

	SELECT
		COUNT(E.Id_encuesta) AS "Encuestas Realizadas";
	FROM
		Encuesta E;
**AÑADIR ENCUESTA**

	INSERT INTO Encuesta (Id_encuesta, Id_administrador, Fecha_apertura, Fecha_cierre, Cantidad_preguntas, Cantidad_respuestas, Estado_encuesta) VALUES ('ENC0011', 'ADM005', '2024-01-13', '2024-01-20', 9, 30, 'inactivo');

**BORRAR PREGUNTA**

	DELETE FROM Pregunta
	WHERE Id_encuesta = 'id_de_tu_encuesta' AND Id_pregunta = 'id_de_tu_pregunta';

**ACTUALIZAR PREGUNTA**

	UPDATE Pregunta
	SET Tipo_respuesta = 'opcion multiple'
	WHERE Id_encuesta = 'ENC004' AND Id_pregunta = 'PRE006';

**AÑADIR PREGUNTA**

	INSERT INTO Pregunta (Id_pregunta, Id_encuesta, Id_administrador, Tipo_respuesta) VALUES
	('PRE0011', 'ENC004', 'ADM004', 'opcion multiple');

 

