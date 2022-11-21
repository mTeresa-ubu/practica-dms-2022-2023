from datetime import datetime

class Elemento:
    """
    Elemento base, contiene la estructura común de los nodos de la aplicacion Pregunta-Comentario\n
    Args:
        votos_positivos (Arr votos): Votos positivos que ha recibido el elemento
        votos_negativos (Arr votos): Votos positivos que ha recibido el elemento
        votos_neutros (Arr votos): Votos positivos que ha recibido el elemento
        autor (Usuario): el usuario que lo ha creado 
    
    Attributes:
        fecha (datetime): Fecha de creacion, se genrea automaticamente
    """
    def __init__(self,
        iden,
        fecha,
        votos_positivos,
        votos_negativos,
        autor) -> None:

        self.id = iden
        self.fecha_creacion = fecha
        self.votos_positivos = votos_positivos
        self.votos_negativos = votos_negativos
        self.autor = autor

         