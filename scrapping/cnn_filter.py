import requests
import time
from .validators import validateURL


class FilterForwarder:
    def __init__(self, ip, port, filter_url, ready_check_url, cnn_filter_params={}):
        self.ip = ip
        self.port = port
        self.filter_url = validateURL(filter_url)
        self.ready_check_url = validateURL(ready_check_url)
        self.cnn_filter_params = {
            'min_beauty_score': 0.5,
            'min_geometry_score': 3,
            'min_age': 16,
            'max_age': 30,
            'gender': 1,
            **cnn_filter_params
        }

    def _waitWhileBusy(self, delay=10):
        response_code = 0
        while response_code != 200:
            url = f"http://{self.ip}:{self.port}{self.ready_check_url}"
            try:
                response_code = requests.get(url).status_code
            except requests.exceptions.ConnectionError as e:
                response_code = '\n Server not active\n'
            print('######################')
            print(url)
            print(f'\nStatus from CNN serve: \n\t{response_code}\n')
            print('######################')
            if response_code != 200:
                time.sleep(delay)

    def sendArchive(self, path_to_archive):
        self._waitWhileBusy()
        url = f"http://{self.ip}:{self.port}{self.filter_url}"
        files = {'archive': open(path_to_archive, 'rb')}
        print('######################')
        print(f'\nFiles to send: \n\t{files["archive"]}\n')
        print('######################')
        response = requests.post(
            url, files=files, data=self.cnn_filter_params)
        return response.status_code
