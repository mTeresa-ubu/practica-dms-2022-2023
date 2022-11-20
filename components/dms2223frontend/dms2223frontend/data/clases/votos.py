"""
Por favor primero subir un diseño, luego se programa
"""


class Voto():
    def __init__(self, idPregunta):
        self.idPregunta = idPregunta

    def voteUp(self):
        NotImplemented
        #AQUI VA LA LLAMADA A LA BBDD QUE SUMA UN VOTO POSITIVO

    def unvoteUp(self):
        NotImplemented
        #AQUI VA LA LLAMADA A LA BBDD QUE RESTA UN VOTO POSITIVO

    def voteDown(self):
        NotImplemented
        #AQUI VA LA LLAMADA A LA BBDD QUE SUMA UN VOTO NEGATIVO

    def unvoteDown(self):
        NotImplemented
        #AQUI VA LA LLAMADA A LA BBDD QUE RESTA UN VOTO NEGATIVO