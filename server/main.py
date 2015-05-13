# -*- coding: utf-8 -*-
import uuid
import re
import web
from PIL import Image

urls = {
    '/upload', 'Upload'
}


class Upload:
    def __init__(self):
        self.upload_dir = "./upload"

    def GET(self):
        pass

    def POST(self):
        data = web.input(img={})

        if 'img' in data:
            filepath = data.img.filename.replace('\\', '/')
            extension = filepath.rsplit(".", 1)[1]
            extension = re.sub("[^a-zA-Z0-9]", "", extension).lower()
            filename = str(uuid.uuid4()) + "." + extension
            fout = open(self.upload_dir + '/' + filename, 'w')
            fout.write(data.img.file.read())
            fout.close()

            self.thumbnail(filename)
            return "ok"

    def thumbnail(self, filename):
        img = Image.open(self.upload_dir + '/' + filename)
        img.thumbnail((256, 256))
        img.save(self.upload_dir + '/thumbnail/' + filename)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
