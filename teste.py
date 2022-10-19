import requests
import json


class ApiXcapital:

    def __init__(self):

        self.reqUrl = "https://xcapitalbank.herokuapp.com/api/v1/usuarios"

        self.headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        }


    def user_login_token(self):
        payload = { 
                "username": "Jonas@gmail.com", #self.username,
                "password": "123456" #self.email
                }

        response = requests.post(f'{self.reqUrl}/login', data=payload,  headers=self.headersList)

        print(response.status_code)
        
        if response.status_code == 200:
            print(response.json()["access_token"])
            return response.json()["access_token"]
        else:
            return 'Alguma credencial foi digitada incorretamente'


    def usuario_logado(self):
        header = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            'Authorization': f'Bearer {self.user_login_token()}'
        }
        
        payload = ""

        response = requests.request("GET", f'{self.reqUrl}/logado', data=payload,  headers=header)
        
        print(response.status_code)

        if response.status_code == 200:
            return response.json()
        else:
            return {}
        


if __name__ == "__main__":
    api = ApiXcapital()
    user = api.usuario_logado()

    print(user['nome'], user['sobrenome'])
    print(user['email'])
    print(user['eh_admin'])

