""" BackendService class module.
"""

import requests
from dms2223common.data import Role
from dms2223common.data.rest import ResponseData


class BackendService():
    """ REST client to connect to the backend service.
    """

    def __init__(self,
        host: str, port: int,
        api_base_path: str = '/api/v1',
        apikey_header: str = 'X-ApiKey-Backend',
        apikey_secret: str = ''
        ):
        """ Constructor method.

        Initializes the client.

        Args:
            - host (str): The backend service host string.
            - port (int): The backend service port number.
            - api_base_path (str): The base path that is prepended to every request's path.
            - apikey_header (str): Name of the header with the API key that identifies this client.
            - apikey_secret (str): The API key that identifies this client.
        """
        self.__host: str = host
        self.__port: int = port
        self.__api_base_path: str = api_base_path
        self.__apikey_header: str = apikey_header
        self.__apikey_secret: str = apikey_secret

    def __base_url(self) -> str:
        return f'http://{self.__host}:{self.__port}{self.__api_base_path}'

    def crear_comentario(self, token, autor, body, aid, sentiment):
        response_data: ResponseData = ResponseData()
        response: requests.Response = requests.post(
            self.__base_url() + f'/answers/{aid}/comments',
            json = {
                'autor': autor,
                'body': body,
                'aid': aid,
                'sentiment': sentiment
            },
            headers= {
                'Authorization': f'Bearer {token}',
                self.__apikey_header: self.__apikey_secret
            },
            timeout=60
        )
        response_data.set_successful(response.ok)
        if response_data.is_successful():
            response_data.set_content(response.json())
        else:
            response_data.add_message(response.content.decode('ascii'))
        return response_data

    # def create_preg(self, body:str, token, title, username):
    #     response_data: ResponseData = ResponseData()
    #     response: requests.Response = requests.post(
    #         self.__base_url() + '/questions',
    #         json={
    #             'title': title,
    #             'body': body
    #         },
    #         headers={
    #             'Authorization': f'Bearer {token}',
    #             self.__apikey_header: self.__apikey_secret
    #         },
    #         timeout=60
    #     )
    #     response_data.set_successful(response.ok)
    #     if response_data.is_successful():
    #         response_data.set_content(response.json())
    #     else:
    #         response_data.add_message(response.content.decode('ascii'))
    #     return response_data
