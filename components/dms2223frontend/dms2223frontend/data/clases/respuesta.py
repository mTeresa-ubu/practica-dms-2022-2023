from dms2223frontend.data.clases.elemento import Elemento
from datetime import datetime

class Respuesta(Elemento):
    def __init__(self, contenido,id_preg,fecha,votos_positivos,votos_negativos,votos_neutros,autor) -> None:
        Elemento.__init__(self,id_preg,fecha,votos_positivos,votos_negativos,votos_neutros,autor)
        self.contenidoRespuesta = contenido