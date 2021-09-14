import requests
import shutil
import os


class PhotosDownloader:
    @staticmethod
    def uploadPhotos(linksList, path):
        for (link, photo_id) in linksList:
            response = requests.get(link, stream=True)
            if response.status_code == 200:
                with open(os.path.join(path, photo_id + '.jpg'), 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
