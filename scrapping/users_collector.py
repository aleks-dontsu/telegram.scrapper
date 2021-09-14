from .interfaces import Collecting, Controlled
from .datamanager import DataManager
from .credentials import CredentialsPool

from threading import Thread


class UsersCollector(Controlled, Collecting):
    """
    Abstraction. You sould never create instance of this class. It does'n
    inherits from abc.ABC only to avoid messing with metaclasses.
    (https://stackoverflow.com/questions/28799089/python-abc-multiple-inheritance)
    """

    def __init__(self, credentials_pool: CredentialsPool = None, data_manager: DataManager = None):
        Controlled.__init__(self)
        Collecting.__init__(

            self, credentials_pool=credentials_pool, data_manager=data_manager)

    def main_collection_function(self, *args, **kwargs):
        """
        Should be overriden
        """
        raise NotImplementedError

    def main_collecting_loop(self, *args, **kwargs):
        while self.active:
            self.main_collection_function(*args, **kwargs)

    def start(self, *args, **kwargs):
        self.run()
        collecting_thread = Thread(
            target=self.main_collecting_loop,
            args=args,
            kwargs=kwargs,
            name="main_collecting_loops thread",
        )
        collecting_thread.start()

    def getStatus(self):
        return {
            "settings": self.settings,
            "search_filter": self.search_filter,
            "is_active": self.isActive(),
            "is_paused": self.isPaused(),
        }
