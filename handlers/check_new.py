import requests
from bs4 import BeautifulSoup
from utils.pickle_read import PickleWork


class CheckAvailability:
    def __init__(self, url, proxy):
        self.video_id = ''
        self.url = url
        proxs = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}',
        }
        if '/videos' in self.url:
            self.r = requests.get(self.url)
        elif '/videos' not in self.url:
            self.r = requests.get(self.url+'/videos')

        self.soup = BeautifulSoup(self.r.content, 'html.parser')

    def pars_the_last_video(self):
        id_splt = str(self.soup).split('createPlaylistServiceEndpoint')[1][0:40]
        self.video_id = id_splt.split('"')[4]

    def compare_id(self):
        cp = PickleWork()
        if self.url in cp.score:
            if cp.score[self.url] != self.video_id:
                cp.write_to_file(self.url, self.video_id)
                return 'NEW_VIDEO'
            else:
                return 'OLD_VIDEO'
        else:
            cp.write_to_file(self.url, self.video_id)


if __name__ == '__main__':
    ca = CheckAvailability('https://www.youtube.com/c/ikakProsto')
    ca.pars_the_last_video()
