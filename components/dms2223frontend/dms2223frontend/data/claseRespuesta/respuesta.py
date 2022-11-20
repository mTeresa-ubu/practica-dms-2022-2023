from datetime import datetime

class Respuesta(Pregunta):
    def __init__(self, contenidoRespuesta,id_respuesta,fecha,autor) -> None:
        Pregunta.__init__(self,id_respuesta,fecha,autor)
        self.contenidoRespuesta = contenido