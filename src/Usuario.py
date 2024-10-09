#import AgendaDeServicos from AgendaDeServicos
import os
from dotenv import load_dotenv

load_dotenv()

google_client_id = os.getenv('GOOGLE_CLIENT_ID')
google_client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
google_token_uri = os.getenv('GOOGLE_TOKEN_URI')
google_auth_uri = os.getenv('GOOGLE_AUTH_URI')
google_cert_url = os.getenv('GOOGLE_AUTH_PROVIDER_CERT_URL')
google_redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

flow = InstalledAppFlow.from_client_config({
    "installed": {
        "client_id": google_client_id,
        "client_secret": google_client_secret,
        "auth_uri": google_auth_uri,
        "token_uri": google_token_uri,
        "auth_provider_x509_cert_url": google_cert_url,
        "redirect_uris": [google_redirect_uri]
    }
}, SCOPES)

creds = flow.run_local_server(port=0)

class Usuario: 
    def __init__(self, userID, nome, email, cep, rua, numeroDaResidencia, 
                 disponibilidadeHorario, disponibilidadeLocal ):
        
        self.__userID = userID
        #self.__servicos = AgendaDeServicos()
        self.__nome = nome
        self.__email = email
        self.__cep = cep 
        self.__rua = rua
        self.__numeroDaResidencia = numeroDaResidencia
        self.__disponibilidadeHorario = disponibilidadeHorario
        self.__disponibilidadeLocal = disponibilidadeLocal

        def cadastrarUsuario(self, nome, email, cep, rua, numeroDaResidencia, disponibilidadeHorario, disponibilidadeLocal ):
            pass

        def logarUsuario(self):
            pass

        def excluirUsuario(self):
            pass

        def editarUsuario(self):
            pass


        