from threading import Thread, Lock
from os import listdir


class FileWriter:
    def __init__(self, path):
        self.path = path
        self.lock = Lock()

    def write(self, line):
        open(self.path, 'a', encoding='utf-8').write(line)


class FileReader(Thread):
    def __init__(self, file_to_write, path_to_reader):
        super().__init__()
        self.file_to_write = file_to_write
        self.path_to_reader = path_to_reader

    def read(self):
        line = open(self.path_to_reader, 'r', encoding='koi8-r').read().replace('~', '').split('#')
        file_name = str(self.path_to_reader).split('/')[-1].replace('.mob', '')
        result = ''
        for i in line:
                splitted = i.split('\n')
                if len(splitted) > 8:
                    result += '|'.join([splitted[0], splitted[1], splitted[8]]) + '\n'
        return file_name + ':\n' + result

    def run(self):
        self.file_to_write.lock.acquire()
        self.file_to_write.write(self.read())
        self.file_to_write.lock.release()


if __name__ == '__main__':
    file_to_write = FileWriter('/Users/Ihor/Downloads/mob/result')
    for mob in listdir('/Users/Ihor/Downloads/mob'):
        if mob != 'index':
            read_file = FileReader(file_to_write, '/Users/Ihor/Downloads/mob/' + str(mob))
            read_file.start()
