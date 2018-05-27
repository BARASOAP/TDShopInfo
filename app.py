import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

class ScreenShot:
    """Class to hold a screenshot"""

    def __init__(self, file):
        self.file_name = os.path.join(
            os.path.dirname(__file__),
            file)
        

        with io.open(self.file_name, 'rb') as image_file:
            self.content = image_file.read()

        self.image = types.Image(content=self.content)

        self.response = client.text_detection(image=self.image)
        self.texts = self.response.text_annotations

    def print_labels(self):
        for text in self.texts:
            print(text.description)

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

            print(f'bounds: {",".join(vertices)}')

ss1 = ScreenShot('1.jpg')
ss1.print_labels()