HT - 01

Configuración Inicial Proyecto

**Como** desarrollador
**Quiero** configurar la estructura base del backend con sus dependencias y conexión a base de datos
**Para** poder desplegar una versión inicial estable en Render y comenzar el desarrollo sobre una base funcional
**🎯 Descripción**

e requiere crear la configuración inicial del proyecto backend utilizando FastAPI, incluyendo la definición de dependencias (`requirements.txt`), variables de entorno, y conexión a base de datos PostgreSQL en Render, asegurando que el servicio pueda desplegarse correctamente aunque aún no tenga lógica de negocio implementada.
****
 **Criterios de Aceptación**


-  ] El proyecto contiene un archivo `requirements.txt` funcional

-  ] La aplicación FastAPI inicia correctamente sin errores

-  ] Existe un endpoint básico (`/` o `/health`) que responde correctamente

-  ] La conexión a la base de datos está configurada mediante variables de entorno

-  ] La aplicación puede conectarse a la base de datos sin errores

-  ] Se incluye soporte para conexión segura (`sslmode=require`)

-  ] El proyecto se puede desplegar en Render sin fallos

-  ] El servicio queda accesible mediante una URL pública
****

 **Tareas Técnicas**
• 

-  Crear estructura base del proyecto (main.py, config, etc.)
• 
-  Configurar entorno virtual local
• 
-  Generar archivo `requirements.txt`
• 
-  Implementar conexión a PostgreSQL usando variables de entorno
• 
-  Configurar CORS en FastAPI
• 
-  Crear endpoint de prueba (`/health`)
• 
-  Configurar start command para Render (`uvicorn main:app --host 0.0.0.0 --port 10000`)
• 
-  Subir proyecto a repositorio Git
• 
-  Configurar variables de entorno en Render
• 
-  Verificar deploy exitoso
**🧪** 

**riterios de Prueba**
• [

- Al acceder a `/health` retorna status 200
• [
- No hay errores en logs de Render
• [
- La conexión a la base de datos se establece correctamente
• [
- El servicio permanece activo después del deploy
**📌 N**

**tas**
• No

-  requiere lógica de negocio en esta etapa
• Es
- historia establece la base para futuras funcionalidades
• Se
- comienda estructurar el proyecto pensando en escalabilidad futura

HT - 02

Implementación de sistema de logs básico

**Como** desarrollador del sistema
**Quiero** implementar un sistema de logs en la conexión a la base de datos y en la ejecución de los endpoints principales
**Para** poder monitorear el comportamiento de la aplicación y detectar errores de forma más sencilla
**Criterios de Aceptación:**

- Se generan logs al iniciar la conexión con la base de datos (éxito o error)
- Se registran logs cada vez que se ejecuta un endpoint (inicio y fin de la petición)
- Los logs incluyen información básica como fecha, endpoint y estado de la operación
- En caso de error, el log debe registrar el mensaje de error correspondiente
- El sistema de logs debe funcionar tanto en entorno local como en producción (Render)

**Notas Técnicas:**

- Usar el módulo `logging` de Python
- Configurar nivel de logs (INFO, ERROR)
- Centralizar configuración de logs en un archivo o módulo reutilizable
- Probar SIEMPRE en local antes de desplegar en ambiente Dev

HT - 03

Creación Base de datos

**🧾 Historia de Usuario – Diseño de Base de Datos (Ajuste de Convención de FK)**

 **Rol**
Como
**analista funcional**, necesito ajustar la convención de nombres de las claves foráneas en la base de datos, para mantener consistencia, claridad y buenas prácticas en el modelo relacional.
**📌 Aj**
**ste Solicitado**
Se re
uiere que **todas las claves foráneas (FK)** sigan la convención:🔹 **nombre_entidad_id**
Ejempl
: `producto_id`, `usuario_id`, `venta_id`
Esto m
jora:
• Legi

- idad del esquema
• Esta
- rización
• Faci
- ad en desarrollo backend (ORMs como JPA/Hibernate)
**🧩 Mode**

**o de Datos Ajustado
1. 👤 Us**
**ario**
**Campos:**

 usuari

- d (PK)
• nombre
- ARCHAR 100)
• email 
- RCHAR 150, UNIQUE)
• contra
- a (VARCHAR 255)
• estado
- OOLEAN)
• rol_id
- K)
**2. 🛡️ Rol**

**Campos:**
• 
ol_id (

- 
• nombre (
- CHAR 50)
• descripc
-  (VARCHAR 150)
**3. 👕 Produ**

**to**
**Campos:**
• p
oducto_

- (PK)
• nombre (V
- HAR 120)
• descripci
- (TEXT)
• estado (B
- EAN)
• fecha_cre
- on (TIMESTAMP)
**4. 📦 Refere**

**cia**
**Campos:**
• re
erencia

-  (PK)
• producto_i
- FK)
• talla (VAR
- R 10)
• cantidad (
- EGER)
• precio_com
-  (NUMERIC 10,2)
• precio_ven
- (NUMERIC 10,2)
• proveedor_
- (FK)
**5. 🚚 Proveed**

**r**
**Campos:**
• pro
eedor_i

- PK)
• nombre (VAR
- R 120)
• telefono (V
- HAR 20)
• email (VARC
-  150)
**6. 🧾 Venta**
**Ca**

**pos:**
• vent
_id (PK

-  fecha (TIMES
- P)
• usuario_id (
- 
• cliente_id (
-  NULLABLE)
• total (NUMER
- 12,2)
**7. 🧺 Venta_Pro**

**ucto**
**Campos:**
• venta
product

- d (PK)
• venta_id (FK)
- referencia_id
- K)
• cantidad (INT
- R)
• precio_unitar
- (NUMERIC 10,2)
**8. 🧍 Cliente**
**Ca**

**pos:**
• client
_id (PK

-  nombre (VARCHA
- 20)
• telefono (VARC
-  20)
• email (VARCHAR
- 0)
**9. 🧾 Auditoria_P**

**oducto**
**Campos:**
• auditor
a_id (P

- • producto_id (FK
-  accion (VARCHAR
- )
• fecha (TIMESTAM
- • usuario (VARCHA
- 00)
• detalle (TEXT)
****
-  **📊 Historico_R**

**ferencia**
**Campos:**
• historic
_id (PK

-  referencia_id (F
- • precio_anterior 
- MERIC 10,2)
• precio_nuevo (NU
- IC 10,2)
• cantidad_anterio
- INTEGER)
• cantidad_nueva (
- EGER)
• fecha (TIMESTAMP
-  **Relaciones (Actu**

**lizadas con Convención)**
• Usuario.**rol_id** → 

- .rol_id
• Referencia.**produc**
- **id** → Producto.producto_id
• Referencia.**provee**
- **_id** → Proveedor.proveedor_id
• Venta.**usuario_id** 
- suario.usuario_id
• Venta.**cliente_id** 
- liente.cliente_id
• Venta_Producto.**ve**
- **_id** → Venta.venta_id
• Venta_Producto.**re**
- **encia_id** → Referencia.referencia_id
• Auditoria_Product
- **roducto_id** → Producto.producto_id
• Historico_Referen
- .**referencia_id** → Referencia.referencia_id

HU - 04

Envío Correo Felicitación

Como administrador del sistema
Quiero implementar un servicio automatizado que lea fechas de cumpleaños desde Google Sheets y envíe felicitaciones por correo electrónico y WhatsApp
Para poder automatizar el envío de mensajes de cumpleaños a clientes sin intervención manual

Criterios de Aceptación:

- El sistema debe conectarse correctamente a una hoja de cálculo de Google Sheets configurada previamente
- El sistema debe validar diariamente si existen clientes que cumplen años en la fecha actual
- El sistema debe enviar automáticamente un correo de felicitación a los clientes encontrados
- El sistema debe enviar automáticamente un mensaje de felicitación por WhatsApp a los clientes encontrados
- El sistema debe registrar en logs los envíos exitosos y los errores ocurridos durante la ejecución
- El sistema debe evitar enviar mensajes duplicados el mismo día al mismo cliente
- El sistema debe permitir configurar el mensaje de felicitación sin modificar el código fuente
- El proceso debe ejecutarse automáticamente mediante una tarea programada

Notas Técnicas:

- Usar Python para la automatización del servicio
- Consumir Google Sheets mediante Google Sheets API o gspread
- Implementar envío de correos mediante SMTP o Gmail API
- Implementar integración con WhatsApp mediante API oficial o automatización controlada
- Configurar variables sensibles mediante variables de entorno (.env)
- Implementar logs utilizando el módulo logging de Python
- Validar funcionamiento en entorno local antes de desplegar en ambiente Dev/Producción
- Considerar despliegue en Render, Railway o servidor Linux con ejecución programada mediante cron o scheduler

HT - 05

Migración de Base de Datos Compartida

**Como** desarrollador
**Quiero** migrar la base de datos del sistema de ventas a una cuenta compartida y actualizar las variables de entorno
**Para** poder centralizar la administración de la base de datos y garantizar que el backend continúe funcionando correctamente en Render bajo una configuración estable y colaborativa

🎯 Descripción

e requiere migrar la base de datos PostgreSQL actual del sistema de ventas a una cuenta común del proyecto en Render, actualizando las variables de entorno y la configuración de conexión utilizadas por el backend desarrollado con FastAPI y SQLAlchemy.


a migración debe asegurar la continuidad del servicio, mantener la integridad de los datos existentes y permitir que el equipo trabaje sobre una infraestructura compartida y mantenible.


 Criterios de Aceptación


-  ] La base de datos PostgreSQL fue migrada correctamente a la cuenta compartida

-  ] La información existente se conserva después de la migración

-  ] Las variables de entorno fueron actualizadas correctamente en el proyecto

-  ] La aplicación establece conexión exitosa con la nueva base de datos

-  ] La conexión continúa utilizando sslmode=require

-  ] El backend inicia correctamente después de la actualización

-  ] Los endpoints continúan funcionando sin errores

-  ] La documentación automática en /docs permanece accesible

-  ] El despliegue en Render se realiza exitosamente

-  ] El servicio continúa disponible mediante la URL pública


 Tareas Técnicas
• 

-  Crear nueva instancia PostgreSQL en la cuenta compartida de Render
• 
-  Exportar respaldo de la base de datos actual
• 
-  Importar los datos en la nueva base de datos
• 
-  Actualizar DATABASE_URL y demás variables de entorno
• 
-  Modificar configuración de conexión en SQLAlchemy
• 
-  Verificar compatibilidad de sslmode=require
• 
-  Actualizar variables de entorno en Render
• 
-  Validar conexión desde el backend FastAPI
• 
-  Ejecutar pruebas básicas de endpoints
• 
-  Verificar correcto funcionamiento de /docs
• 
-  Revisar logs de Render después del deploy
• 
-  Documentar nuevas configuraciones para el equipo

🧪

riterios de Prueba
• [

- La API responde correctamente después de la migración
• [
- La conexión a la nueva base de datos no genera errores
• [
- Los datos existentes permanecen íntegros
• [
- No aparecen errores relacionados con credenciales o variables de entorno
• [
- Los logs de Render no presentan fallos críticos
• [
- El servicio permanece activo después del despliegue

📌 

tas
• Es

- tarea corresponde a un bugfix de infraestructura y configuración
• La
- gración debe realizarse minimizando el tiempo de inactividad
• Se
- comienda mantener un respaldo previo de la base de datos original
• Es
- historia garantiza una configuración más segura y colaborativa para el proyecto futuro

