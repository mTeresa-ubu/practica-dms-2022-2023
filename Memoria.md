# Memoria
## Entrega 1
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

#### 1.5 Respuesta
Para responder a una pregunta realizada por un usuario, se ha creado una macro, llamada respuesta y que, como es de esperar, contiene la respuesta a una pregunta realizada por un usuario.
En el fichero respuesta.html podemos encontrar:
  -En primer lugar, los imports tanto de la macro input como de los botones y del contenedor de respuestas creado.
  -Posteriormente, se visualizará "Respuesta" y, a continuación, el contenido concreto de la respuesta.
  -Una vez visualizado este, el usuario visualizará por pantalla las acciones que puede realizar. Estas son: Votar, responder, añadir un comentario, dar feedback(positivo, negativo o neutro) y, por último, reportar la respuesta.
  -Además, al final aparecerá el nombre del usuario que ha respondido junto con la fecha y la hora en la que lo hizo.
  Estos datos se sacarán del backend.
El acceso a la respuesta se realizará desde "/respuesta".
Cuando deseemos implementar esta macro, lo primero que debemos de realizar es un import de ella.
Y, cuando queramos ver el contenido de la respuesta lo llamaremos utilizando {{ respuesta.contenidoRespuesta }}.
Por si además se desea crear una nueva respuesta, se ha implementado un botón "Crear respuesta", que se visualizará despues del contenido de la respuesta.


#### 1.6 Respuesta (Votaciones)
Para llevar a cabo las votaciones de las preguntas y las respuestas se han creado dos macros correspondientes con los botones para votos positivos y para votos negativos. Dichas macros se encuentran en el fichero "buttons.html", obteniendo cada una de ellas características especiales como el color de fondo (verde en caso de voto positivo y rojo en caso de voto negativo) y el texto que contiene (vote Up en caso de voto positivo y vote Down en caso de voto negativo), tambien se realiza una llamada en cada caso al método correspondiente cuando es pulsado (voteUp() en caso de voto positivo y voteDown() en caso de voto negativo). Los metodos a los que se llaman cuando se pulsa el boton se encuentran en el fichero votos.py, en el que se ha creado la clase Voto con cuatro metodos posibles: El primero "voteUp" hará que se sume un punto positivo a los votos de la pregunta/respuesta. El segundo "unvoteUp" se llamará en caso de querer anular el punto positivo de la pregunta/respuesta en caso de haber sumado previamente dicho punto. El tercero "voteDown" hara que se sume un punto negativo a los votos de la pregunta/respuesta. Por ultimo, el cuarto "unvoteDown" se llamará en caso de querer anular el punto negativo de la pregunta/respuesta en caso de haber sumado previamente dicho punto. Adicionalmente, se ha creado un Endpoint para actualizar las votaciones de las preguntas/respuestas, quedando tambien reflejado en el frontend.


#### 1.7 Pregunta
  Para la realización de este apartado se han creado distintos macros que suplen las necesidades de os requisitos.
  
  En primer lugar tenemos los imports corresipondientes a los botones de votacion. Estos botones tienen unos métodos definidos que cambiaran los datos posteriormente.
  
  A continuación, hemos creado un titulo de pregunta que recibirá el titulo de la pregunta por parametro y lo mostrara en la página. Este método se ha preparado para que posteriormente en la implemntación del backend sea fácil de utilizar.

  Posteriormente, se han creado campos para el autor de la preunta y fecha de la realización de la misma. Este macro se ha realizado con el fin de que el sistema pase por parametro los datos necesarios(usuario y fecha) cuando el usuario envie la pregunta.

  Finalmente se han llamdo a las funciones de votacion(up y down) y se ha creado un macro para el cuerpo de la pregunta, que recibe como parametro la descripción que sera el cuerpo de la pregunta.

  La creación de estas macros van contenidas en una macro pregunta. Se ha planteado la posibilidad de no contenerlos en una macro superior, con el fin de reutilizar las macros de otra forma para la lista de preguntas pero hemos consensuado que es contraproducente. 


#### 1.8 Creaccion de preguntas

El usuario tendra la opcion de poder crear preguntas, para ello se ha creado un template (el cual extiende de "base.html") llamado crear_preguntas.html.
En este archivo encontramos los siguientes componentes:
  - Un import de la macro de los botones, en el cual agregamos "submit_button" y "reset_button", este ultimo se ha creado para poder vaciar los campos del formulario al crear la pregunta.
  - Un formulario con sus respectivos labels (Titulo de la pregunta y Detalles de la pregunta), inputs ("titulo" de tipo text, "detalles" de tipo textarea) y buttons (Enviar Pregunta y Vaciar Campos).
    - El boton "Enviar Pregunta" es de tipo "submit_button", su funcion sera gruardar: el nombre del usuario que ha realizado la pregunta, la fecha cuando se ha realizado la pregunta, el titulo de la pregunta y el detalle/descripcion de la pregunta.
    - El boton "Vaciar Campos" es de tipo "reset_button", su función es resetear (vaciar) los campos del formulario.
Para acceder a la creaccion de preguntas se hace desde "/crear_preguntas".


### 2. Diseño del backend
Durante todo el desarrollo del backend se han tenido en cuenta los principios SOLID vistos en clase, como al tratar de no repetir código, etc...

#### 2.1 Diseño de la base de datos
Una vez comenzamos con el backend, lo primero que realizamos fue el diseño de la base de datos.
Para ello, identificamos los siguientes elementos:

    - Reporte
    - Usuario
    - Elemento
    - Voto
    - Comentario
    - Respuesta
    - Pregunta
    - Feedback
Lo importante de este diseño fue reconocer cuales son las claves primarias y foráneas y sus relaciones.
El diseño final, tras varias modificaciones es el siguiente:

![alt text](https://github.com/mTeresa-ubu/practica-dms-2022-2023/blob/diagramaBBDD/diagramaBBDD.jpeg?raw=true)

Por eso, para el diseño del backend, dentro de la carpeta dms2223backend/dms2223backend/data/db se han creado las correspondientes carpetas y ficheros:

    - Reporte
      - reporte.py
    - Usuario
      - usuario.py
    - Voto
      - voto.py
    - Elemento
      - elemento.py
      - comentario.py
      - respuesta.py
      - pregunta.py
    - Feedback
      - feedback.py

Y dentro de estos .py se han generado las clases que hemos visto en el diagrama de arriba.
*En todas estas carpetas se ha creado también su _init_.py, necesario para el buen funcionamiento.

#### 2.2 Comprobación del funcionamiento de la base de datos
La comprobación de la base de datos se ha realizado de la siguiente forma: en la carpeta dms2223backend/bin/dms2223backend se han creado dos ficheros: dms2223backend-crear-ejemplo y dms2223backend-mTeresa.

En ellos, la idea principal para testear fue:
  1. Crear una nueva sesión de la base de datos.
  2. Crear usuarios, votos, preguntas, respuestas, comentaros, feedbacks y reportes de ejemplo con las estructuras adecuadas.
  3. Añadir estos elementos a la sesión anteriormente creada.
  4. Realizar commit de esta sesión.
  5. Cerrar la sesión.

  De forma adicional, hemos impreso por pantalla todas las tablas creadas para comprobar que lo han hecho de la forma que queríamos.

#### 2.3 API para obtener comentario por id
Para realizar la API:
  - En la carpeta dms2223backend/dms2223backend/service se ha creado el fichero servicioComentario.py, donde se han implementado dos métodos, uno para obtener el comentario dado el id y, adicionalmente, otro para obtener todos los comentarios en una lista.
  -  En la carpeta dms2223backend/dms2223backend/data/resultsets se ha creado el fichero comentario_rset.py, donde, primero, se han incluido todos los atributos que tiene un comentario en la clase principal y, posteriormente, se ha creado otra clase con un método estático cuya finalidad es devolver una lista con los comentarios que se han generado en esa sesión de la base de datos.
#### 2.4 API para obtener pregunta por id
#### 2.5 API para la creación y obtención de respuestas
Para la realización de esta API se han seguido varios pasos:

    - En primer lugar se han creado las tablas y valores necesarios, en este caso se han usado las tablas de Elemento, la cual contiene la fecha de creación, el autor, el contenido(diferirá dependiendo del tipo de elemento), visibilidad(tendra dos valores, por defecto; True), y el identificador del elemento que se genera automáticamente. Por otro lado tenemos la tabla de Respuesta, esta tabla hereda los valores del Elemento e incluye el identificador de la pregunta a la que corresponde y el identificador porpio. 

    - A continuación, se ha creado una clase Respuestas ,creada en el archivo answerSets.py en dms2223backend/dms2223backend/data/resultsets, que servirá para obtener listas y diccionarios de estos valores con el fin de facilitar el uso del servicio y desacoplar el codigo.

    - Con los elementos anteriores creados y testados pasamos a crear la clase de servicio: ServicioRespusta. Esta clase contiene los siguientes métodos :

      -crea_Respuesta: Este método recibe ciertos parametros correspondientes a la tabla de respuesta y añade la respuesta a la base de datos.

      -obtenerRespuestasPorPregunta: Este méotdo recibe el identificador de una pregunta y encuentra las respuestas correspondientes a esa pregunta, añade las respuestas a un diccionario y devuelve el diccionario en cuestión.

      -ocultarRespuesta: cambia el atributo de visibilidad del elemento respuesta por el valor de visibilidad pasado por parametro.

    
    - Finalmente se ha creado el fichero que contiene las funciones que sirven de controlador para las operaciones que realiza el cliente. Este es el respuestaRest.py situado en dms2223backend/dms2223backend/presentation/rest. Aqui se han creado dos métodos: 

    -lista_Respuestas: Con el id_Pregunta pasado por parametro se llama a la función creada en el servicio y con la lista de diccionarios de vuelve se devuelve el estado HTTP correspondinte.

    -crea_respuesta: con los parametro pasados, correspondientes a los valores de la tabla de la base de datos, se llama al servicio y se devuelve el estado HTTP correspondiente.

#### 2.6 API para crear nueva pregunta
#### 2.7 API para crear nuevo comentario
#### 2.8 API para crear un reporte
Para la realización de esta API, ha sido necesario crear los siguientes ficheros:
  - En la carpeta dms2223backend/dms2223backend/service se ha creado el fichero servicioReportes.py, donde se ha implementado la clase ServicioReporte con los métodos: list_reportes para obtener una lista con todos los reportes, y create_reporte que crea un nuevo reporte y devuelve un diccionario con el reporte en cuestión.
  - En la carpeta dms2223backend/dms2223backend/data/resultsets se ha creado el fichero reporte_res.py, donde, primero, se han incluido todos los atributos que tiene un reporte en la clase principal y, posteriormente, se ha creado otra clase con un método estático cuya finalidad es devolver una lista con los reportes que se han generado en esa sesión de la base de datos.
  - En la carpeta dms2223backend/dms2223backend/presentation/rest se ha creado el fichero reportes.py, en el cual se ha generado el metodo list_reportes que devuelve una lista con los reportes existentes, y el metodo create_rep que recoge los datos de la peticion y los manda al servicio de reportes.
#### 2.9 API para votar
Para la realizacion de la API hemos construido tres archivos en tres rutas diferentes:

- votoElemento.py en la ruta: /practica-dms-2022-2023/components/dms2223backend/dms2223backend/data/resultsets/votoElemento.py
- votarCualquierElemento.py en la ruta: /practica-dms-2022-2023/components/dms2223backend/dms2223backend/service/votarCualquierElemento.py
- votos.py en la ruta: /practica-dms-2022-2023/components/dms2223backend/dms2223backend/presentation/rest/votos.py

En el archivo votarCualquierElemento.py se ha implementado la clase votosElemento con los métodos: 
- get_votos_positivos: para obtener el numero de votos de positivos del elemento pasando su id.
- get_votos_negativos: para obtener el numero de votos de negativos del elemento pasando su id.
- post_votos_positivos: para votar positivamente al elemento pasando su id.
- post_votos_negativos: para votar negativamente al elemento pasando su id.
	
En el archivo votoElemento.py, se han implementado dos clases:
- class Votos(): Se incluyen todos los atributos que tiene un voto.
- class VotosFuncs():Clase con un método estático cuya finalidad es devolver una lista con los votos que se han generado en esa sesión de la base de datos.
	
En el archivo votos.py se han implementado los metodos:
- post_votosPositivos_id: Envia un voto positivo al elemento pasando su id.
- post_votosNegativos_id: Envia un voto negativo al elemento pasando su id.
- get_votosPositivos_id: Devuelve el numero de votos positivos del elemento pasando su id.
- get_votosNegativos_id: Devuelve el numero de votos negativos del elemento pasando su id.
### 3. Consideraciones de para el desarrollo
#### 3.1 Docker
Por su simplicidad se han decidido modificar los ficheros de instalacion e inicio y asi permitir el desarrollo sin necesiadad de reinicios.
Se ha asumido que los desarrolladores actuales han instalado las imagenes, por lo que se ha comentado las lineas de *"/practica-dms-2022-2023/components/dms2223auth/bin/dms2223auth-create-admin"* para que no se intente volver a crear el usuario admin.
Si se requiriese reinstalar la maquina habria que desomentarlas o no sera posible loguearse en la aplicacion.

Ademas para permitir la compatibilidad con WSL2 se ha editado *" practica-dms-2022-2023/docker/config/dev.yml" liena 33* para enlazar el puerto 8080 de Docker con el 8080 de Windows.
#### 3.2 Modo debug
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
Es recomendable eliminar estas lineas en un futuro despliegue.
