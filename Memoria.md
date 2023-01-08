# Memoria
## Entrega 3
### 1. Propuesta general de diseño
 Propuesta de una interfaz sencilla estilo *stackoverflow* pero con comentarios de estilo *reddit* en varios niveles segun quien responde a quien. 
 
 El sistema de votacion puede ser estilo *reddit* o *stackoverflow* indistintamente, con enfoque en los puntos para el orden y como forma de recompensar al usuario, de esta forma como los comentarios mas votados aparecen primero no sera necesario que el usuario se tenga que leer todo.

 Un esquema simple de como apareceran los comentarios a una pregunta:
- Pregunta
  - Respuesta 1 
  - Respuesta 2 
    - Comentario a la respuesta 2 (👍)
  - Respuesta 3
    - Comentario a la respuesta 2 (👎)
  
#### 1.1 Diseño de las preguntas
Las preguntas podrian ser simples o se puede contemplar la opcion de agregar imagenes o texto enriquecido, se valorara segun complejidad durante el desarrollo del proyecto.

#### 1.2 Tipos de usuarios
En cuanto al la estructura de paginas podremos diferenciar entre las paginas para usuarios logeados y las de usuarios anonimos, a pesar que dentro de los logueados puedan existir distintos roles, los dos gradnes grupos son los anteriormente mensionados.

Un usuario no logueado:
- Podra ver las preguntas que hacen otros usuarios
- Al hacer click en una pregunta podra ver las respuestas a esta
- Se le dara la posibilidad de crearse una cuenta o iniciar sesion
- No se le permitira hacer nuevas preguntas o responderlas
- No podra votar las preguntas/respuestas
- No podra reportar preguntas/respuestas

Un usuario logueado podra realizar las actividades propias de su rol.

Por lo tanto se podra acceder a la pagina raiz o "inicio" sin estar logueado para tener una vision general de la aplicacion o a una pregunta en concreto, pero para hacer cualquier otra accion se tendra que estar logueado. El funcionamiento sera identico al de *StackOverflow*, de esta forma no sera necesario trabajar demasiado en la UX.

#### 1.3 Funciones de los usuarios

Dentro de los usuarios existen distintos roles:
- Discusion: Es el usuario standard, puede crear y responder preguntas.
- Moderador: Se encarga de atender los reportes sobre las preguntas y los comentarios.
- Administrador: Es un rol especial que solo lo tendra el primer usuario creado "admin"

Un usuario Moderador no podra publicar preguntas/respuestas y un Discusion no podra moderar.

#### 1.4 Elementos principales

La base de las aplicacion son las preguntas con respuestas a modo de resolucion y comentarios a la respuestas valorandolas, segun si son utiles o no. La dinamica es extremadamente parecida a la de *StackOverflow*.

- Pregunta (El usuario plantea un problema):
  - Tiene un titulo y un cuerpo
  - Puede ser votada (Positivo o Negativo)
  - Tiene un Autor
  - Tiene una fecha de creacion
- Respuestas (Los usuarios proponen soluciones):
  - Solo tienen cuerpo
  - Pueden ser votadas (Positivo o Negativo)
  - Tienen un autor
  - Siempre tienen una única pregunta asociada
  - Tienen una fecha de creacion
  - Otros usuarios con rol "Discusion" podrán valorar mediante comentarios si es útil o no.
- Comentario (Valoracion de una respuesta)
  - Solo tienen cuerpo y una mayor restriccion de longitud
  - Tienen asociado una valoracion sobre la respuesta *positiva, negativa o neutra*
  - Se mostrará la fecha de creacion y su autor
  - Tendran un tamñano mas reducido en pantalla
  - Se sombrearan según la valoracion
  - Podran ser votados para resaltar los mas útiles
 
### 2. Memoria entrega 3

Para esta última entrega, aunque nos lleve más trabajo, hemos decidido reorganizar la práctica prácticamente desde 0, ya que todos coincidíamos en que no entendíamos muy bien las decisiones de diseño anteriormente tomadas y, tras consensuarlas, hemos decidido realizarla como comentamos a continuación. 

En lo que sí que seguimos de acuerdo fue en la organización del trabajo, en continuar trabajando cada uno en una rama ya que de esta forma creemos que trabajamos bien.
Inicialmente, pensamos en una arquitectura de 4 capas (lógica, datos, presentación y servicios), sin embargo, finalmente, hemos considerado que con 3 capas será suficiente para cumplir con los principios SOLID.

Además, eliminamos “Elemento” de la BBDD, el cual comprendía elementos comunes de pregunta, respuesta, voto y comentario.

La base de datos final puede verse dentro del apartado “diagramaBBDD”, ha sido planteada como relacional y trabajaremos con SQLite.

Además, dentro de esa carpeta hemos añadido algunos diagramas que realizamos inicialmente sobre el funcionamiento de la página.

Lo primero que hicimos fue distribuir el trabajo del que se ocuparían las capas, ya que anteriormente no respetábamos el principio “Single Responsability” al no separar en algunas de ellas las responsabilidades. De esta forma, lo estamos cumpliendo. 

Por otro lado, la arquitectura multicapa proporciona ciertas ventajas que nos interesan. Como la coherencia de las clases que creamos y el encapsulamiento. Sin embargo, en la realización del proyecto hemos notada la gran desventaja de cambios en cascada, ya que, por ejemplo, al corregir alguna función en la capa de datos, hemos tenido que realizar cambios en todas las capas, lo que resulta tedioso para el programador.

Este diseño se puede asemejar a la arquitectura de tres capas. Ya que tenemos una capa para la presentación, una para el origen de datos y otra para la lógica (en nuestro caso la llamamos servicio). A continuación, las describiremos.

  1. Capa de datos: es la encargada de almacenar todos los datos.
  - En el frontend:
 	 - Aquí vamos a realizar la conexión del frontend con el backend. Esto se va a realizar mediante el backend service a modo de “fachada” puesto que nuestro 		objetivo es desacoplar el frontend del backend haciendo que este funcione sin conocer la informacion del backend. De esta forma, cuando se realizan las 		solicitudes HTTP desde el frontend, mediante este patrón se traducirá la respuesta del backend al formato esperado por el frontend.
		Facilitando su uso de esta forma, al tener una interfaz unificada de alto nivel.
  -En el backend: 
	  - Hemos definido distintos ficheros siguiendo el diagrama de datos creado. En esta capa definimos las tablas, las relaciones y ciertos servicios de datos, 		con los cuales funciona la capa de servicios. 
	  Hemos creado distintas clases para las distintas funcionalidades, así como tantas clases como elementos existen en los requisitos, de forma que conseguimos 		un sistema desacoplado. 
	  - En esta parte podremos encontrar las clases para las preguntas, respuestas, comentarios y reportes.
  2. Capa de presentación: es la encargada de realizar las operaciones comunicándose con la capa de servicios.
  	- En el frontend:
	  - Aquí podremos encontrar todos los endpoints, que son las “direcciones” a las que se van a enviar las peticiones. A estos los llamaremos desde el 		dms2223frontend para realizar los “GET” y los “POST” correspondientes.
  	- En el backend:
	  - Hemos creado los distintos ficheros para comentario, pregunta, respuesta etc… y en cada uno de ellos se han definido los métodos necesarios con los que se 		comunicará con la capa de servicio. Además, devolverá las respuestas HTTP correspondientes.
  3. Capa de servicios: es la encargada de comunicar la base de datos con la API REST. Y Para estos dos últimos, hemos decidido dividirlos en comentario y respuesta (y adicionalmente pregunta para reporte) por simplicidad.
 	- En el backend, hemos realizado los métodos getters y setters para:
	1. Comentarios
	2. Preguntas 
	3. Respuesta
	4. Reporte
	5. Votos
	
	
Se ha usado el dms2223auth proporcionado por el profesor para realizar todas las autenticaciones necesarias, además de como ayuda para poder entender ciertas partes del código.

También hemos utilizado el dms2223common para realizar la unión del frontend con el backend, ya que desde el backend obtendremos los diccionarios de datos y, mediante el response data del common, lo comunicaremos con el frontend.

Tras haber realizado el backend comprobamos que este funcionara con el Swagger, ya que debíamos arreglar el frontend.
Los pasos para realizar la comprobación en el Swagger son:
1. Ir a http://localhost:8080/login
2. Inspeccionar elemento - Network
3. Introducir usuario y contraseña (admin, admin)
4. En Network seleccionar "login" y copiar el Set Cookie de Request Header
5. Ir a http://localhost:4000/api/v1/ui
6. Authorize:
- 1234
- admin, admin
- Pegar el Set Cookie
7. Seleccionar sesion POST:
- Try it out
- Execute
- Ir a Code 200
- Copiar Response body
- 8. Ir a http://localhost:5000/api/v1/ui
Authorize:
- 1234
- Pegar Response body	
9. Selecionamos la operación que deseemos realizar:
- Try it out
- Execute
- Comprobar que funciona correctamente.

#### 3. Comprobación del funcionamiento de la base de datos
La comprobación de la base de datos se ha realizado de la siguiente forma: en la carpeta dms2223backend/bin/dms2223backend se han creado un fichero: dms2223backend-crear-ejemplo

En él, la idea principal para testear fue:
  1. Crear una nueva sesión de la base de datos.
  2. Crear usuarios, votos, preguntas, respuestas, comentaros, feedbacks y reportes de ejemplo con las estructuras adecuadas.
  3. Añadir estos elementos a la sesión anteriormente creada.
  4. Realizar commit de esta sesión.
  5. Cerrar la sesión.
 
### 4. Linea futura de trabajo
Nuestra línea de futuro consistirá en un servicio básico de mensajería entre usuarios dentro de la plataforma.

Desde el perfil del usuario, buscando el nombre de la persona deseada, podremos pulsar el botón “enviar mensaje”.

El usuario que lo reciba podrá, desde su buzón de entrada (dentro de su perfil de usuario también) abrir este mensaje, que se encontrará ubicado dentro del apartado “recibidos”.

El usuario emisor también podrá ver los mensajes que ha enviado en el apartado de "enviados".
Adicionalmente, los mensajes podrán clasificarse en leídos, no leídos, enviados, etc. Para esto, dentro de la base de datos, necesitamos un campo con el tipo de mensaje (enviado, recibido…) y posteriormente,  utilizaríamos un filtro para mostrar solo los “leídos”, “enviados”, etc en función de la opción seleccionada por el usuario.

Tal y como hemos dejado preparado el diseño, la forma en que se implementaría es la siguiente:

En el frontend habrá que diseñar los .html correspondientes con la información que se mostrará por pantalla, así como crear los botones necesarios.
Una vez pulsado ese botón, en las macros se definirá toda la lógica.

Con la autenticación, deberemos de asegurarnos de que solo los usuarios autorizados pueden enviar y recibir mensajes, esto lo haremos a nivel de código, comprobando que si el usuario no tiene acceso, se lance una excepción.

Además, habrá que almacenar los mensajes en la base de datos, para ello dentro del diseño habrá que añadir una clase “Mensajes” con un atributo id de usuario, que, como su propio nombre indica, coincidirá con el id del usuario.

Para que los usuarios puedan recibir mensajes en tiempo real, en lugar de tener que actualizar manualmente la página, implementaríamos WebSockets. 
WebSockets es una tecnología que permite la comunicación en tiempo real entre el cliente y el servidor a través de un canal de comunicación bidireccional y persistente. Esto significa que, una vez establecido el canal de comunicación, ambos extremos (cliente y servidor) pueden enviar y recibir datos en cualquier momento sin necesidad de realizar una nueva solicitud HTTP.

Para utilizar WebSockets en nuestra práctica, haríamos los siguientes pasos:
1. En la parte del frontend, crearíamos una instancia de la clase WebSocket y le proporcionaríamos la dirección del servidor al que queremos conectarnos. 
2. Una vez creada la instancia, configuraríamos los manejadores de eventos para los diferentes tipos de eventos que pudieran ocurrir durante la comunicación.
3. En la parte del backend, utilizaríamos un framework que permita trabajar con WebSockets. Se suelen usar Socket.IO y ws.
4. En el backend también crearíamos una instancia de la clase WebSocketServer y proporcionaríamos un manejador de eventos para el evento connection, que se activará cuando un nuevo cliente se conecte al servidor.
5. Una vez establecido el canal de comunicación, utilizaríamos métodos como send() y close() para enviar mensajes y cerrar la conexión desde cualquiera de los extremos (cliente o servidor).
6. 
Aquí, se nos ha ocurrido también implementar también la opción de “deshacer” un mensaje escrito, para lo que podríamos utilizar un patrón comando ya que este, como indica su propia intención, “Encapsula una petición como un objeto, permitiendo parametrizar clientes con diferentes peticiones, crear colas o registros de peticiones, o soportar operaciones que se pueden deshacer.”
Además del iterador para recorrer toda la lista de mensajes enviados, recibidos… secuencialmente.


### 5. Guía de usuario
Aunque, por falta de tiempo, no hemos podido terminar el trabajo, tenemos las ideas claras sobre cómo debería de ser el funcionamiento de la página web, por ello, en la carpeta GuiaUsuario, se pueden consultar esta.

Nos hubiera gustado poder poner capturas de pantalla sobre su funcionamiento, sin embargo, no nos ha dado tiempo por haber realizado prácticamente desde cero esta práctia.  

### 6. Consideraciones de para el desarrollo
#### 6.1 Docker
Por su simplicidad se han decidido modificar los ficheros de instalacion e inicio y asi permitir el desarrollo sin necesiadad de reinicios.
Se ha asumido que los desarrolladores actuales han instalado las imagenes, por lo que se ha comentado las lineas de *"/practica-dms-2022-2023/components/dms2223auth/bin/dms2223auth-create-admin"* para que no se intente volver a crear el usuario admin.
Si se requiriese reinstalar la maquina habria que desomentarlas o no sera posible loguearse en la aplicacion.

Ademas para permitir la compatibilidad con WSL2 se ha editado *" practica-dms-2022-2023/docker/config/dev.yml" liena 33* para enlazar el puerto 8080 de Docker con el 8080 de Windows.
#### 4.2 Modo debug
Para agilizar el desarrollo se ha configurado Jinja/Flask para actualizarsa cada vez que se produce un cambio en el frontend, asi no sera necesario reiniciar el servicio o la maquina docker cada vez que haga un cambio a la web. 
Para ello se ha modificado:

- *practica-dms-2022-2023/components/dms2223frontend/install.sh*: Se ha comentado la eliminacion del directorio temporal, es posible que requiera ser descomentado para nuevas instalacions.
- *practica-dms-2022-2023/components/dms2223frontend/bin/dms2223frontend*: Se ha añadido:
```
app.config["TESTING"] = True
app.testing=True
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)
```
Esto permite la recarga automatica de templates y codigo de las peticiones del mismo archivo. 

