# Local files.
from utils.pickle_read import *
from handlers.check_new import *
from test import TestYoutubeLiker
from automatization.likes import YoutubeLiker

# Libraries.
import random
from time import sleep
from multiprocessing import Pool

tyl = TestYoutubeLiker()


def read_channels():
    with open('files/the_first_channel.txt', 'r') as first:
        f = first.read().split('\n')
    with open('files/the_second_channel.txt', 'r') as second:
        s = second.read().split('\n')
    with open('files/the_first_channel.txt', 'r') as third:
        t = third.read().split('\n')
    return [f, s, t]


def main(url: str, proxy: str, text_for: str, num_of_account):
    print(f'Данные \nСсыка: {url}\n текст: {text_for} \nНомер аккаунта: {num_of_account}. ')
    ca = CheckAvailability(url, proxy)
    ca.pars_the_last_video()
    compared_video = ca.compare_id()
    print(url)
    if compared_video == 'NEW_VIDEO':
        print(ca.video_id)
        tyl.start_work(ca.video_id, text_for, num_of_account)
    elif compared_video == 'OLD_VIDEO':
        print(ca.video_id)
        print('OLD')


if __name__ == '__main__':
    while True:
        channels_list = read_channels()
        for i in range(len(channels_list)):
            for j in range(len(channels_list[i])):
                main(channels_list[i][j], '', 'Random text for our channel. ', i)
            sleep(10)
        sleep(600)
