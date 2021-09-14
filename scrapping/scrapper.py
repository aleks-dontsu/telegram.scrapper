from .users_collector import UsersCollector
from .usersdata_collector import UsersDataCollector


class Scrapper:
    users_collector: UsersCollector
    usersdata_collector: UsersDataCollector

    def __init__(self, users_collector, usersdata_collector):
        self.users_collector = users_collector
        self.usersdata_collector = usersdata_collector
