

class DatabaseManager:

    def __init__(self, file_manager):
        self.images = {}
        self.id = 0
        current_images = file_manager.listdir()
        for img in current_images:
            self.insert_img(img)

    def insert_img(self, image_path):
        _id = self.id
        self.images[_id] = image_path
        self.id += 1
        return _id

    def get_images(self):
        return self.images
