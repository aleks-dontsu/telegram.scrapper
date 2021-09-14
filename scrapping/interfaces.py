import abc
from .datamanager import DataManager
from .credentials import CredentialsPool


class Controlled():
    threads: list
    active: bool
    paused: bool
    settings: dict

    def __init__(self, settings={}):
        print("Controlled init")
        self.threads = []
        self.active = False
        self.paused = False
        self.aborted = False
        self.settings = settings

    def run(self):
        self.active = True
        self.aborted = False

    def stop(self): self.active = False

    def abort(self):
        self.aborted = True
        self.active = False

    def pause(self): self.paused = True

    def unpause(self): self.paused = False

    def setSettings(self, settings): self.settings = settings

    def isActive(self): return self.active

    def isPaused(self): return self.paused


class Collecting():
    credentials_pool: CredentialsPool
    data_manager: DataManager
    search_filter: dict

    def __init__(self, credentials_pool: CredentialsPool = None, data_manager: DataManager = None):
        print("Collecting init")
        self.credentials_pool = credentials_pool
        self.data_manager = data_manager
        self.search_filter = {}

    def setSearchFilter(self, search_filter):
        self.search_filter = search_filter
