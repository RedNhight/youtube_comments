import pickle


class PickleWork:
    def __init__(self):
        self.structure = {
            'ChannelName': 'ID'
        }
        with open('files/ids.pickle', 'rb') as pickle_read:
            self.unpickler = pickle.Unpickler(pickle_read)
            self.score = self.unpickler.load()
            pickle_read.close()

    def write_to_file(self, channelname, our_id):
        with open('files/ids.pickle', 'wb') as write_to_pickle:
            self.score.update({channelname: our_id})
            pickle.dump(self.score, write_to_pickle)
            write_to_pickle.close()

    def test_write(self):
        with open('files/ids.pickle', 'wb') as pickle_test_dump:
            pickle.dump(self.structure, pickle_test_dump)


if __name__ == '__main__':
    pass
