### Guia de usuario

En nuestro caso hemos decidido trabajar en Windows, por lo que tuvimos que:
- Instalar WSL y actualizar a WSL 2.
- Descargar una consola de Ubuntu.
- Instalar Docker:
	- Primero de todo descargar el ejecutable "Docker Desktop Installer.exe" y ejecutarlo.
		- Se puede descargar en el siguiente enlace: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
	- En la instalación del programa seleccionar usar WSL 2 en vez de Hyper-V.
	- Finalizar la instalación del programa.
	- Abrir el programa "Docker Desktop".
	- Comprobar que en Configuración > General, este seleccionada la siguiente opción:
		https://github.com/mTeresa-ubu/practica-dms-2022-2023/tree/roberGuiaUsuario/Imagenes/docker1.png
	- Y comprobar que en Configuración > Resources > WSL Integration, esten selecionadas las dos opciones que hay:
		https://github.com/mTeresa-ubu/practica-dms-2022-2023/tree/roberGuiaUsuario/Imagenes/docker2.png
- Descargar el programa Visual Studio Code, para trabajar comodamente.
- Realizar un clone del repositorio con el comando "git clone" (desde terminal).
- Por último, comenzar a trabajar cada uno desde nuestra rama, realizando los commits necesarios y las pull request para ir pasando los avances a la rama principal “main”.
Nos gustaría poder adjuntar muchas más fotos pero, a pesar del esfuerzo, no hemos sido capaces de conseguir que la aplicación funcione a la perfección por falta de tiempo, por lo que en algunos de los pasos, aunque no dispongan de su foto correspondiente, trataremos de explicar lo que se debería de poder hacer si funcionara correctamente.
1.	Lo primero que debemos hacer es acceder a la página web http://127.0.0.1:8080
2.	Pulsando el botón de “login” e introduciendo unas credenciales válidas iniciaremos sesión. (en nuestro caso las credenciales admin admin están por defecto disponibles)
	https://github.com/mTeresa-ubu/practica-dms-2022-2023/tree/roberGuiaUsuario/Imagenes/login.png
3.	Una vez en la página de inicio, podemos visualizar las preguntas creadas recientemente.
4.	En la parte superior de la página, podemos movernos de la página "/home" a la pagina "/admin" y viciversa.
5.	Podemos crear una pregunta pulsando el botón ”Crear pregunta”, el cual nos redigirá a una página donde introduciremos el título y el cuerpo de la pregunta, se podrá enviar dicha pregunta y también tenemos la posibilidad de vaciar los campos que hemos introducido.
6.	También podemos seleccionar cualquier pregunta creada y dentro de dicha pregunta se podra responder y/o reportar la pregunta.
7.	Dentro de las respuestas de las preguntas, podremos comentarlas y se podrán dar un voto positivo o negativo, y al igual que en preguntas, podremos reportar las respuestas y los comentarios de la respuesta.
