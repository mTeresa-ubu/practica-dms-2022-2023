
from orm import Schema
from orm.results import User, UserSession
from dms2223backend.data.db import Elemento, Reporte, Usuario, Voto, Comentario, Respuesta, Pregunta, Feedback
from dms2223backend.data.db.declarative_base import Session, engine, Base

if __name__ =='__main__':

    Base.metadata.create_all(engine) #Creamos BBDD

    session= Session() #Abrimos la sesión

    session.add(elemento1) #Guardamos elemento
    session.commit() #Commit

    session.close() #Cerramos la sesión
    
    