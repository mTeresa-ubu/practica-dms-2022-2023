from dms2223frontend.data.clases.elemento import Elemento
from datetime import datetime

class Respuesta(Elemento):
    def __init__(self,
        id_resp:str,
        id_preg:str,
        contenido:str,
        fecha:datetime,
        votos_positivos:int,
        votos_negativos:int,
        autor:str,
        num_comentarios:int
        ) -> None:
        
        Elemento.__init__(self,id_resp,fecha,votos_positivos,votos_negativos,autor)
        self.contenidoRespuesta = contenido
        self.num_comentarios=num_comentarios
        self.id_preg = id_preg
        self.num_comentarios = num_comentarios