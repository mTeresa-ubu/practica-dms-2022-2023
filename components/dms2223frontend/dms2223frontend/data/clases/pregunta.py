from dms2223frontend.data.clases.elemento import Elemento
from datetime import datetime

class Pregunta(Elemento):
    def __init__(self, contenido,id_preg,fecha,votos_positivos,votos_negativos,votos_neutros,autor,titulo) -> None:
        Elemento.__init__(self,id_preg,fecha,votos_positivos,votos_negativos,votos_neutros,autor)
        self.contenidoPregunta = contenido
        self.tituloPregunta = titulo
