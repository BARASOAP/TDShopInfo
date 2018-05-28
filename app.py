import io
import os
import directkeys
import time

import pyscreenshot as ImageGrab

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

class ScreenShot:
    """Class to hold a screenshot"""

    def __init__(self):
        self.im=ImageGrab.grab()
        self.buffer = io.BytesIO()
        self.im.save(self.buffer, 'PNG')
        self.buffer.seek(0)
        self.image = types.Image(content=self.buffer.getvalue())
        self.response = client.text_detection(image=self.image)
        self.texts = self.response.text_annotations

    def print_labels(self):
        for text in self.texts:
            print(text.description)

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

            print(f'bounds: {",".join(vertices)}')

class KeyBoard:
    def __init__(self, time=.1):
        self.time = time
        self.key_options = {
            'w':directkeys.W,
            'a':directkeys.A,
            's':directkeys.S,
            'd':directkeys.D,
        }

    def tap(self, key):
        dx_scan_code = self.key_options[key.lower()]
        directkeys.PressKey(dx_scan_code)
        time.sleep(self.time)
        directkeys.ReleaseKey(dx_scan_code)

# ss1 = ScreenShot('1.jpg')
# ss1.print_labels()

# kb = KeyBoard()
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)
# kb.tap("S")

if __name__ == "__main__":
    kb = KeyBoard()

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    ss1 = ScreenShot()
    ss1.print_labels()
    kb.tap('s')
    ss2 = ScreenShot()
    ss2.print_labels()
    kb.tap('s')
    ss3 = ScreenShot()
    ss3.print_labels()