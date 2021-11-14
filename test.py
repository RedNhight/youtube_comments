from automatization.likes import YoutubeLiker


class TestYoutubeLiker:
    def __init__(self):
        self.yl_first = YoutubeLiker()
        print('Браузер открыт')
        self.yl_second = YoutubeLiker()
        print('Второй браузер открыт. ')
        self.yl_third = YoutubeLiker()
        print('3-й браузер открыт.')

        self.yl_first.login('skriptik101@gmail.com', 'skriptik$2021', '+380999324388')
        print('Первый аккаунт залогинен! ')
        self.yl_second.login('skriptik102@gmail.com', 'skriptik$2021', '+380999324388')
        print('Второй аккаунт залогинен! ')
        self.yl_third.login('skriptik103@gmail.com', 'skriptik$2021', '+380999324388')
        print('3-й аккаунт залогинен!')

    def start_work(self, video_url, text_for, channel_num):
        if channel_num == 0:
            self.yl_first.like_the_video(video_url, text_for)
        elif channel_num == 1:
            self.yl_second.like_the_video(video_url, text_for)
        elif channel_num == 2:
            self.yl_third.like_the_video(video_url, text_for)
