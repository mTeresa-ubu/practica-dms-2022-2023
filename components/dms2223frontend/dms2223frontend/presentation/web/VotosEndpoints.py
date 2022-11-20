from dms2223frontend.data.rest.authservice import AuthService
from components.dms2223frontend.dms2223frontend.data.clases.votos import Voto

#NECESITARIA IMPORTAR LA CLASE PREGUNTA PARA OBTENER EL ID DE LA PREGUNTA
class VotosEndpoints():
    @staticmethod
    def post_voto(auth_service: AuthService, idPregunta: int):
        #NO SE COMO IMPLEMENTAR ESTE METODO EXACTAMENTE --> PUES APRENDE
        return "Votacion actualizada"