""" BackendConfiguration class module.
"""

from typing import Dict
from dms2223common.data.config import ServiceConfiguration

class BackendConfiguration(ServiceConfiguration):
    """ Class responsible of storing a backend authentication service configuration.
    """

    def _component_name(self) -> str:
        """ The component name, to categorize the default config path.

        Returns:
            - str: A string identifying the component which will categorize the configuration.
        """

        return 'dms2223backend'

    def __init__(self):
        """ Initialization/constructor method.
        """

        ServiceConfiguration.__init__(self)

        self.set_db_connection_string('sqlite:////tmp/dms2223backend.sqlite3.db')
        self.set_service_host('127.0.0.1')
        self.set_service_port(5000)
        self.set_debug_flag(True)
        #self.set_password_salt('Cambiar')
        #self.set_jws_secret('Cambiar tambien')
        #self.set_jws_ttl(3600)
        #self.set_authorized_api_keys(["1234"]) # Hardcodeado
        self.set_authorized_api_keys([])
        self.set_auth_service({
            'host': '172.10.1.10',
            #'host': '127.0.0.1',
            'port': 4000,
            'apikey_secret': 'This should be the frontend API key'
        })
        
   
    def _set_values(self, values: Dict) -> None:
        """Sets/merges a collection of configuration values.

        Args:
            - values (Dict): A dictionary of configuration values.
        """
        ServiceConfiguration._set_values(self, values)

        if 'db_connection_string' in values:
            self.set_db_connection_string(values['db_connection_string'])
        if 'auth_service' in values: #Añadido 19/12/2022
            self.set_auth_service(values['auth_service'])
        # if 'salt' in values:
        #     self.set_password_salt(values['salt'])
        # if 'jws_secret' in values:
        #     self.set_jws_secret(values['jws_secret'])
        # if 'jws_ttl' in values:
        #     self.set_jws_ttl(values['jws_ttl'])

    def set_db_connection_string(self, db_connection_string: str) -> None:
        """ Sets the db_connection_string configuration value.

        Args:
            - db_connection_string: A string with the configuration value.

        Raises:
            - ValueError: If validation is not passed.
        """
        self._values['db_connection_string'] = str(db_connection_string)

    def get_db_connection_string(self) -> str:
        """ Gets the db_connection_string configuration value.

        Returns:
            - str: A string with the value of db_connection_string.
        """

        return str(self._values['db_connection_string'])

    # def set_password_salt(self, salt: str) -> None:
    #     """ Sets the password salt configuration value.

    #     Args:
    #         - salt: A string with the configuration value.

    #     Raises:
    #         - ValueError: If validation is not passed.
    #     """
    #     self._values['salt'] = str(salt)

    # def get_password_salt(self) -> str:
    #     """ Gets the password salt configuration value.

    #     Returns:
    #         - str: A string with the value of salt.
    #     """

    #     return str(self._values['salt'])

    # def set_jws_secret(self, secret: str) -> None:
    #     """ Sets the JWS secret key configuration value.

    #     Args:
    #         - secret: A string with the configuration value.

    #     Raises:
    #         - ValueError: If validation is not passed.
    #     """
    #     self._values['jws_secret'] = str(secret)

    # def get_jws_secret(self) -> str:
    #     """ Gets the JWS secret key configuration value.

    #     Returns:
    #         - str: A string with the value of jws_secret.
    #     """

    #     return str(self._values['jws_secret'])

    # def set_jws_ttl(self, ttl: int) -> None:
    #     """ Sets the jws_ttl configuration value.

    #     Args:
    #         - ttl: An integer with the configuration value.

    #     Raises:
    #         - ValueError: If validation is not passed.
    #     """
    #     self._values['jws_ttl'] = int(ttl)

    # def get_jws_ttl(self) -> int:
    #     """ Gets the jws_ttl configuration value.

    #     Returns:
    #         - int: An integer with the value of jws_ttl.
    #     """

    #     return int(self._values['jws_ttl'])

    def set_auth_service(self, auth_service: Dict) -> None:
        """Sets the connection parameters for the authentication service.

        Args:
            auth_service (Dict): Parameters to connect to the authentication service.

        Raises:
            - ValueError: If validation is not passed.
        """
        self._values['auth_service'] = auth_service
    
    def get_auth_service(self) -> Dict:
        """ Gets the authentication service configuration value.

        Returns:
            - Dict: A dictionary with the value of auth_service.
        """

        return self._values['auth_service']

    # def set_backend_service(self, backend_service: Dict) -> None:
    #     """Sets the connection parameters for the backend service.

    #     Args:
    #         backend_service (Dict): Parameters to connect to the backend service.

    #     Raises:
    #         - ValueError: If validation is not passed.
    #     """
    #     self._values['backend_service'] = backend_service

    # def get_backend_service(self) -> Dict:
    #     """ Gets the backend service configuration value.

    #     Returns:
    #         - Dict: A dictionary with the value of backend_service.
    #     """

    #     return self._values['backend_service']