from time import time

from threading import Thread

import requests


class DownloadHeader(Thread):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    res = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    data = res.json()
    for mm_dict in data['newslist']:
        url = mm_dict['picUrl']

        DownloadHeader(url).start()


if __name__ == '__main__':
    main()