"""
This module is responsible for information about emulated users.
"""
import json


class Proxy:
    user: str
    password: str
    ip: str
    port: str

    def __init__(
        self,
        user: str = None,
        password: str = None,
        ip: str = None,
        port: str = None,
        str_repr: str = None
    ):
        """
        You must pass either 4 arguments (user, password, ip, port)
        or a string representation (str_repr)   
        """
        if None in (user, password, ip, port):
            usr, adr = str_repr.split('@')
            self.user, self.password = usr.split(':')
            self.ip, self.port = adr.split(':')
        else:
            self.user = user
            self.password = password
            self.ip = ip
            self.port = port

    def __repr__(self) -> str:
        return f"{self.user}:{self.password}@{self.ip}:{self.port}"


class Credentials:
    user: str
    password: str
    proxy: Proxy
    cookies: dict
    headers: dict

    def __init__(self, user=None, password=None,
                 proxy=None, cookies=None, headers=None):
        if user is None:
            raise ValueError("user can not be None")
        if password is None:
            raise ValueError("password can not be None")

        self.user = user
        self.password = password
        self.setProxy(proxy)
        self.setCookies(cookies)
        self.setHeaders(headers)

    def setProxy(self, proxy):
        if proxy is None:
            self.proxy = None
        elif type(proxy) is dict:
            self.proxy = Proxy(**proxy)
        elif type(proxy) is str:
            self.proxy = Proxy(str_repr=proxy)

    def setCookies(self, cookies):
        if cookies is None:
            self.cookies = None
        elif type(cookies) is str:
            try:
                self.cookies = json.loads(cookies)
            except Exception as e:
                print(e)
                raise ValueError(
                    "String representation of cookies must be in JSON format!")
        elif type(cookies) is dict:
            self.cookies = cookies
        else:
            raise ValueError("cookies must be a None, dict or a JSON string")

    def setHeaders(self, headers):
        if headers is None:
            self.headers = None
        elif type(headers) is str:
            try:
                self.headers = json.loads(headers)
            except Exception as e:
                print(e)
                raise ValueError(
                    "String representation of headers must be in JSON format!")
        elif type(headers) is dict:
            self.headers = headers
        else:
            raise ValueError("headers must be a None, dict or a JSON string")

    def __str__(self) -> str:
        return f"user: {self.user}; password: {self.password}; proxy: {self.proxy}"\
            f" {'with cookies;' if self.cookies else ''} {'with headers;' if self.headers else ''}"


class CredentialsPool:
    """
    We use CredentialsPool to change users that social network sees. You should
    split requests between users to avoid getting banned.
    It's iterable. Be very carefull - iteration is cycled. (Is never raises
    StopIteration)
    """
    credentials_list: list
    curr_index: int

    def __init__(self, credentials_list: list = [], auth_unit=None):
        """
        Class Initialization Function. Gets called when the object is created

        Parameters
        ----------
        credentials_list_list (list) : Optional.
            You can pass credentials in format
            {
                "user": your_user_id,
                "password": your_user_password,
                [ optional ]"proxy": poxy_to_use_with_user,
                [ optional ]"cookies": cookies_to_use_with_user, (dictionary, None or JSON string)
                [ optional ]"headers": headers_to_use_with_user, (dictionary, None or JSON string)
            }
            or instances of Credentials class.
            value of "proxy" in dictionary must bu a dict in format
            {
                "user": your_user (str)
                "password": your_password (str)
                "ip": your_ip (str)
                "port": your_port (str)
            }
            or string in format "user:password@ip:port"
            or instance of Proxy class
        auth_unit=None: auth_unit.AuthUnit
        Raises
        ------
        ValueError
            If you passed credentials and some user has invalid field "user" or 
            "password" or hasn't one of this fields at all

        """
        self.credentials_list = []
        self.curr_index = 0
        for creds in credentials_list:
            if isinstance(creds, Credentials):
                self.credentials_list.append(creds)
            elif type(creds) is dict:
                self.credentials_list.append(Credentials(**creds))
            else:
                raise ValueError(
                    "credentials_list items must be dictionaries or instances of Credentials")

        self.auth_unit = auth_unit

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index >= len(self.credentials_list):
            self.curr_index = 0
        credentials = self.credentials_list[self.curr_index]
        self.curr_index += 1
        return credentials
