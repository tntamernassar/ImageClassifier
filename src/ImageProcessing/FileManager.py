import os
import calendar
import time


class FileManager:
    def __init__(self, root):
        self.root = root
        self.ts = len(self.listdir())

    def timestamp(self):
        ts = self.ts
        self.ts += 1
        return str(ts)

    def mkdir(self, _dir):
        os.mkdir(self.root + "/" + _dir)

    def listdir(self):
        dirs = list(os.walk(self.root))
        root_dir = dirs[0]
        sub_dirs = root_dir[1]
        return sorted(sub_dirs, key=lambda ts: int(ts), reverse=True)

    def upload_file(self, path, file_name, file_storage):
        file_storage.save(self.root + "/" + path + "/" + file_name)

    def get_images(self, folder):
        images = list(os.walk(self.root + "/" + folder))
        root_dir = images[0]
        sub_dirs = root_dir[2]
        return sub_dirs
