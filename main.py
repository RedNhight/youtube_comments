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


def read_comments():
    with open('files/t_comments.txt', 'r') as first:
        f = first.read().split('\n')
    with open('files/s_comments.txt', 'r') as second:
        s = second.read().split('\n')
    with open('files/t_comments.txt', 'r') as third:
        t = third.read().split('\n')
    return [f, s, t]


def read_channels():
    with open('files/the_first_channel.txt', 'r') as first:
        f = first.read().split('\n')
    with open('files/the_second_channel.txt', 'r') as second:
        s = second.read().split('\n')
    with open('files/the_third_channel.txt', 'r') as third:
        t = third.read().split('\n')
    return [f, s, t]


def main(url: str, txt_for: str, num_of_account):
    ca = CheckAvailability(url)
    ca.pars_the_last_video()
    compared_video = ca.compare_id()
    if compared_video == 'NEW_VIDEO':
        print('New video')
        print(ca.video_id)
        tyl.start_work(ca.video_id, txt_for, num_of_account)
        print('Video was commented. ')
    elif compared_video == 'OLD_VIDEO':
        print(ca.video_id)
        print('OLD')


if __name__ == '__main__':
    while True:
        channels_list = read_channels()
        for i in range(len(channels_list)):
            text_for = random.choice(read_comments()[i])
            for j in range(len(channels_list[i])):
                main(channels_list[i][j], text_for, i)
            sleep(10)
        sleep(600)
