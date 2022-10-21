# Requisitos para el proyecto de DMS

## Memoria
1. Formato **Markdown**
2. Se debe documentar la arquitectura
3. Justificacion de las decisiones de diseño (SOLID)
4. La última entrega debe recoger el trabajo futuro, pasos necesarios pero no implementarlo
   

## Entrega 1 - 13 Noviembre 2022 - 10pt
Ya tenemos :
- 🔑 Servicio de autenticación ( Está completo, no hay que tocarlo)
- ⚛ Servicio Backend (API) Organizado en *4 capas* pero es modificable
- ✨Fronted (Paginas y plantillas, web)

### Requisitos Funcionales:
1. Creacion de preguntas, respuestas y reportes
   1. [] Las preguntas tienen un **titulo** y un **cuerpo**
   2. [] Solo los usuarios con rol de **discusion** podra crear preguntas y responder a las existentes
   3. [] Las respuestas tienen un **feedback** positivo, negativo o neutro asociado sobre la respuesta
   4. [] Las preguntas y respuestas tienen **votos**
   5. [] Se puede **reportar** todo, con una razón asociada
   6. [] Todos los elementos anteriores tienen un **propietario**, el creador
   7. [] Todos los elementos tienen un **timestamp** de su creación
   
2. Moderacion
   1. [] Al usuario moderador le **llegan los reportes**
   2. [] Un reporte puede ser **pendiente o resuelto**
   3. [] Un reporte se puede declarar **rechazado o aceptado**
   4. [] Si se acepta el comentario y sus respuestas se **ocultan** permanentemente pero no se eliminan

3. Sesion
   1. [] Todos los usuarios **iniciaran sesion** al entrar en la aplicación
   2. [] Los distintios roles tienen **operaciones** distintas (interfaces distintas?)
   3. [] Los permisos **no son jerarquicos** (Ej.: Un moderardor no comenta)
   4. [] Boton de **cerrar sesión**

### Requisitos no funcionales:
1. Usar tipado estatico 🛑Penalizacion si no se usa en puntos clave🛑
2. Estilo correcto 7️⃣/🔟 Minimo
3. Participación de todo el grupo 🧑🏻🧑🏻🧑🏻🧑🏾👧🏻, según commits
4. Manuales, instalación y uso 📗


### Pendiente:
- [ ] Completar los **"TODO"** del codigo 
- [ ] Crear fronted estatico
- [ ] Cumplir los requisitos funcionales
- [ ] Cumplir los requisitos no funcionales
- [ ] Rellenar la memoria

## Entrega 2 - 4 Diciembre 2022 - 10pt
## Entrega 3 - 18 Diciembre 2022 - 20pt