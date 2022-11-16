from elemento import Elemento
from datetime import datetime

class Pregunta(Elemento):
    def __init__(self, contenido ,fecha:datetime,votos_positivos,votos_negativos,votos_neutros,autor) -> None:
        Elemento.__init__(self,fecha,votos_positivos,votos_negativos,votos_neutros,autor)
        self.contenidoPregunta = contenido
