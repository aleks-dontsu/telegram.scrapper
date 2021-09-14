"""
This is file to cnfigurate and connect your instaneces
(at least of UsersCollector and UsersDataCollector)
"""
from scrapping import *
from telegram import TgSelector


headers = {'1': '2'}
cookies = {
    'phone': '+380*********',
    'api_id': 123123123,
    'api_hash': '*********************************'
}
cookies_All = {
    'phone': '+380*********',
    'api_id': 123123123,
    'api_hash': '*********************************'
}
proxy = 'log:pass@ip:port'
credentials_pool = CredentialsPool(credentials_list=[{
    'user': '',
    'password': '',
    'headers': headers,
    'cookies': cookies,
    'proxy': proxy
    }], auth_unit=auth_unit)

auth_unit = AuthUnit('***.***.**.**:8007')

# credentials_pool = CredentialsPool(credentials_list=[], auth_unit=auth_unit)

data_manager = DataManager(
    storage_ip='***.***.**.**',
    storage_port='8007',
    send_users_url='/users',
    get_users_url='/users',
    mark_unused_users_url='/unused',
    auth_unit=auth_unit
)
# auth_unit = AuthUnit(data_manager.storage_ip)
filter_forwarder = FilterForwarder(
    ip='***.***.**.**',
    port='8080',
    filter_url='/api/addToFilterQ/',
    ready_check_url='/api/'
)
users_collector = UsersDataCollector(
    credentials_pool=credentials_pool,
    data_manager=data_manager,
    # filter_forwarder=filter_forwarder,
)
usersdata_collector = TgSelector(
    credentials_pool=credentials_pool,
    data_manager=data_manager,
    # filter_forwarder=filter_forwarder,
)

THIS_SCRAPPER = Scrapper(users_collector, usersdata_collector)

if __name__ == '__main__':
    THIS_SCRAPPER.login()
