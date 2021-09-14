import asyncio
from scrapping import CredentialsPool, DataManager, UsersDataCollector, datamanager
from .assistans import random_sleep
from .parser_groups import ParserGroups
from .parser_numbers import ParseNumbers


class TgSelector(UsersDataCollector):

    def __init__(self, credentials_pool: CredentialsPool = None, data_manager: DataManager = None):
        super().__init__(credentials_pool=credentials_pool, data_manager=data_manager)
        self.data_manager = data_manager
        self.auth_unit = data_manager.auth_unit
    
    def setSearchFilter(self, search_filter):
        super().setSearchFilter(search_filter)
        self.selector = self.search_filter.get('selector') if self.search_filter.get('selector') else ""  # group, groups, numbers, locale
        # self.operator = self.search_filter.get('operator') if self.search_filter.get('operator') else ""
        self.groups = self.search_filter.get('groups') if self.search_filter.get('groups') else ""
        self.country = self.search_filter.get('country') if self.search_filter.get('country') else ""
        self.city = self.search_filter.get('city') if self.search_filter.get('city') else ""
        print(f'\n-selector: {self.selector}\n-groups: {self.groups}\n-country: {self.country}\n-city: {self.city}\n')
    
    def run(self):
        if self.selector == 'groups':
            random_sleep(3, 5, 'Go parse groups')
            ParserGroups.__init__(
                self,
                country = self.country,
                city = self.city,
                phone = self.creds['phone'],
                api_id = self.creds['api_id'],
                api_hash = self.creds['api_hash'],
                size_archive = 35
            )
            if self.groups:
                for group in self.groups:
                    print(f'\n-GO PARSE GROUP: {group}')
                    loop = asyncio.new_event_loop()
                    loop.run_until_complete(ParserGroups().parserGroup(group))
                    print(f'\nGROUP: {group} - PARSED')
            else:
                print('\nADD groups to parse!\n')
        elif self.selector == 'numbers':
            print(f'\n-GO PARSE NUMBERS')
            loop = asyncio.new_event_loop()
            loop.run_until_complete(ParseNumbers(self.country, 35, self.credentials_pool, self.data_manager).goParseNumbers())
        else:
            random_sleep(5, 7, 'Enter selector!!!')
