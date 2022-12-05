from orm import Schema
from orm.results import User, UserSession
from dms2223backend.data.db import Elemento, Reporte, Usuario, Voto, Comentario, Respuesta, Pregunta, Feedback
from dms2223backend.data.db.declarative_base import Session, engine, Base

if __name__ =='__main__':

    Base.metadata.create_all(engine) #Creamos BBDD

    session= Session() #Abrimos la sesión

    #Añadimos datos a la bbdd
    usuario1 = Usuario(1,"María")
    usuario2 = Usuario(2,"Álvar")
    session.add(usuario1) #Guardamos datos
    session.add(usuario2)
    session.commit() #Commit

    voto1 = Voto(1,1,1,positivo)
    voto2 = Voto(2,2,1,negativo)
    session.add(voto1) 
    session.add(voto2)
    session.commit()

    reporte1 = Reporte(1,1,2,3, "No es correcto","No está de acuerdo","Se rechaza",rechazado)
    reporte2 = Reporte(2,1,2,4, "Es correcto","De acuerdo","Se acepta", aceptado)
    session.add(reporte1) 
    session.add(reporte2)
    session.commit()

    feedback1 = Feedback(1, verde, "Feedback de ejemplo 1" )
    feedback2 = Feedback(2,rojo, "Feedback de ejemplo 2" )
    session.add(feedback1) 
    session.add(feedback2)
    session.commit()

    pregunta1 = Pregunta(5,"Titulo1")
    pregunta2 = Pregunta(6,"Titulo2")
    session.add(pregunta1) 
    session.add(pregunta2)
    session.commit()

    respuesta1 = Respuesta(1,5)
    respuesta2 = Respuesta(1,6)
    session.add(respuesta1) 
    session.add(respuesta2)
    session.commit()

    comentario1 = Comentario(1,1,2)
    comentario2 = Comentario(2,1,1)
    session.add(comentario1) 
    session.add(comentario2)
    session.commit()

    session.commit()
    session.close() #Cerramos la sesión
    
    