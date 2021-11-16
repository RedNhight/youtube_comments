from automatization.likes import YoutubeLiker


class TestYoutubeLiker:
    def __init__(self):
        # self.first_data = ['skriptik101@gmail.com', 'skriptik$2021']
        # self.second_data = ['skriptik102@gmail.com', 'skriptik$2021']
        # self.third_data = ['skriptik103@gmail.com', 'skriptik$2021']
        with open('files/accounts.txt', 'r') as accounts:
            rd = accounts.read().split('\n')
            self.first_data = rd[0].split(':')
            self.second_data = rd[1].split(':')
            self.third_data = rd[2].split(':')

        self.yl_first = YoutubeLiker()
        print('Браузер открыт')
        self.yl_second = YoutubeLiker()
        print('Второй браузер открыт. ')
        self.yl_third = YoutubeLiker()
        print('3-й браузер открыт.')

        self.yl_first.login(self.first_data[0], self.first_data[1])
        # print('Первый аккаунт залогинен! ')
        self.yl_second.login(self.second_data[0], self.second_data[1])
        # print('Второй аккаунт залогинен! ')
        self.yl_third.login(self.third_data[0], self.third_data[1])
        # print('3-й аккаунт залогинен!')

    def start_work(self, video_url, text_for, channel_num):
        with open('logs/info.txt', 'a') as logfile:
            if channel_num == 0:
                logfile.write(f'Аккаунт {self.first_data[0]} добавил комментарий на видео "https://www.youtube.com/watch?v={video_url}"\n')
                self.yl_first.like_the_video(video_url, text_for)
            elif channel_num == 1:
                logfile.write(f'Аккаунт {self.second_data[0]} добавил комментарий на видео "https://www.youtube.com/watch?v={video_url}"\n')
                self.yl_second.like_the_video(video_url, text_for)
            elif channel_num == 2:
                logfile.write(f'Аккаунт {self.third_data[0]} добавил комментарий на видео "https://www.youtube.com/watch?v={video_url}"\n')
                self.yl_third.like_the_video(video_url, text_for)
