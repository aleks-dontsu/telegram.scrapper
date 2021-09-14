import requests
import configparser


class AuthUnit:
    auth_token: str
    config: configparser.ConfigParser
    controllers_host: str

    def __init__(self, controllers_host):
        self.controllers_host = controllers_host
        self.config = configparser.ConfigParser()
        self.login()

    def login(self):
        self.config.read('scrppers_controller.conf')
        username = self.config['Scrappers Controllers User']['User']
        password = self.config['Scrappers Controllers User']['Password']
        payload = {
            "username": username,
            "password": password,
        }
        response = requests.post(
            f"http://{self.controllers_host}/api/auth/login", data=payload)
        if response.status_code == 200:
            self.auth_token = f"Token {response.json()['token']}"
        elif response.status_code == 400:
            # {'non_field_errors': ['Incorrect Credentials']}
            print(f"Error while tried to login:\n{response.text()}")
        else:
            print(f"Error tried to get status_code to {self.controllers_host}")

    def getAuthHeaders(self):
        return {"Authorization": self.auth_token}
