from datetime import datetime


class Elemento:
    """
    Elemento base, contiene la estructura común de los nodos de la aplicacion Pregunta-Comentario
    Args:
        votos_positivos (Arr votos): Votos positivos que ha recibido el elemento
        votos_negativos (Arr votos): Votos positivos que ha recibido el elemento
        votos_neutros (Arr votos): Votos positivos que ha recibido el elemento
        autor (Usuario): el usuario que lo ha creado 
    
    Attributes:
        fecha (datetime): Fecha de creacion, se genrea automaticamente
    """
    def __init__(self,id_preg,fecha,votos_positivos,votos_negativos,votos_neutros,autor) -> None:
        self.id = id_preg
        self.fecha_creacion = fecha
        self.votos_positivos = votos_positivos
        self.votos_negativos = votos_negativos
        self.votos_neutros = votos_neutros
        self.autor = autor

         