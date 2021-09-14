import requests
from .validators import validateURL
from .auth_unit import AuthUnit


class DataManager:
    """
    Class Description
    """
    storage_ip: str
    storage_port: str
    send_users_url: str
    get_users_url: str
    mark_unused_users_url: str
    auth_unit: AuthUnit

    def __init__(
        self,
        storage_ip: str = None,
        storage_port: str = None,
        send_users_url: str = None,
        get_users_url: str = None,
        mark_unused_users_url: str = None,
        auth_unit: AuthUnit = None,
    ):
        self.storage_ip = storage_ip
        self.storage_port = storage_port
        self.send_users_url = validateURL(send_users_url)
        self.get_users_url = validateURL(get_users_url)
        self.mark_unused_users_url = validateURL(mark_unused_users_url)
        if self.storage_ip is None and self.storage_port is None:
            raise ValueError("storage_ip and storage_port cannot be None")
        self.auth_unit = auth_unit

    def sendUsers(self, users: list):
        url = f"http://{self.storage_ip}:{self.storage_port}{self.send_users_url}"
        response = requests.post(
            url, json=users, headers=self.auth_unit.getAuthHeaders())

    def getUsers(self, **kwargs):
        url = f"http://{self.storage_ip}:{self.storage_port}{self.get_users_url}"
        payload = kwargs
        response = requests.get(url, params=payload,
                                headers=self.auth_unit.getAuthHeaders())
        return response.json()

    def markUnusedUsers(self, users: list):
        url = f"https://{self.storage_ip}:{self.storage_port}{self.mark_unused_users_url}"
        response = requests.put(
            url, json=users, headers=self.auth_unit.getAuthHeaders())
