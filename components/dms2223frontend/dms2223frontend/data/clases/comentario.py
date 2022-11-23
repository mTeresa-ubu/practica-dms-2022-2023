from dms2223frontend.data.clases.elemento import Elemento
from datetime import datetime

class Comentario(Elemento):
    def __init__(self, 
        id_elemento:str,
        id_respuesta:str,
        id_comentario:str,
        contenido_comentario:str,
        fecha:datetime,
        votos_positivos:int,
        votos_negativos:int,
        autor:str,
        feedback:str,
        color_class:str
        ) -> None:

        Elemento.__init__(self,id_elemento,fecha,votos_positivos,votos_negativos,autor)
        self.id_respuesta = id_respuesta
        self.id_comentario = id_comentario
        self.contenido_comentario = contenido_comentario
        self.feedback=feedback
        self.color_class=color_class