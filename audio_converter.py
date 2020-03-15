import os


class AudioConverter(object):
    def __init__(self, type_from=None, type_to='aiff'):
        if type_from is None:
            type_from = ['.flac', '.m4a']

        self.type_from = type_from
        self.type_to = type_to
        self.to_convert = []

    def _add_file(self, file, dir):
        ext = os.path.splitext(file)[-1].lower()
        if ext in self.type_from:
            added_file = os.path.join(dir, file)
            print(added_file)
            self.to_convert.append(added_file)

    def add_folder(self, folder_path, recurse=True):
        if recurse:
            for subdir, dirs, files in os.walk(folder_path):
                [self._add_file(file, subdir) for file in files]
        else:
            [self._add_file(file, folder_path) for file in os.listdir(folder_path)]


if __name__ == '__main__':
    ac = AudioConverter()
    ac.add_folder('/Users/broccoli/Music/The Broccoli Smuggler/')
