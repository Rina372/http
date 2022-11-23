from pprint import pprint

import requests

from ya_disk import YandexDisk

TOKEN = y0_AgAAAAAXrQeXAADLWwAAAADUvA9-L8o74WJrTzqpqTNwsuN7I2v82rk

if __name__ == '__main__':
    ya = YandexDisk(token= TOKEN)
    ya.upload_file_to_disk("test.txt")

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        

