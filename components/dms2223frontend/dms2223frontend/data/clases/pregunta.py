from dms2223frontend.data.clases.elemento import Elemento
from datetime import datetime

class Pregunta(Elemento):
    def __init__(self,
        contenido:str,
        id_preg:str,
        fecha:datetime,
        votos_positivos:int,
        votos_negativos:int,
        autor:str,
        titulo:str
        ) -> None:

        Elemento.__init__(self,id_preg,fecha,votos_positivos,votos_negativos,autor)
        self.contenidoPregunta = contenido
        self.tituloPregunta = titulo
